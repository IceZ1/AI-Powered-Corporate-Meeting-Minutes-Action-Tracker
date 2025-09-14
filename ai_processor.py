"""
AI processing module for CorpMeet-AI application.
Contains functions to process meeting transcripts and extract structured data.
"""

import re
from datetime import datetime, timedelta
import random


def process_meeting_transcript(transcript_text):
    """
    Process meeting transcript using AI to extract structured information.

    This is a mock implementation that simulates OpenAI API processing.
    In production, this would call the actual OpenAI API.

    Args:
        transcript_text (str): Raw meeting transcript text

    Returns:
        dict: Structured meeting data containing:
            - summary: List of 3-5 key summary points
            - action_items: List of action items with task, owner, deadline
            - decisions: List of key decisions made
    """

    # Mock AI processing - in production, replace with actual OpenAI API call
    # Example OpenAI API call structure:
    """
    import openai
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant that processes meeting transcripts"
            },
            {
                "role": "user",
                "content": f"Process this meeting transcript: {transcript_text}"
            }
        ],
        temperature=0.3
    )
    """

    # For demo purposes, we'll generate structured output based on transcript content
    result = {
        "summary": generate_summary_points(transcript_text),
        "action_items": generate_action_items(transcript_text),
        "decisions": generate_decisions(transcript_text),
    }

    return result


def generate_summary_points(transcript):
    """Generate summary points based on transcript content."""

    # Look for common meeting patterns and keywords
    keywords = extract_keywords(transcript)

    summary_templates = [
        f"Discussed {keywords[0]} strategy and implementation approach",
        f"Reviewed current status of "
        f"{keywords[1] if len(keywords) > 1 else 'ongoing projects'}",
        f"Addressed key challenges related to "
        f"{keywords[2] if len(keywords) > 2 else 'project execution'}",
        "Aligned team on next steps and priorities",
        "Established timeline for upcoming deliverables",
    ]

    # Select 3-4 relevant summary points
    return summary_templates[: min(4, len(summary_templates))]


def generate_action_items(transcript):
    """Generate action items based on transcript content."""

    # Extract potential team members mentioned
    team_members = extract_team_members(transcript)

    # Generate realistic action items
    action_items = []

    # Sample action items with different deadlines
    sample_actions = [
        "Follow up on budget approval process",
        "Prepare technical specification document",
        "Schedule stakeholder review meeting",
        "Implement proposed solution framework",
        "Review and update project timeline",
    ]

    for i, action in enumerate(sample_actions[:3]):  # Limit to 3 action items
        deadline = (datetime.now() + timedelta(days=random.randint(3, 14))).strftime(
            "%Y-%m-%d"
        )
        owner = (
            team_members[i % len(team_members)]
            if team_members
            else f"Team Member {i+1}"
        )

        action_items.append({"task": action, "owner": owner, "deadline": deadline})

    return action_items


def generate_decisions(transcript):
    """Generate key decisions based on transcript content."""

    decisions_templates = [
        "Approved budget allocation for Q4 initiatives",
        "Decided to proceed with recommended technology stack",
        "Agreed on weekly progress review meetings",
        "Confirmed project timeline and key milestones",
    ]

    # Return 2-3 decisions
    return decisions_templates[: min(3, len(decisions_templates))]


def extract_keywords(text):
    """Extract relevant keywords from transcript text."""

    # Common business/project keywords
    default_keywords = [
        "project",
        "development",
        "strategy",
        "implementation",
        "review",
        "planning",
    ]

    if not text or len(text.strip()) < 50:
        return default_keywords

    # Simple keyword extraction (in production, use more sophisticated NLP)
    words = re.findall(r"\b[a-zA-Z]{4,}\b", text.lower())

    # Filter out common stop words
    stop_words = {
        "that",
        "this",
        "with",
        "from",
        "they",
        "were",
        "been",
        "have",
        "will",
        "would",
        "could",
        "should",
    }
    keywords = [word for word in words if word not in stop_words and len(word) > 3]

    # Return unique keywords, limiting to first 6
    unique_keywords = list(dict.fromkeys(keywords))[:6]

    return unique_keywords if unique_keywords else default_keywords


def extract_team_members(text):
    """Extract potential team member names from transcript."""

    # Default team members for demo
    default_members = ["Sarah Johnson", "Mike Chen", "Alex Rodriguez", "Emily Davis"]

    if not text:
        return default_members

    # Look for capitalized words that might be names (simple approach)
    potential_names = re.findall(r"\b[A-Z][a-z]+\s+[A-Z][a-z]+\b", text)

    if potential_names:
        return list(set(potential_names))[:4]  # Limit to 4 names

    return default_members


def validate_openai_api_key():
    """
    Validate OpenAI API key configuration.

    Returns:
        bool: True if API key is configured, False otherwise
    """
    import os
    from dotenv import load_dotenv

    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    return api_key is not None and len(api_key.strip()) > 0


# Example function for actual OpenAI integration (commented out for demo)
"""
def process_with_openai(transcript_text):
    '''
    Process transcript using actual OpenAI API.
    Uncomment and configure when ready to use real AI processing.
    '''
    
    import openai
    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    openai.api_key = os.getenv('OPENAI_API_KEY')
    
    system_prompt = '''
    You are an AI assistant specialized in processing corporate meeting transcripts.
    Extract and structure the following information from meeting transcripts:
    
    1. Summary: 3-5 key bullet points summarizing the main topics discussed
    2. Action Items: List of specific tasks with assigned owners and deadlines
    3. Decisions: Key decisions or conclusions reached during the meeting
    
    Return the response in JSON format with keys: summary, action_items, decisions
    Action items should have: task, owner, deadline (YYYY-MM-DD format)
    '''
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": f"Process this meeting transcript:\n\n{transcript_text}"
                }
            ],
            temperature=0.3,
            max_tokens=1000
        )
        
        import json
        result = json.loads(response.choices[0].message.content)
        return result
        
    except Exception as e:
        print(f"OpenAI API error: {e}")
        # Fallback to mock processing
        return process_meeting_transcript(transcript_text)
"""
