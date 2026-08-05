"""
Section 1: Regular Expressions – Resume Information Extraction
=============================================================
A Python-based resume information extraction system that extracts candidate
information from resume text using Regular Expressions.
"""

import re
from dataclasses import dataclass, field


@dataclass
class CandidateProfile:
    """Data class to store extracted candidate information."""

    name: str = ""
    emails: list[str] = field(default_factory=list)
    mobile_numbers: list[str] = field(default_factory=list)
    technical_skills: list[str] = field(default_factory=list)
    years_of_experience: int | None = None
    is_eligible: bool = False


class ResumeExtractor:
    """
    Extracts candidate information from resume text using Regular Expressions.

    Features:
    - Extract candidate's name
    - Identify email addresses
    - Extract mobile numbers
    - Detect technical skills (Python, Java, SQL, Machine Learning, NLP)
    - Extract years of experience
    - Generate structured summary
    - Filter candidates by eligibility criteria
    """

    # Predefined technical skills to detect
    TECHNICAL_SKILLS = [
        "Python",
        "Java",
        "SQL",
        "Machine Learning",
        "NLP",
        "machine learning",
        "natural language processing",
    ]

    # Regex patterns
    EMAIL_PATTERN = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

    MOBILE_PATTERN = re.compile(
        r"(?:\+?(\d{1,3})[-.\s]?)?"  # Country code
        r"(?:\(?\d{2,4}\)?[-.\s]?)?"  # Area code
        r"\d{3,4}[-.\s]?\d{3,4}"  # Main number
    )

    EXPERIENCE_PATTERNS = [
        re.compile(r"(\d+)\s*(?:\+\s*)?(?:years?|yrs?)\s*(?:of\s+)?(?:experience|exp)", re.IGNORECASE),
        re.compile(r"(?:experience|exp)[:\s]*(\d+)\s*(?:\+\s*)?(?:years?|yrs?)", re.IGNORECASE),
        re.compile(
            r"(\d+)\s*(?:\+\s*)?(?:years?|yrs?)\s*(?:in|of)\s*(?:relevant\s+)?(?:experience|work)",
            re.IGNORECASE,
        ),
        re.compile(r"(?:total\s+)?experience[:\s]*(\d+)\s*(?:years?|yrs?)", re.IGNORECASE),
    ]

    NAME_PATTERNS = [
        # Try label-based pattern first (more specific)
        re.compile(r"(?:name|candidate)[:\s]+([A-Z][a-z]+(?: +[A-Z][a-z]+){1,3})", re.IGNORECASE),
        # Fallback: name on the first line of the resume (not any line — avoids section headers)
        re.compile(r"\A\s*([A-Z][a-z]+(?: +[A-Z][a-z]+){1,3})"),
        # Match after honorifics
        re.compile(r"(?:Mr|Ms|Mrs|Dr|Prof)\.?\s+([A-Z][a-z]+(?: +[A-Z][a-z]+){1,3})", re.IGNORECASE),
    ]

    def __init__(self):
        self.candidates: list[CandidateProfile] = []

    def extract_name(self, text: str) -> str:
        """Extract candidate's name from resume text."""
        for pattern in self.NAME_PATTERNS:
            match = pattern.search(text)
            if match:
                name = match.group(1) if match.lastindex else match.group(0)
                # Clean up the name
                name = name.strip()
                if len(name.split()) >= 2:  # Ensure first and last name
                    return name
        return "Not Found"

    def extract_emails(self, text: str) -> list[str]:
        """Extract all email addresses from text."""
        return list(set(self.EMAIL_PATTERN.findall(text)))

    def extract_mobile_numbers(self, text: str) -> list[str]:
        """Extract mobile/contact numbers from text."""
        # Clean and validate numbers (must have at least 7 digits)
        valid_numbers = []
        for match in self.MOBILE_PATTERN.finditer(text):
            number = re.sub(r"[^\d]", "", match.group())
            if len(number) >= 7 and len(number) <= 15:
                valid_numbers.append(match.group().strip())
        return list(set(valid_numbers))

    def extract_skills(self, text: str) -> list[str]:
        """Extract technical skills from resume text."""
        found_skills = []
        for skill in self.TECHNICAL_SKILLS:
            # Use word boundary to match exact skills
            pattern = re.compile(r"\b" + re.escape(skill) + r"\b", re.IGNORECASE)
            if pattern.search(text):
                # Add the canonical form (title case for mixed-case, uppercase for acronyms)
                canonical = skill if skill.isupper() else skill.title()
                if canonical not in found_skills:
                    found_skills.append(canonical)
        return found_skills

    def extract_experience(self, text: str) -> int | None:
        """Extract years of experience from text."""
        for pattern in self.EXPERIENCE_PATTERNS:
            match = pattern.search(text)
            if match:
                try:
                    return int(match.group(1))
                except (ValueError, IndexError):
                    continue
        return None

    def check_eligibility(
        self, profile: CandidateProfile, min_experience: int = 2, required_skill: str = "Python"
    ) -> bool:
        """
        Check if candidate meets minimum eligibility criteria.

        Criteria:
        - Minimum 2 years of experience
        - Python skill required
        """
        has_experience = profile.years_of_experience is not None and profile.years_of_experience >= min_experience
        has_skill = required_skill in profile.technical_skills
        return has_experience and has_skill

    def extract_candidate_info(self, resume_text: str) -> CandidateProfile:
        """Extract all candidate information from resume text."""
        profile = CandidateProfile()

        profile.name = self.extract_name(resume_text)
        profile.emails = self.extract_emails(resume_text)
        profile.mobile_numbers = self.extract_mobile_numbers(resume_text)
        profile.technical_skills = self.extract_skills(resume_text)
        profile.years_of_experience = self.extract_experience(resume_text)
        profile.is_eligible = self.check_eligibility(profile)

        return profile

    def generate_summary(self, profile: CandidateProfile) -> str:
        """Generate a structured summary of the candidate's profile."""
        separator = "=" * 50

        summary = f"""
{separator}
        CANDIDATE PROFILE SUMMARY
{separator}
Name:               {profile.name}
Email(s):           {", ".join(profile.emails) if profile.emails else "Not Found"}
Mobile Number(s):   {", ".join(profile.mobile_numbers) if profile.mobile_numbers else "Not Found"}
Technical Skills:   {", ".join(profile.technical_skills) if profile.technical_skills else "None Detected"}
Experience:         {f"{profile.years_of_experience} years" if profile.years_of_experience else "Not Specified"}
Eligibility:        {"✓ ELIGIBLE" if profile.is_eligible else "✗ NOT ELIGIBLE"}
{separator}
"""
        return summary

    def display_eligible_candidates(
        self,
        candidates: list[CandidateProfile],
        min_experience: int = 2,
        required_skill: str = "Python",
    ) -> str:
        """Display candidates who satisfy minimum eligibility criteria."""
        eligible = [c for c in candidates if c.is_eligible]

        result = f"""
{"=" * 60}
        ELIGIBILITY FILTER RESULTS
        (Minimum {min_experience} years experience + {required_skill} skill)
{"=" * 60}
Total Candidates:     {len(candidates)}
Eligible Candidates:  {len(eligible)}
Not Eligible:         {len(candidates) - len(eligible)}
{"=" * 60}
"""
        if eligible:
            result += "\n✓ ELIGIBLE CANDIDATES:\n"
            result += "-" * 40 + "\n"
            for i, candidate in enumerate(eligible, 1):
                result += f"  {i}. {candidate.name}\n"
                result += f"     Experience: {candidate.years_of_experience} years\n"
                result += f"     Skills: {', '.join(candidate.technical_skills)}\n\n"
        else:
            result += "\n✗ No candidates meet the eligibility criteria.\n"

        return result


