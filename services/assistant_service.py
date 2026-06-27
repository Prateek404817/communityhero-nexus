from database.models import Issue


def ask_assistant(message):

    msg = message.lower()

    if "road" in msg or "pothole" in msg:
        return "Road related issues are handled by the Road Maintenance Department."

    if "garbage" in msg:
        return "Garbage complaints are assigned to the Sanitation Department."

    if "water" in msg:
        return "Water leakage issues are handled by the Water Supply Department."

    if "tracking" in msg:
        return "Open the Tracking page and enter your Tracking ID."

    if "resolved" in msg:

        count = Issue.query.filter_by(status="Resolved").count()

        return f"There are currently {count} resolved issues."

    if "pending" in msg:

        count = Issue.query.filter_by(status="Reported").count()

        return f"There are currently {count} pending issues."

    return (
        "I can help you with:\n"
        "- Tracking reports\n"
        "- Reporting issues\n"
        "- Departments\n"
        "- Dashboard information"
    )