from database.models import Issue


def calculate_health_score():

    issues = Issue.query.all()

    if len(issues) == 0:
        return 100

    resolved = len([i for i in issues if i.status == "Resolved"])

    score = int((resolved / len(issues)) * 100)

    return score