# Sample resumes for testing
SAMPLE_RESUMES = [
    """
    John Smith
    Email: john.smith@email.com
    Phone: +1-555-123-4567

    PROFESSIONAL SUMMARY
    Experienced software developer with 5 years of experience in Python and Java development.
    Skills: Python, Java, SQL, Machine Learning

    EXPERIENCE
    Senior Developer at Tech Corp (2019-2024) - 5 years experience
    """,
    """
    Name: Jane Doe
    Contact: jane.doe@company.org, jane_d@work.net
    Mobile: 9876543210

    PROFESSIONAL BACKGROUND
    Data Scientist with 3 years of experience in NLP and Machine Learning.

    TECHNICAL SKILLS
    Python, SQL, Machine Learning, NLP

    Total experience: 3 years
    """,
    """
    Robert Johnson
    Email: robert.j@techmail.com
    Phone: 44-20-1234-5678

    Junior Developer
    1 year experience in Java development

    Skills: Java, SQL
    """,
    """
    Dr. Emily Chen
    Contact: emily.chen@university.edu

    RESEARCH PROFILE
    7 years of experience in Machine Learning and NLP research

    Expertise: Python, Machine Learning, NLP, Java
    """,
]


def main():
    """Main function to demonstrate the Resume Extraction System."""
    extractor = ResumeExtractor()

    print("\n" + "=" * 70)
    print("     RESUME INFORMATION EXTRACTION SYSTEM")
    print("     Using Regular Expressions")
    print("=" * 70)

    # Process each resume
    all_candidates = []

    for i, resume in enumerate(SAMPLE_RESUMES, 1):
        print(f"\n{'─' * 70}")
        print(f"Processing Resume #{i}")
        print(f"{'─' * 70}")

        profile = extractor.extract_candidate_info(resume)
        all_candidates.append(profile)

        # Print individual profile summary
        print(extractor.generate_summary(profile))

    # Display eligibility results
    print(extractor.display_eligible_candidates(all_candidates))

    return all_candidates


if __name__ == "__main__":
    main()
