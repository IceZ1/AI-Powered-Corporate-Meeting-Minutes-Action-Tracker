# Contributing to CorpMeet-AI 🤝

Thank you for your interest in contributing to CorpMeet-AI! We welcome contributions from developers of all skill levels. This guide will help you get started with contributing to our AI-powered meeting minutes tracker.

## 🌟 How to Contribute

There are many ways to contribute to CorpMeet-AI:

- 🐛 **Report bugs** and suggest fixes
- 💡 **Propose new features** and enhancements
- 📚 **Improve documentation** and examples
- 🧪 **Write tests** and improve code coverage
- 🎨 **Enhance UI/UX** design and accessibility
- 🔧 **Fix issues** and implement features
- 🌍 **Translate** the application to other languages

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git for version control
- Basic knowledge of Flask, HTML/CSS, JavaScript
- Familiarity with AI/ML concepts (for AI-related contributions)

### Development Setup

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/AI-Powered-Corporate-Meeting-Minutes-Action-Tracker.git
   cd AI-Powered-Corporate-Meeting-Minutes-Action-Tracker
   ```

3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # Development dependencies
   ```

5. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

6. **Run the application**:
   ```bash
   python app.py
   ```

7. **Verify setup** by visiting `http://localhost:5000`

## 🔄 Development Workflow

### Creating a Feature Branch

1. **Create a new branch** for your feature:
   ```bash
   git checkout -b feature/amazing-new-feature
   ```

2. **Make your changes** following our coding standards

3. **Test your changes** thoroughly

4. **Commit your changes**:
   ```bash
   git add .
   git commit -m "feat: add amazing new feature"
   ```

5. **Push to your fork**:
   ```bash
   git push origin feature/amazing-new-feature
   ```

6. **Create a Pull Request** on GitHub

### Commit Message Guidelines

