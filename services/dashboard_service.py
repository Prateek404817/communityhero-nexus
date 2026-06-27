from database.models import Issue

from services.health_score_service import calculate_health_score
from services.leaderboard_service import leaderboard
from services.heatmap_service import get_heatmap_points


def get_dashboard_stats():

    issues = Issue.query.all()

    total = len(issues)

    resolved = len([i for i in issues if i.status == "Resolved"])

    pending = total - resolved

    high = len([i for i in issues if i.severity == "High"])

    return {

        "total": total,

        "resolved": resolved,

        "pending": pending,

        "high": high,

        "health": calculate_health_score(),

        "leaderboard": leaderboard(),

        "heatmap": get_heatmap_points(),

        "issues": issues

    }