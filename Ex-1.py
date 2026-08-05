import re

text = "My phone number is 9876543210 and my email is student123@gmail.com."

match_result = re.match(r"My", text)

if match_result:
    print("Match found at the beginning:", match_result.group())
else:
    print("No match found at the beginning.")

search_result = re.search(r"\d{10}", text)

if search_result:
    print("Phone number found:", search_result.group())
else:
    print("Phone number not found.")

email_result = re.search(r"\w+@\w+\.\w+", text)

if email_result:
    print("Email found:", email_result.group())
else:
    print("Email not found.")
    