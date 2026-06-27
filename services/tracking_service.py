from database.models import Issue


def get_issue_by_tracking_id(tracking_id):
    return Issue.query.filter_by(tracking_id=tracking_id).first()


def get_all_issues():
    return Issue.query.order_by(Issue.created_at.desc()).all()


def get_pending_issues():
    return Issue.query.filter_by(status="Reported").all()


def update_issue_status(issue_id, status):

    issue = Issue.query.get(issue_id)

    if issue:

        issue.status = status

        from database.database import db

        db.session.commit()

    return issue