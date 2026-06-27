from database.models import Issue


def leaderboard():

    issues = Issue.query.all()

    ranking = {}

    for issue in issues:

        dept = issue.authority

        ranking.setdefault(dept, 0)

        if issue.status == "Resolved":
            ranking[dept] += 1

    return sorted(
        ranking.items(),
        key=lambda x: x[1],
        reverse=True
    )