import re


 
register_number = input(
    "Enter register number: "
)

email = input(
    "Enter institutional email: "
)

course_code = input(
    "Enter course code: "
)

semester = input(
    "Enter semester: "
)

mobile_number = input(
    "Enter mobile number: "
)


 
register_pattern = r"^\d{9}$"

email_pattern = (
    r"^[A-Za-z0-9._]+"
    r"@saveetha\.com$"
)

course_pattern = r"^[A-Z]{3}\d{4}$"

semester_pattern = r"^[1-8]$"

mobile_pattern = r"^[6-9]\d{9}$"


 
register_valid = bool(
    re.fullmatch(
        register_pattern,
        register_number
    )
)

if register_valid:

    print(
        "Register Number: Valid"
    )

else:

    print(
        "Register Number: Invalid"
    )


 
email_valid = bool(
    re.fullmatch(
        email_pattern,
        email
    )
)

if email_valid:

    print(
        "Institutional Email: Valid"
    )

else:

    print(
        "Institutional Email: Invalid"
    )


 
course_valid = bool(
    re.fullmatch(
        course_pattern,
        course_code
    )
)

if course_valid:

    print(
        "Course Code: Valid"
    )

else:

    print(
        "Course Code: Invalid"
    )


 
semester_valid = bool(
    re.fullmatch(
        semester_pattern,
        semester
    )
)

if semester_valid:

    print(
        "Semester: Valid"
    )

else:

    print(
        "Semester: Invalid"
    )


 
mobile_valid = bool(
    re.fullmatch(
        mobile_pattern,
        mobile_number
    )
)

if mobile_valid:

    print(
        "Mobile Number: Valid"
    )

else:

    print(
        "Mobile Number: Invalid"
    )


 
if (
    register_valid
    and email_valid
    and course_valid
    and semester_valid
    and mobile_valid
):

    print(
        "\nREGISTRATION SUCCESSFUL"
    )

else:

    print(
        "\nREGISTRATION FAILED"
    )