from flask import Blueprint, render_template, request, redirect

from services.authority_service import (
    get_all_issues,
    update_status
)

bp = Blueprint("authority", __name__)


@bp.route("/authority")
def authority_dashboard():

    issues = get_all_issues()

    return render_template(
        "authority/authority-dashboard.html",
        issues=issues
    )


@bp.route("/authority/update/<int:issue_id>", methods=["POST"])
def authority_update(issue_id):

    status = request.form["status"]

    update_status(issue_id, status)

    return redirect("/authority")