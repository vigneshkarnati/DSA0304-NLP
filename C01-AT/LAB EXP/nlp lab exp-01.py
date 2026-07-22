import re
text = input("enter the text: ")
pattern = input("enter pattern to search: ")
match = re.search(pattern,text)
if match:
    print("pattern found")
    print(str(match.start()) +" "+ str(match.end()))
else:
    print("pattern not found")