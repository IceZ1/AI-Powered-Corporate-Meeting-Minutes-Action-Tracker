"""
Database models for CorpMeet-AI application.
Defines the Meeting model for storing meeting minutes and related data.
"""

import json
from datetime import datetime
from typing import Any, Dict, List, Optional

from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy database instance with explicit type annotation
db: SQLAlchemy = SQLAlchemy()


class Meeting(db.Model):
    """
    Meeting model to store meeting minutes, action items, and decisions.

    Attributes:
        id: Primary key for the meeting record
        title: Meeting title/subject
        date_created: Timestamp when the meeting was processed
        summary: Meeting summary in JSON format (list of bullet points)
        action_items: Action items in JSON format (list of tasks with
                     owner and deadline)
        decisions: Key decisions in JSON format (list of decision points)
        original_transcript: Original meeting transcript text
    """

    # Primary key
    id = db.Column(db.Integer, primary_key=True)

    # Meeting basic information
    title = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # Meeting content (stored as JSON strings for flexibility)
    summary = db.Column(db.Text, nullable=True)  # JSON string of summary points
    action_items = db.Column(db.Text, nullable=True)  # JSON string of action items
    decisions = db.Column(db.Text, nullable=True)  # JSON string of decisions

    # Original transcript for reference
    original_transcript = db.Column(db.Text, nullable=False)

    def __init__(
        self,
        title: str,
        summary: List[str],
        action_items: List[Dict[str, Any]],
        decisions: List[str],
        original_transcript: str,
    ) -> None:
        """
        Initialize a new Meeting record.

        Args:
            title: Meeting title
            summary: List of summary points
            action_items: List of action item dictionaries
            decisions: List of decision points
            original_transcript: Original meeting transcript text
        """
        self.title = title
        self.summary = json.dumps(summary) if isinstance(summary, list) else summary
        self.action_items = (
            json.dumps(action_items) if isinstance(action_items, list) else action_items
        )
        self.decisions = (
            json.dumps(decisions) if isinstance(decisions, list) else decisions
        )
        self.original_transcript = original_transcript

    def get_summary(self) -> List[str]:
        """Get summary as a Python list."""
        try:
            return json.loads(self.summary) if self.summary else []
        except json.JSONDecodeError:
            return []

    def get_action_items(self) -> List[Dict[str, Any]]:
        """Get action items as a Python list."""
        try:
            return json.loads(self.action_items) if self.action_items else []
        except json.JSONDecodeError:
            return []

    def get_decisions(self) -> List[str]:
        """Get decisions as a Python list."""
        try:
            return json.loads(self.decisions) if self.decisions else []
        except json.JSONDecodeError:
            return []

    def __repr__(self) -> str:
        """String representation of the Meeting object."""
        return (
            f'<Meeting {self.title} - {self.date_created.strftime("%Y-%m-%d %H:%M")}>'
        )
