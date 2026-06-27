from database.models import Issue
from database.database import db


def get_all_issues():
    return Issue.query.order_by(Issue.created_at.desc()).all()


def get_issue(issue_id):
    return db.session.get(Issue, issue_id)


def update_status(issue_id, status):

    issue = db.session.get(Issue, issue_id)

    if issue is not None:
        issue.status = status
        db.session.commit()

    return issue