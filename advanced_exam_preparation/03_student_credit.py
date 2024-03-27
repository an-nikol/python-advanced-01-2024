def students_credits(*args):
    total_credits = 0
    course_credits = {}

    for course_data in args:
        course_data = course_data.split("-")
        percent_test_taken = int(course_data[3]) / int(course_data[2])
        current_credit = int(course_data[1]) * percent_test_taken
        total_credits += current_credit

        if course_data[0] not in course_credits:
            course_credits[course_data[0]] = current_credit

    result = ""

    if total_credits >= 240:
        result += f"Diyan gets a diploma with {total_credits:.1f} credits.\n"
    else:
        result += f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.\n"

    course_credits = dict(sorted(course_credits.items(), key=lambda x: -x[1]))

    for name, credits in course_credits.items():
        result += f"{name} - {credits:.1f}\n"

    return result


print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)

