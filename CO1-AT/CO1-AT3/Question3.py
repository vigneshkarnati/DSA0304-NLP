import re

text = """
Meeting on 12/09/2026
Call 9876543210
#NLP
@OpenAI
natural language processing
"""

while True:
    print("\n1.Search Date")
    print("2.Search Phone Number")
    print("3.Search Hashtag")
    print("4.Search Mention")
    print("5.Search Prefix")
    print("6.Search Suffix")
    print("7.Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        print(re.findall(r'\b\d{2}/\d{2}/\d{4}\b', text))

    elif choice == "2":
        print(re.findall(r'\b[6-9]\d{9}\b', text))

    elif choice == "3":
        print(re.findall(r'#\w+', text))

    elif choice == "4":
        print(re.findall(r'@\w+', text))

    elif choice == "5":
        prefix = input("Enter Prefix: ")
        print(re.findall(r'\b' + prefix + r'\w*', text, re.IGNORECASE))

    elif choice == "6":
        suffix = input("Enter Suffix: ")
        print(re.findall(r'\b\w*' + suffix + r'\b', text, re.IGNORECASE))

    elif choice == "7":
        break

    else:
        print("Invalid Choice")