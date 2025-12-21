import pandas as pd

def matches_branch(course_name, selected_branches):
    if pd.isna(course_name):
        return False

    course_name = course_name.lower().replace("&", "and").replace("-", " ").replace("\n", " ").strip()
    course_words = set(course_name.split()) - {"engineering", "engg"}

    for branch in selected_branches:
        if branch.lower() == "any branch":
            return True

        branch_clean = branch.lower().replace("&", "and").replace("-", " ").replace("\n", " ").strip()
        branch_words = set(branch_clean.split()) - {"engineering", "engg"}

        if branch_words & course_words:
            return True

    return False
