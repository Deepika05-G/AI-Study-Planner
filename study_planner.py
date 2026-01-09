# AI-Based Personalized Study Planner (Basic Version)

def create_study_plan(subjects, hours):
    plan = {}
    hours_per_subject = hours // len(subjects)

    for subject in subjects:
        plan[subject] = f"{hours_per_subject} hours per day"

    return plan


# Example usage
subjects = ["Maths", "Python", "DSA"]
total_hours = 6

study_plan = create_study_plan(subjects, total_hours)

for subject, time in study_plan.items():
    print(subject, ":", time)
