from datetime import datetime
from database.models import Issue


def generate_tracking_id():

    count = Issue.query.count() + 1

    year = datetime.now().year

    return f"CHN-{year}-{count:04d}"