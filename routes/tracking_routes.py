from flask import Blueprint, render_template, request

from services.tracking_service import get_issue_by_tracking_id

bp = Blueprint("tracking", __name__)


@bp.route("/tracking", methods=["GET", "POST"])
def tracking():

    issue = None
    searched = False

    if request.method == "POST":

        searched = True

        tracking_id = request.form["tracking_id"].strip()

        issue = get_issue_by_tracking_id(tracking_id)

    return render_template(
        "citizen/tracking.html",
        issue=issue,
        searched=searched
    )