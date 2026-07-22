import re

 
resumes = [
    """
    Name: Rahul Kumar
    Email: rahul@gmail.com
    Mobile: 9876543210
    Skills: Python, Java, SQL, Machine Learning
    Experience: 3 years
    """,

    """
    Name: Priya Sharma
    Email: priya@gmail.com
    Mobile: 9123456780
    Skills: Java, SQL, NLP
    Experience: 1 year
    """,

    """
    Name: Arjun Reddy
    Email: arjun@gmail.com
    Mobile: 8765432109
    Skills: Python, NLP, Machine Learning
    Experience: 4 years
    """
]

 
technical_skills = [
    "Python",
    "Java",
    "SQL",
    "Machine Learning",
    "NLP"
]


 
def extract_information(resume):

    # Extract candidate name
    name_pattern = r"Name:\s*([A-Za-z ]+)"
    name_match = re.search(name_pattern, resume)

    if name_match:
        name = name_match.group(1).strip()
    else:
        name = "Not found"

     
    email_pattern = r"[\w.-]+@[\w.-]+\.\w+"
    email_match = re.search(email_pattern, resume)

    if email_match:
        email = email_match.group()
    else:
        email = "Not found"

     
    mobile_pattern = r"\b[6-9]\d{9}\b"
    mobile_match = re.search(mobile_pattern, resume)

    if mobile_match:
        mobile = mobile_match.group()
    else:
        mobile = "Not found"

     
    detected_skills = []

    for skill in technical_skills:

        if re.search(
            re.escape(skill),
            resume,
            re.IGNORECASE
        ):
            detected_skills.append(skill)

     
    experience_pattern = r"(\d+)\s*(?:year|years)"
    experience_match = re.search(
        experience_pattern,
        resume,
        re.IGNORECASE
    )

    if experience_match:
        experience = int(experience_match.group(1))
    else:
        experience = 0

     
    return {
        "Name": name,
        "Email": email,
        "Mobile": mobile,
        "Skills": detected_skills,
        "Experience": experience
    }


 
for resume in resumes:

    candidate = extract_information(resume)

    print("\n---------- CANDIDATE PROFILE ----------")

    print("Name       :", candidate["Name"])
    print("Email      :", candidate["Email"])
    print("Mobile     :", candidate["Mobile"])

    print(
        "Skills     :",
        ", ".join(candidate["Skills"])
    )

    print(
        "Experience :",
        candidate["Experience"],
        "years"
    )

    
    if (
        candidate["Experience"] >= 2
        and
        "Python" in candidate["Skills"]
    ):

        print("Eligibility: ELIGIBLE")

    else:

        print("Eligibility: NOT ELIGIBLE")