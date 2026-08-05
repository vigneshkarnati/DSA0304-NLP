"""
Section 3: Regular Expressions – University Registration System
==============================================================
A Python-based validation system that verifies student information
before course enrollment using Regular Expressions.
"""

import re
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ValidationResult:
    """Data class to store validation result for a field."""

    field_name: str
    value: str
    is_valid: bool
    message: str


@dataclass
class StudentRegistration:
    """Data class to store student registration information."""

    register_number: str = ""
    email: str = ""
    course_code: str = ""
    semester: str = ""
    mobile_number: str = ""
    validation_results: list[ValidationResult] = field(default_factory=list)
    is_registration_successful: bool = False


class UniversityRegistrationSystem:
    """
    University registration validation system using Regular Expressions.

    Features:
    - Validate student register number
    - Validate institutional email address
    - Validate course code
    - Validate semester information
    - Validate student's mobile number
    - Display appropriate validation messages
    - Generate final registration status report
    """

    # Validation Patterns
    # Register Number: Format like "REG2024001", "STU2024-001", "2024CS001"
    REGISTER_NUMBER_PATTERN = re.compile(r"^(?:REG|STU|STD)?\d{4}(?:[A-Z]{2})?(?:[-_]?\d{3,5})$", re.IGNORECASE)

    # Institutional Email: Must end with university domain
    EMAIL_PATTERN = re.compile(
        r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(?:edu|ac\.in|edu\.in|ac\.uk|edu\.au)$", re.IGNORECASE
    )

    # Course Code: Format like "CS101", "MATH201", "PHY-101", "CS 101"
    COURSE_CODE_PATTERN = re.compile(r"^[A-Z]{2,4}[-\s]?\d{3}(?:[A-Z]?)$", re.IGNORECASE)

    # Semester: "1st Semester", "Sem 1", "Semester I", "Fall 2024", "Spring 2024"
    SEMESTER_PATTERN = re.compile(
        r"^(?:"
        r"(?:1st|2nd|3rd|[4-8]th)\s*semester"
        r"|sem(?:ester)?\s*[1-8]"
        r"|(?:fall|spring|summer|winter)\s*\d{4}"
        r"|[I-VIII]{1,4}"
        r")$",
        re.IGNORECASE,
    )

    # Mobile Number: International format
    MOBILE_PATTERN = re.compile(
        r"^(?:\+?(\d{1,3})[-.\s]?)?"
        r"(?:\d{2,5}[-.\s]?)?"
        r"\d{3,5}[-.\s]?\d{3,5}$"
    )

    def __init__(self):
        self.validated_students: list[StudentRegistration] = []

    def validate_register_number(self, register_number: str) -> ValidationResult:
        """
        Validate student register number.

        Valid formats:
        - REG2024001
        - STU2024-001
        - 2024CS001
        """
        is_valid = bool(self.REGISTER_NUMBER_PATTERN.match(register_number))

        if is_valid:
            message = f"✓ Register number '{register_number}' is valid"
        else:
            message = (
                f"✗ Invalid register number '{register_number}'. Expected format: REG2024001, STU2024-001, or 2024CS001"
            )

        return ValidationResult(field_name="Register Number", value=register_number, is_valid=is_valid, message=message)

    def validate_email(self, email: str) -> ValidationResult:
        """
        Validate institutional email address.

        Must end with:
        - .edu
        - .ac.in
        - .edu.in
        - .ac.uk
        - .edu.au
        """
        is_valid = bool(self.EMAIL_PATTERN.match(email))

        if is_valid:
            message = f"✓ Email '{email}' is a valid institutional email"
        else:
            message = f"✗ Invalid institutional email '{email}'. Must end with .edu, .ac.in, .edu.in, etc."

        return ValidationResult(field_name="Email Address", value=email, is_valid=is_valid, message=message)

    def validate_course_code(self, course_code: str) -> ValidationResult:
        """
        Validate course code.

        Valid formats:
        - CS101
        - MATH201
        - PHY-101
        - CS 101
        """
        is_valid = bool(self.COURSE_CODE_PATTERN.match(course_code))

        if is_valid:
            message = f"✓ Course code '{course_code}' is valid"
        else:
            message = f"✗ Invalid course code '{course_code}'. Expected format: CS101, MATH-201, PHY 301"

        return ValidationResult(field_name="Course Code", value=course_code, is_valid=is_valid, message=message)

    def validate_semester(self, semester: str) -> ValidationResult:
        """
        Validate semester information.

        Valid formats:
        - 1st Semester, 2nd Semester, etc.
        - Sem 1, Sem 2, etc.
        - Fall 2024, Spring 2024
        - I, II, III, IV
        """
        is_valid = bool(self.SEMESTER_PATTERN.match(semester))

        if is_valid:
            message = f"✓ Semester '{semester}' is valid"
        else:
            message = f"✗ Invalid semester '{semester}'. Expected: 1st Semester, Sem 1, Fall 2024, etc."

        return ValidationResult(field_name="Semester", value=semester, is_valid=is_valid, message=message)

    def validate_mobile_number(self, mobile_number: str) -> ValidationResult:
        """
        Validate student's mobile number.

        Accepts international formats:
        - +1-555-123-4567
        - 9876543210
        - +91-98765-43210
        """
        # First check pattern
        pattern_match = bool(self.MOBILE_PATTERN.match(mobile_number))

        # Also count digits to ensure valid length
        digits_only = re.sub(r"[^\d]", "", mobile_number)
        valid_length = 7 <= len(digits_only) <= 15

        is_valid = pattern_match and valid_length

        if is_valid:
            message = f"✓ Mobile number '{mobile_number}' is valid"
        else:
            message = f"✗ Invalid mobile number '{mobile_number}'. Expected format: +1-555-123-4567 or 9876543210"

        return ValidationResult(field_name="Mobile Number", value=mobile_number, is_valid=is_valid, message=message)

    def validate_student(
        self, register_number: str, email: str, course_code: str, semester: str, mobile_number: str
    ) -> StudentRegistration:
        """
        Validate all student information and return registration object.
        """
        registration = StudentRegistration(
            register_number=register_number,
            email=email,
            course_code=course_code,
            semester=semester,
            mobile_number=mobile_number,
        )

        # Perform all validations
        registration.validation_results = [
            self.validate_register_number(register_number),
            self.validate_email(email),
            self.validate_course_code(course_code),
            self.validate_semester(semester),
            self.validate_mobile_number(mobile_number),
        ]

        # Registration is successful only if ALL validations pass
        registration.is_registration_successful = all(result.is_valid for result in registration.validation_results)

        self.validated_students.append(registration)
        return registration

    def display_validation_results(self, registration: StudentRegistration) -> str:
        """Display validation messages for each field."""
        separator = "=" * 60

        output = f"""
{separator}
        STUDENT VALIDATION RESULTS
{separator}
Student: {registration.register_number}
{separator}
"""
        for result in registration.validation_results:
            status = "✓ PASS" if result.is_valid else "✗ FAIL"
            output += f"\n  [{status}] {result.field_name}"
            output += f"\n      Value: {result.value}"
            output += f"\n      {result.message}\n"

        return output

    def generate_registration_report(self, registration: StudentRegistration) -> str:
        """Generate final registration status report."""
        separator = "=" * 60

        if registration.is_registration_successful:
            status = "✓ REGISTRATION SUCCESSFUL"
        else:
            status = "✗ REGISTRATION FAILED"

        passed = sum(1 for r in registration.validation_results if r.is_valid)
        total = len(registration.validation_results)

        report = f"""
{separator}
        REGISTRATION STATUS REPORT
{separator}
Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

REGISTRATION INFORMATION:
  Register Number: {registration.register_number}
  Email:          {registration.email}
  Course Code:    {registration.course_code}
  Semester:       {registration.semester}
  Mobile Number:  {registration.mobile_number}

VALIDATION SUMMARY:
  Fields Validated: {total}
  Passed:          {passed}
  Failed:          {total - passed}

STATUS: {status}
{separator}
"""

        if not registration.is_registration_successful:
            report += "\n⚠ FAILED VALIDATIONS:\n"
            report += "-" * 40 + "\n"
            for result in registration.validation_results:
                if not result.is_valid:
                    report += f"  • {result.field_name}: {result.message}\n"

        return report

    def generate_all_students_report(self) -> str:
        """Generate a summary report for all validated students."""
        if not self.validated_students:
            return "\nNo students have been validated yet.\n"

        separator = "=" * 60
        successful = sum(1 for s in self.validated_students if s.is_registration_successful)
        failed = len(self.validated_students) - successful

        report = f"""
{separator}
        BATCH REGISTRATION SUMMARY
        Total Students Processed: {len(self.validated_students)}
{separator}

{"Register Number":<20}{"Status":<15}{"Passed/Total":>12}
{"-" * 47}
"""
        for student in self.validated_students:
            passed = sum(1 for r in student.validation_results if r.is_valid)
            total = len(student.validation_results)
            status = "✓ APPROVED" if student.is_registration_successful else "✗ REJECTED"
            report += f"{student.register_number:<20}{status:<15}{passed}/{total}\n"

        report += f"""
{"-" * 47}
Total Approved: {successful}
Total Rejected: {failed}
Success Rate:   {(successful / len(self.validated_students)) * 100:.1f}%
{separator}
"""
        return report


