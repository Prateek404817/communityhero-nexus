def assign_authority(issue_type):

    mapping = {

        "Road Damage": (
            "Municipal Corporation",
            "Road Maintenance Department",
            "High"
        ),

        "Garbage": (
            "Sanitation Department",
            "Solid Waste Management",
            "Medium"
        ),

        "Street Light": (
            "Electricity Board",
            "Electrical Maintenance",
            "Low"
        ),

        "Water Leakage": (
            "Water Works Department",
            "Water Supply Department",
            "High"
        ),

        "Drainage": (
            "Municipal Corporation",
            "Drainage Department",
            "Medium"
        ),

        "Electricity": (
            "Electricity Board",
            "Electrical Maintenance",
            "High"
        ),

        "Tree Hazard": (
            "Parks Department",
            "Tree Maintenance Department",
            "Medium"
        ),

        "Other": (
            "Municipal Corporation",
            "General Administration",
            "Medium"
        )

    }

    authority, department, priority = mapping.get(
        issue_type,
        (
            "Municipal Corporation",
            "General Administration",
            "Medium"
        )
    )

    return {
        "authority": authority,
        "department": department,
        "priority": priority
    }