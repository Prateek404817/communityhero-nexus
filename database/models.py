from database.database import db
from datetime import datetime


class Issue(db.Model):

    __tablename__ = "issues"

    id = db.Column(db.Integer, primary_key=True)

    # -------------------------
    # Tracking
    # -------------------------

    tracking_id = db.Column(db.String(50), unique=True, nullable=False)

    # -------------------------
    # Citizen Report
    # -------------------------

    title = db.Column(db.String(200))

    description = db.Column(db.Text)

    category = db.Column(db.String(100))

    image_path = db.Column(db.String(300))

    address = db.Column(db.String(300))

    latitude = db.Column(db.Float)

    longitude = db.Column(db.Float)

    anonymous = db.Column(db.Boolean, default=False)

    contact = db.Column(db.String(20))

    # -------------------------
    # Scout AI
    # -------------------------

    issue_type = db.Column(db.String(100))

    severity = db.Column(db.String(50))

    confidence = db.Column(db.Float)

    ai_summary = db.Column(db.Text)

    # -------------------------
    # Risk AI
    # -------------------------

    risk_level = db.Column(db.String(50))

    risk_score = db.Column(db.Integer)

    # -------------------------
    # Authority AI
    # -------------------------

    authority = db.Column(db.String(150))

    department = db.Column(db.String(150))

    priority = db.Column(db.String(50))

    # -------------------------
    # Resolution AI
    # -------------------------

    estimated_time = db.Column(db.String(100))

    resources = db.Column(db.String(300))

    # -------------------------
    # Workflow
    # -------------------------

    status = db.Column(db.String(50), default="Reported")

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )