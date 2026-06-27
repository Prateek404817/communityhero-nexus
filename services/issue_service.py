import os

from werkzeug.utils import secure_filename

from database.database import db
from database.models import Issue

from utils.tracking_id import generate_tracking_id

from ai_agents.scout_ai import analyze_issue
from ai_agents.risk_ai import analyze_risk
from ai_agents.authority_ai import assign_authority
from ai_agents.resolution_ai import generate_resolution


def save_issue(
    image,
    title,
    description,
    category,
    address,
    latitude,
    longitude,
    contact,
    anonymous
):

    filename = secure_filename(image.filename)

    image_path = "uploads/issues/" + filename
    image_path = image_path.replace("\\", "/")

    image.save(image_path)

    # --------------------------
    # Mock AI Pipeline
    # --------------------------

    scout = analyze_issue(image_path, category)

    risk = analyze_risk(scout["issue_type"])

    authority = assign_authority(scout["issue_type"])
    print("CATEGORY:", category)
    print("SCOUT:", scout)
    print("AUTHORITY:", authority)

    resolution = generate_resolution(scout["issue_type"])

    # --------------------------
    # Database
    # --------------------------

    issue = Issue(

        tracking_id=generate_tracking_id(),

        title=title,

        description=description,

        category=category,

        image_path=image_path,

        address=address,

        latitude=float(latitude),

        longitude=float(longitude),

        contact=contact,

        anonymous=anonymous,

        issue_type=scout["issue_type"],

        severity=scout["severity"],

        confidence=scout["confidence"],

        ai_summary=scout["description"],

        risk_level=risk["risk_level"],

        risk_score=risk["risk_score"],

        authority=authority["authority"],

        department=authority["department"],

        priority=authority["priority"],

        estimated_time=resolution["estimated_time"],

        resources=resolution["resources"],

        status="Reported"

    )

    db.session.add(issue)

    db.session.commit()

    return {

        "issue": issue,

        "scout": scout,

        "risk": risk,

        "authority": authority,

        "resolution": resolution

    }