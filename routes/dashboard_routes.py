from flask import Blueprint,render_template

from services.dashboard_service import get_dashboard_stats

bp=Blueprint("dashboard",__name__)


@bp.route("/dashboard")
def dashboard():

    stats=get_dashboard_stats()

    return render_template(
        "dashboards/impact-dashboard.html",
        stats=stats
    )