"""
CorpMeet-AI: AI-Powered Corporate Meeting Minutes & Action Tracker
Main Flask application with all routes and functionality.
"""

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    send_file,
    jsonify,
)
from werkzeug.utils import secure_filename
import os
from docx import Document

# Import our custom modules
from models import db, Meeting
from ai_processor import process_meeting_transcript
from pdf_generator import create_meeting_minutes_pdf, create_downloads_directory

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config["SECRET_KEY"] = (
    "your-secret-key-change-in-production"  # Change this in production!
)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///corpmeet_ai.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB max file size

# Initialize database
db.init_app(app)

# Allowed file extensions for upload
ALLOWED_EXTENSIONS = {"txt", "docx"}


def allowed_file(filename):
    """Check if uploaded file has an allowed extension."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def extract_text_from_file(file_path):
    """Extract text content from uploaded file (txt or docx)."""
    try:
        if file_path.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()
        elif file_path.endswith(".docx"):
            doc = Document(file_path)
            return "\n".join([paragraph.text for paragraph in doc.paragraphs])
        else:
            return None
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


@app.route("/")
def homepage():
    """Homepage with navigation options."""
    return render_template("index.html")


@app.route("/upload")
def upload_page():
    """Upload page for meeting transcripts."""
    return render_template("upload.html")


@app.route("/process_transcript", methods=["POST"])
def process_transcript():
    """Process uploaded transcript or pasted text."""

    transcript_text = ""
    meeting_title = request.form.get("meeting_title", "Untitled Meeting")

    # Check if text was pasted in textarea
    pasted_text = request.form.get("transcript_text", "").strip()

    if pasted_text:
        transcript_text = pasted_text
    else:
        # Check if file was uploaded
        if "transcript_file" not in request.files:
            flash("No file uploaded and no text provided", "error")
            return redirect(url_for("upload_page"))

        file = request.files["transcript_file"]

        if file.filename == "":
            flash("No file selected", "error")
            return redirect(url_for("upload_page"))

        if file and allowed_file(file.filename):
            # Save uploaded file
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)

            # Extract text from file
            transcript_text = extract_text_from_file(filepath)

            # Clean up uploaded file
            os.remove(filepath)

            if not transcript_text:
                flash("Could not extract text from uploaded file", "error")
                return redirect(url_for("upload_page"))
        else:
            flash("Invalid file type. Please upload .txt or .docx files only", "error")
            return redirect(url_for("upload_page"))

    if not transcript_text or len(transcript_text.strip()) < 20:
        flash(
            "Transcript text is too short. Please provide a more detailed transcript.",
            "error",
        )
        return redirect(url_for("upload_page"))

    try:
        # Process transcript with AI
        ai_result = process_meeting_transcript(transcript_text)

        # Create new meeting record
        meeting = Meeting(
            title=meeting_title,
            summary=ai_result["summary"],
            action_items=ai_result["action_items"],
            decisions=ai_result["decisions"],
            original_transcript=transcript_text,
        )

        # Save to database
        db.session.add(meeting)
        db.session.commit()

        flash("Meeting transcript processed successfully!", "success")
        return redirect(url_for("view_results", meeting_id=meeting.id))

    except Exception as e:
        print(f"Error processing transcript: {e}")
        flash("Error processing transcript. Please try again.", "error")
        return redirect(url_for("upload_page"))


@app.route("/results/<int:meeting_id>")
def view_results(meeting_id):
    """Display processing results for a specific meeting."""

    meeting = Meeting.query.get_or_404(meeting_id)

    return render_template("results.html", meeting=meeting)


@app.route("/past_meetings")
def past_meetings():
    """Display list of past meetings."""

    meetings = Meeting.query.order_by(Meeting.date_created.desc()).all()

    return render_template("past_meetings.html", meetings=meetings)


@app.route("/meeting/<int:meeting_id>")
def view_meeting(meeting_id):
    """View details of a specific past meeting."""

    meeting = Meeting.query.get_or_404(meeting_id)

    return render_template("meeting_details.html", meeting=meeting)


@app.route("/export_pdf/<int:meeting_id>")
def export_pdf(meeting_id):
    """Export meeting minutes as PDF."""

    meeting = Meeting.query.get_or_404(meeting_id)

    try:
        # Ensure downloads directory exists
        create_downloads_directory()

        # Generate PDF
        pdf_path = create_meeting_minutes_pdf(meeting)

        # Send file to user
        return send_file(
            pdf_path, as_attachment=True, download_name=os.path.basename(pdf_path)
        )

    except Exception as e:
        print(f"Error generating PDF: {e}")
        flash("Error generating PDF. Please try again.", "error")
        return redirect(url_for("view_results", meeting_id=meeting_id))


@app.route("/save_meeting/<int:meeting_id>")
def save_meeting(meeting_id):
    """Save meeting (already saved, just show confirmation)."""

    meeting = Meeting.query.get_or_404(meeting_id)
    flash(f'Meeting "{meeting.title}" has been saved successfully!', "success")

    return redirect(url_for("past_meetings"))


@app.route("/delete_meeting/<int:meeting_id>", methods=["POST"])
def delete_meeting(meeting_id):
    """Delete a meeting from the database."""

    meeting = Meeting.query.get_or_404(meeting_id)

    try:
        db.session.delete(meeting)
        db.session.commit()
        flash(f'Meeting "{meeting.title}" deleted successfully', "success")
    except Exception as e:
        print(f"Error deleting meeting: {e}")
        flash("Error deleting meeting. Please try again.", "error")

    return redirect(url_for("past_meetings"))


@app.route("/api/meetings")
def api_meetings():
    """API endpoint to get all meetings as JSON."""

    meetings = Meeting.query.order_by(Meeting.date_created.desc()).all()

    meetings_data = []
    for meeting in meetings:
        meetings_data.append(
            {
                "id": meeting.id,
                "title": meeting.title,
                "date_created": meeting.date_created.isoformat(),
                "summary": meeting.get_summary(),
                "action_items": meeting.get_action_items(),
                "decisions": meeting.get_decisions(),
            }
        )

    return jsonify(meetings_data)


@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors."""
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    db.session.rollback()
    return render_template("500.html"), 500


# Create database tables
with app.app_context():
    # Ensure upload directory exists
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    # Create database tables
    db.create_all()

    print("Database tables created successfully!")

if __name__ == "__main__":
    # Run the Flask application
    print("Starting CorpMeet-AI application...")
    print("Access the application at: http://localhost:5000")

    app.run(debug=True, host="0.0.0.0", port=5000)