We follow the [Conventional Commits](https://conventionalcommits.org/) specification:

- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation changes
- `style:` Code style changes (formatting, etc.)
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

**Examples:**
```
feat: add real-time collaboration for meeting notes
fix: resolve PDF generation issue with special characters
docs: update API documentation with new endpoints
style: format code according to PEP 8 standards
```

## 📋 Code Standards

### Python Code Style

- Follow **PEP 8** guidelines
- Use **type hints** where appropriate
- Write **docstrings** for all functions and classes
- Maximum line length: **88 characters** (Black formatter)
- Use **meaningful variable names**

### Frontend Code Style

- Use **semantic HTML5** elements
- Follow **Bootstrap 5** conventions
- Write **accessible** code (ARIA labels, alt texts)
- Use **consistent naming** for CSS classes
- Optimize for **mobile-first** design

### Code Example

```python
def process_meeting_transcript(transcript_text: str) -> dict:
    """
    Process meeting transcript using AI to extract structured information.
    
    Args:
        transcript_text: Raw meeting transcript text
        
    Returns:
        dict: Structured meeting data containing summary, action_items, decisions
        
    Raises:
        ValueError: If transcript_text is empty or too short
    """
    if not transcript_text or len(transcript_text.strip()) < 20:
        raise ValueError("Transcript text is too short")
    
    # Process the transcript
    result = {
        "summary": extract_summary(transcript_text),
        "action_items": extract_action_items(transcript_text),
        "decisions": extract_decisions(transcript_text)
    }
    
    return result
```

## 🧪 Testing Guidelines

### Running Tests

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=app --cov-report=html

# Run specific test file
python -m pytest tests/test_ai_processor.py
```

### Writing Tests

- Write tests for **all new features**
- Include **edge cases** and **error conditions**
- Use **descriptive test names**
- Follow **AAA pattern** (Arrange, Act, Assert)

```python
def test_process_meeting_transcript_with_valid_input():
    """Test that valid transcript input returns expected structure."""
    # Arrange
    transcript = "Meeting started. John discussed project status..."
    
    # Act
    result = process_meeting_transcript(transcript)
    
    # Assert
    assert "summary" in result
    assert "action_items" in result
    assert "decisions" in result
    assert len(result["summary"]) > 0
```

## 🎨 UI/UX Guidelines

### Design Principles

- **Corporate Professional**: Clean, minimal, business-appropriate
- **Accessibility First**: WCAG 2.1 AA compliance
- **Mobile Responsive**: Works on all screen sizes
- **Consistent Branding**: Follow color scheme and typography

### Color Palette

- **Primary Blue**: `#1e40af` (buttons, headers)
- **Secondary Blue**: `#3b82f6` (links, accents)
- **Success Green**: `#16a34a` (success messages)
- **Warning Orange**: `#f59e0b` (warnings)
- **Danger Red**: `#dc2626` (errors)
- **Light Gray**: `#f8fafc` (backgrounds)

### Component Guidelines

- Use **Bootstrap 5** components consistently
- Include **loading states** for async operations
- Provide **clear feedback** for user actions
- Implement **progressive enhancement**

## 📖 Documentation Standards

### Code Documentation

- **Docstrings** for all public functions and classes
- **Inline comments** for complex logic
- **Type hints** for function parameters and returns
- **Examples** in documentation

### User Documentation

- **Clear step-by-step** instructions
- **Screenshots** for UI features
- **Code examples** for API usage
- **Troubleshooting** sections

## 🐛 Bug Reports

When reporting bugs, please include:

### Bug Report Template

```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Environment:**
 - OS: [e.g. Windows 10, macOS 12.0, Ubuntu 20.04]
 - Python Version: [e.g. 3.9.7]
 - Browser: [e.g. Chrome 95, Firefox 94]
 - CorpMeet-AI Version: [e.g. 1.0.0]

**Additional context**
Add any other context about the problem here.
```

## 💡 Feature Requests

### Feature Request Template

```markdown
**Is your feature request related to a problem?**
A clear description of what the problem is.

**Describe the solution you'd like**
A clear description of what you want to happen.

**Describe alternatives you've considered**
Other solutions or features you've considered.

**Additional context**
Add any other context or screenshots about the feature request.

**Implementation Ideas**
If you have ideas about how to implement this feature, please share them.
```

## 🎯 Priority Areas for Contribution

### High Priority

- 🔐 **User Authentication**: Multi-user support with secure login
- 🤖 **Advanced AI Models**: Integration with multiple AI providers
- 📊 **Analytics Dashboard**: Meeting insights and trends
- 🔌 **Calendar Integration**: Sync with Google Calendar, Outlook
- 📱 **Mobile App**: React Native or Flutter implementation

### Medium Priority

- 🌍 **Internationalization**: Multi-language support
- 🔍 **Search Functionality**: Full-text search across meetings
- 📈 **Export Options**: Excel, CSV, Word document exports
- 🎨 **Themes**: Dark mode and custom branding
- 🔔 **Notifications**: Email and push notifications

### Good First Issues

- 📝 **Documentation improvements**
- 🐛 **Small bug fixes**
- 🧪 **Adding tests for existing features**
- 🎨 **UI polish and minor enhancements**
- 📱 **Mobile responsiveness improvements**

## 🏆 Recognition

### Contributors

All contributors will be recognized in:

- **README.md** contributors section
- **GitHub contributors** page
- **Release notes** for their contributions
- **Special mentions** in project updates

### Contribution Levels

- 🥉 **Bronze**: 1-5 merged PRs
- 🥈 **Silver**: 6-15 merged PRs
- 🥇 **Gold**: 16+ merged PRs
- 💎 **Diamond**: Major feature contributions
- 🌟 **Maintainer**: Ongoing project maintenance

## 📞 Getting Help

### Communication Channels

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: Questions and general discussion
- **Email**: [maintainer@corpmeet-ai.com](mailto:maintainer@corpmeet-ai.com)
- **Discord**: [Join our Discord](https://discord.gg/corpmeet-ai) (coming soon)

### Mentorship

New contributors can request mentorship by:

1. **Creating an issue** with the `mentorship` label
2. **Joining our Discord** server
3. **Attending virtual office hours** (announced in discussions)

## 📜 Code of Conduct

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone, regardless of:

- Age, body size, disability, ethnicity
- Gender identity and expression
- Level of experience, education, socio-economic status
- Nationality, personal appearance, race, religion
- Sexual identity and orientation

### Our Standards

**Positive behavior includes:**

- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

**Unacceptable behavior includes:**

- Trolling, insulting/derogatory comments, personal attacks
- Public or private harassment
- Publishing others' private information without permission
- Other conduct inappropriate for a professional setting

### Enforcement

Instances of abusive behavior may be reported to [conduct@corpmeet-ai.com](mailto:conduct@corpmeet-ai.com). All complaints will be reviewed and investigated promptly and fairly.

## 🎉 Thank You!

Thank you for contributing to CorpMeet-AI! Your efforts help make meeting management more efficient for teams worldwide. Every contribution, no matter how small, makes a difference.

---

**Happy Contributing!** 🚀

*For questions about contributing, please create an issue or reach out to the maintainers.*