# Sample student registrations for testing
SAMPLE_REGISTRATIONS = [
    # Valid registration
    {
        "register_number": "REG2024001",
        "email": "john.smith@university.edu",
        "course_code": "CS101",
        "semester": "1st Semester",
        "mobile_number": "+1-555-123-4567",
    },
    # Valid registration with different format
    {
        "register_number": "2024CS002",
        "email": "jane.doe@college.ac.in",
        "course_code": "MATH-201",
        "semester": "Fall 2024",
        "mobile_number": "9876543210",
    },
    # Invalid - wrong email domain
    {
        "register_number": "STU2024-003",
        "email": "bob@gmail.com",
        "course_code": "PHY301",
        "semester": "Sem 3",
        "mobile_number": "+91-98765-43210",
    },
    # Invalid - wrong register number format
    {
        "register_number": "INVALID123",
        "email": "alice@mit.edu",
        "course_code": "CHEM101",
        "semester": "III",
        "mobile_number": "1234567890",
    },
    # Invalid - wrong course code and semester
    {
        "register_number": "REG2024005",
        "email": "charlie@oxford.ac.uk",
        "course_code": "123",
        "semester": "Invalid Semester",
        "mobile_number": "555-1234",
    },
]


def main():
    """Main function to demonstrate the University Registration System."""
    registration_system = UniversityRegistrationSystem()

    print("\n" + "=" * 70)
    print("     UNIVERSITY REGISTRATION VALIDATION SYSTEM")
    print("     Using Regular Expressions")
    print("=" * 70)

    # Process each registration
    for i, student_data in enumerate(SAMPLE_REGISTRATIONS, 1):
        print(f"\n{'─' * 70}")
        print(f"Processing Student #{i}")
        print(f"{'─' * 70}")

        # Validate student
        registration = registration_system.validate_student(**student_data)

        # Display validation results
        print(registration_system.display_validation_results(registration))

        # Display registration report
        print(registration_system.generate_registration_report(registration))

    # Generate batch summary
    print("\n" + "=" * 70)
    print("📊 BATCH PROCESSING SUMMARY")
    print("=" * 70)
    print(registration_system.generate_all_students_report())

    return registration_system


if __name__ == "__main__":
    main()
