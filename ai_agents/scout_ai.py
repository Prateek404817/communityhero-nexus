def analyze_issue(image_path, category):

    category = category.lower().strip()

    if category == "road damage":
        return {
            "issue_type": "Road Damage",
            "severity": "High",
            "confidence": 96,
            "description": "Large pothole or damaged road detected.",
            "multiple_issues": ["Road Damage"]
        }

    elif category == "garbage":
        return {
            "issue_type": "Garbage",
            "severity": "Medium",
            "confidence": 94,
            "description": "Garbage accumulation detected.",
            "multiple_issues": ["Garbage"]
        }

    elif category == "street light":
        return {
            "issue_type": "Street Light",
            "severity": "Low",
            "confidence": 93,
            "description": "Street light failure detected.",
            "multiple_issues": ["Street Light"]
        }

    elif category == "water leakage":
        return {
            "issue_type": "Water Leakage",
            "severity": "High",
            "confidence": 95,
            "description": "Water leakage detected.",
            "multiple_issues": ["Water Leakage"]
        }

    elif category == "drainage":
        return {
            "issue_type": "Drainage",
            "severity": "Medium",
            "confidence": 92,
            "description": "Drainage blockage detected.",
            "multiple_issues": ["Drainage"]
        }

    elif category == "electricity":
        return {
            "issue_type": "Electricity",
            "severity": "High",
            "confidence": 95,
            "description": "Electrical infrastructure issue detected.",
            "multiple_issues": ["Electricity"]
        }

    elif category == "tree hazard":
        return {
            "issue_type": "Tree Hazard",
            "severity": "Medium",
            "confidence": 94,
            "description": "Tree hazard detected.",
            "multiple_issues": ["Tree Hazard"]
        }

    else:
        return {
            "issue_type": "Other",
            "severity": "Medium",
            "confidence": 90,
            "description": "General civic issue detected.",
            "multiple_issues": []
        }