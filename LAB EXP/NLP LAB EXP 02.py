def ends_with_ab(string):
    if string.endswith("ab"):
        return True
    else:
        return False
string = input("Enter a word: ")
if(ends_with_ab(string)):
    print("Accepted : String ends with ab")
else:
    print("Not Accepted : string doesnt end with ab")