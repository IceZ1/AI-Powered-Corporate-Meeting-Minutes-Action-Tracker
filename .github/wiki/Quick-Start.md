# 🚀 Quick Start Guide

Get CorpMeet-AI up and running in just **5 minutes**! This guide will walk you through your first AI-powered meeting analysis.

## 📋 Prerequisites

Before starting, ensure you have:
- ✅ Python 3.8+ installed
- ✅ Git installed  
- ✅ Basic command line knowledge
- ✅ A meeting recording file (MP3, WAV, MP4, etc.)

## 🛠️ Step 1: Installation

### 📁 Clone the Repository
```bash
git clone https://github.com/Jani-shiv/AI-Powered-Corporate-Meeting-Minutes-Action-Tracker.git
cd AI-Powered-Corporate-Meeting-Minutes-Action-Tracker
```

### 🐍 Set Up Python Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 🔧 Initialize Database
```bash
python app.py
```

The application will automatically create the SQLite database on first run.

## 🎯 Step 2: First Launch

### 🌐 Start the Application
```bash
python app.py
```

You should see:
```
🚀 CorpMeet-AI Server Starting...
📊 Database initialized successfully
🌐 Server running on http://localhost:5000
💡 Visit the URL above to access CorpMeet-AI
```

### 🎉 Access the Interface
Open your web browser and navigate to: **http://localhost:5000**

## 📁 Step 3: Upload Your First Meeting

### 🎵 Prepare Your Recording
Supported formats:
- **Audio**: MP3, WAV, M4A, AAC
- **Video**: MP4, AVI, MOV (audio will be extracted)
- **Max Size**: 100MB per file

### ⬆️ Upload Process
1. **Click "Choose File"** - Select your meeting recording
2. **Add Meeting Title** - Enter a descriptive name (e.g., "Weekly Team Standup")
3. **Click "Upload & Process"** - Watch the magic happen!

### ⏳ Processing Time
- **Small files** (< 10MB): 30-60 seconds
- **Medium files** (10-50MB): 1-3 minutes  
- **Large files** (50-100MB): 3-5 minutes

## 🤖 Step 4: Review AI Results

Once processing completes, you'll see:

### 📊 Meeting Summary
- **Key Topics**: Main discussion points
- **Meeting Duration**: Automatically calculated
- **Participant Count**: Estimated from audio analysis
- **Meeting Type**: Detected based on content

### ✅ Action Items
```
🎯 Action Items Detected:
1. John to prepare Q3 financial report by Friday
2. Sarah to schedule client demo for next week
3. Team to review new project proposal by Tuesday
```

### 🔍 Key Decisions
```
📋 Decisions Made:
• Approved budget increase for marketing campaign
• Selected new project management tool
• Scheduled quarterly review for next month
```

### 👥 Participants
```
🗣️ Detected Speakers:
• Speaker 1 (Main presenter)
• Speaker 2 (Active participant)
• Speaker 3 (Occasional contributor)
```

## 📄 Step 5: Generate Professional Report

### 🖨️ Export PDF
1. **Click "Export PDF"** button
2. **Download automatically starts**
3. **Professional report** with your company branding

### 📋 PDF Contents
- Executive summary
- Detailed action items with assignments
- Key decisions and outcomes
- Meeting timeline and participants
- Professional formatting

## 🔍 Step 6: Explore Features

### 📚 Meeting History
- View all processed meetings
- Search by title, date, or content
- Filter by meeting type or participants
- Quick access to previous reports

### 🎨 Customization
- Upload company logo
- Customize PDF templates
- Set default meeting categories
- Configure AI processing preferences

## 🛡️ Step 7: Security & Privacy

### 🔒 Data Protection
- All files processed locally
- No data sent to external servers
- Meeting recordings deleted after processing
- Encrypted database storage

### 🌐 Network Requirements
- **Internet**: Only for initial setup and updates
- **Local Processing**: All AI analysis runs offline
- **Privacy First**: Your meeting data stays private

## 🚀 Step 8: What's Next?

### 🎯 Power User Features
- **API Integration**: Connect with existing tools
- **Batch Processing**: Upload multiple meetings
- **Custom Templates**: Create branded reports
- **Advanced Search**: Find any discussion point
- **Analytics Dashboard**: Track meeting trends

### 🔧 Advanced Configuration
- **Custom AI Models**: Train on your meeting style
- **Webhook Integration**: Auto-sync with project tools
- **LDAP Authentication**: Enterprise user management
- **Custom Workflows**: Automate post-meeting actions

## 💡 Pro Tips

### 🎵 Audio Quality
- **Clear Recording**: Use quality microphones
- **Minimize Background Noise**: Choose quiet environments
- **Multiple Speakers**: Ensure each person speaks clearly
- **File Format**: MP3 or WAV for best results

### 📝 Meeting Preparation
- **Structured Agenda**: Helps AI identify key points
- **Clear Action Items**: State assignments explicitly
- **Decision Points**: Clearly announce when decisions are made
- **Participant Introductions**: Help with speaker identification

### 🔄 Regular Use
- **Consistent Upload**: Process meetings immediately after
- **Review AI Results**: Improve accuracy with feedback
- **Update Software**: Get latest AI improvements
- **Backup Data**: Export important meetings regularly

## 🐛 Troubleshooting

### ❌ Common Issues

**Problem**: Upload fails
```
✅ Solution: Check file size (<100MB) and format
✅ Solution: Ensure stable internet connection
✅ Solution: Try different file format
```

**Problem**: Processing takes too long
```
✅ Solution: Check system resources (RAM/CPU)
✅ Solution: Close other applications
✅ Solution: Try smaller file first
```

**Problem**: Poor AI accuracy
```
✅ Solution: Improve audio quality
✅ Solution: Use structured meeting format
✅ Solution: Update to latest version
```

## 🎉 Success!

You've successfully:
- ✅ Installed CorpMeet-AI
- ✅ Processed your first meeting
- ✅ Generated a professional report
- ✅ Explored key features

## 🤝 Need Help?

- 📖 **Full Documentation**: [Wiki Home](Home)
- 🐛 **Report Issues**: [GitHub Issues](https://github.com/Jani-shiv/AI-Powered-Corporate-Meeting-Minutes-Action-Tracker/issues)
- 💬 **Community**: [Discussions](https://github.com/Jani-shiv/AI-Powered-Corporate-Meeting-Minutes-Action-Tracker/discussions)
- 📧 **Direct Support**: [Contact Us](mailto:support@corpmeeting.ai)

---

**🎉 Welcome to the future of meeting management!**

*Next: [Advanced Features Guide](Advanced-Features) →*