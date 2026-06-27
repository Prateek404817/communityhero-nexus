from database.models import Issue


def get_heatmap_points():

    issues = Issue.query.all()

    points = []

    for issue in issues:

        points.append({

            "lat": issue.latitude,

            "lng": issue.longitude,

            "severity": issue.severity

        })

    return points