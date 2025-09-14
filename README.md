# CorpMeet-AI 🤖

> **AI-Powered Corporate Meeting Minutes & Action Tracker**

Transform your meeting transcripts into actionable insights with AI-powered analysis. CorpMeet-AI automatically generates meeting summaries, extracts action items, identifies key decisions, and creates professional PDF reports.

![CorpMeet-AI Demo](https://via.placeholder.com/800x400/1e40af/ffffff?text=CorpMeet-AI+Demo)

## ✨ Features

### 🎯 **Core Functionality**
- **Smart Meeting Processing**: Upload text files (.txt) or Word documents (.docx), or paste transcript directly
- **AI-Powered Analysis**: Automatically extract structured information from meeting transcripts
- **Professional PDF Export**: Generate beautifully formatted meeting minutes
- **Meeting History**: Access and manage all previously processed meetings
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices

### 🔍 **AI Extraction Capabilities**
- **Meeting Summary**: 3-5 key bullet points highlighting main discussion topics
- **Action Items**: Structured tasks with assigned owners and deadlines
- **Key Decisions**: Important conclusions and decisions made during the meeting
- **Original Transcript**: Preserve and access the complete original text

### 💼 **Professional Features**
- **Corporate Design**: Clean, professional interface with Bootstrap 5
- **PDF Reports**: Professional meeting minutes with company-ready formatting
- **Data Persistence**: SQLite database for reliable data storage
- **API Access**: JSON endpoints for integration with other tools

## 🛠️ Tech Stack

- **Backend**: Python 3.8+, Flask, SQLAlchemy
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Database**: SQLite (easily upgradeable to PostgreSQL/MySQL)
- **PDF Generation**: ReportLab
- **Document Processing**: python-docx
- **AI Integration**: OpenAI API (configurable)

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Jani-shiv/AI-Powered-Corporate-Meeting-Minutes-Action-Tracker.git
   cd AI-Powered-Corporate-Meeting-Minutes-Action-Tracker
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   - Open your browser and navigate to: `http://localhost:5000`
   - Start processing your meeting transcripts!

### 🔧 Environment Setup (Optional)

For OpenAI integration, create a `.env` file:
```env
OPENAI_API_KEY=your_openai_api_key_here
SECRET_KEY=your_secret_key_for_production
```

## 📖 Usage Guide

### 1. **Upload Meeting Transcript**
- Navigate to "Upload Transcript" from the main menu
- Choose your input method:
  - **Paste Text**: Copy and paste your meeting transcript directly
  - **Upload File**: Upload .txt or .docx files (max 16MB)
- Enter a descriptive meeting title
- Click "Generate Meeting Minutes"

### 2. **Review Results**
- View the AI-generated meeting summary
- Check extracted action items with assignments and deadlines
- Review key decisions made during the meeting
- Access the original transcript if needed

### 3. **Export and Save**
- **Export PDF**: Download professional meeting minutes
- **Save Meeting**: Store in your meeting history
- **Process Another**: Upload additional transcripts

### 4. **Manage Past Meetings**
- Access "Past Meetings" to view your history
- Click on any meeting to view full details
- Export individual meetings as PDFs
- Delete old meetings if needed

## 🏗️ Project Structure

```
CorpMeet-AI/
├── app.py                  # Main Flask application
├── models.py              # Database models (SQLAlchemy)
├── ai_processor.py        # AI processing logic
├── pdf_generator.py       # PDF generation utilities
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── LICENSE               # License file
├── templates/            # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Homepage
│   ├── upload.html       # Upload page
│   ├── results.html      # Results display
│   ├── past_meetings.html # Meeting history
│   ├── 404.html          # Error page
│   └── 500.html          # Error page
├── static/               # Static assets
│   ├── css/
│   │   └── style.css     # Custom CSS styling
│   └── downloads/        # Generated PDF files
└── uploads/              # Temporary file storage
```

## 🔗 API Endpoints

### REST API
- `GET /` - Homepage
- `GET /upload` - Upload page
- `POST /process_transcript` - Process meeting transcript
- `GET /results/<meeting_id>` - View meeting results
- `GET /past_meetings` - Meeting history
- `GET /export_pdf/<meeting_id>` - Download PDF
- `POST /delete_meeting/<meeting_id>` - Delete meeting
- `GET /api/meetings` - JSON API for all meetings

### Example API Response
```json
{
  "id": 1,
  "title": "Weekly Team Standup",
  "date_created": "2025-09-14T10:30:00",
  "summary": [
    "Discussed project status and upcoming milestones",
    "Reviewed current blockers and solutions",
    "Aligned on next week's priorities"
  ],
  "action_items": [
    {
      "task": "Complete user authentication module",
      "owner": "Sarah Johnson", 
      "deadline": "2025-09-18"
    }
  ],
  "decisions": [
    "Approved moving to weekly sprint cycles",
    "Decided to prioritize mobile responsiveness"
  ]
}
```

## 🤖 AI Integration

### Current Implementation
The application includes a **mock AI processor** that demonstrates the expected functionality. It analyzes meeting transcripts and generates structured output including summaries, action items, and decisions.

### OpenAI Integration
To enable real OpenAI processing:

1. **Get an OpenAI API key** from [OpenAI Platform](https://platform.openai.com/)

2. **Set environment variables**:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

3. **Uncomment the OpenAI code** in `ai_processor.py`:
   ```python
   # Uncomment the process_with_openai function
   # Update the process_meeting_transcript function to use OpenAI
   ```

### Custom AI Models
The modular design allows easy integration with other AI services:
- Azure OpenAI
- Google PaLM API
- Anthropic Claude
- Custom trained models

## 🎨 Customization

### Styling
- Modify `static/css/style.css` for custom branding
- Update color scheme in CSS variables
- Replace logo and icons as needed

### Database
- SQLite is used by default for simplicity
- Easily upgrade to PostgreSQL or MySQL for production
- Update connection string in `app.py`

### Features
- Add user authentication
- Implement team collaboration
- Add calendar integration
- Extend with custom AI prompts

## 🧪 Development

### Running in Development Mode
```bash
# Enable debug mode
export FLASK_ENV=development
python app.py
```

### Database Management
```python
# Reset database (caution: deletes all data)
from app import app, db
with app.app_context():
    db.drop_all()
    db.create_all()
```

### Testing Uploads
Sample meeting transcript for testing:
```
Meeting: Weekly Team Standup
Date: September 14, 2025
Attendees: Sarah Johnson (Project Manager), Mike Chen (Developer), Alex Rodriguez (Designer)

Sarah: Good morning everyone. Let's start with our weekly standup. Mike, can you give us an update on the authentication module?

Mike: Sure, I'm about 80% complete with the user authentication system. I should have it finished by Wednesday. The main challenge has been integrating with our existing database schema.

Alex: I've completed the new UI mockups for the dashboard. I'll send them to the team for review today. We should schedule a design review meeting for Thursday.

Sarah: Great work both of you. Let's make sure we stay on track for our sprint deadline next Friday. 

Action Items:
- Mike to complete authentication module by Wednesday
- Alex to send UI mockups for team review
- Sarah to schedule design review meeting for Thursday

Decisions:
- Approved the new dashboard design direction
- Decided to extend sprint deadline by one day due to complexity
```

## 📝 Contributing

We welcome contributions to CorpMeet-AI! Here's how you can help:

### Development Process
1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes** and add tests if applicable
4. **Commit your changes**: `git commit -m 'Add amazing feature'`
5. **Push to the branch**: `git push origin feature/amazing-feature`
6. **Open a Pull Request**

### Code Standards
- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Update documentation for new features

### Areas for Contribution
- 🔐 **Authentication**: User management and security
- 🎨 **UI/UX**: Design improvements and accessibility
- 🤖 **AI Models**: Advanced processing capabilities
- 📊 **Analytics**: Meeting insights and reporting
- 🔌 **Integrations**: Calendar, Slack, Teams integration
- 🧪 **Testing**: Unit tests and integration tests

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Bootstrap Team** for the excellent CSS framework
- **Flask Community** for the lightweight and powerful web framework
- **ReportLab** for professional PDF generation capabilities
- **OpenAI** for AI processing capabilities

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/Jani-shiv/AI-Powered-Corporate-Meeting-Minutes-Action-Tracker/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Jani-shiv/AI-Powered-Corporate-Meeting-Minutes-Action-Tracker/discussions)
- **Email**: [Contact the maintainer](mailto:your-email@example.com)

## 🗺️ Roadmap

### Version 2.0 (Coming Soon)
- [ ] User authentication and multi-user support
- [ ] Real-time collaboration features
- [ ] Calendar integration (Google Calendar, Outlook)
- [ ] Advanced AI prompts and customization
- [ ] Mobile app (React Native)

### Version 2.1
- [ ] Team workspaces and permissions
- [ ] Integration with Slack, Microsoft Teams
- [ ] Meeting analytics and insights
- [ ] Custom AI model training
- [ ] Enterprise deployment options

---

<div align="center">

**Built with ❤️ for better meeting management**

[![GitHub stars](https://img.shields.io/github/stars/Jani-shiv/AI-Powered-Corporate-Meeting-Minutes-Action-Tracker?style=social)](https://github.com/Jani-shiv/AI-Powered-Corporate-Meeting-Minutes-Action-Tracker)
[![GitHub issues](https://img.shields.io/github/issues/Jani-shiv/AI-Powered-Corporate-Meeting-Minutes-Action-Tracker)](https://github.com/Jani-shiv/AI-Powered-Corporate-Meeting-Minutes-Action-Tracker/issues)
[![GitHub license](https://img.shields.io/github/license/Jani-shiv/AI-Powered-Corporate-Meeting-Minutes-Action-Tracker)](https://github.com/Jani-shiv/AI-Powered-Corporate-Meeting-Minutes-Action-Tracker/blob/main/LICENSE)

</div>