transitions = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q0',
    ('q1', 'a'): 'q1',
    ('q1', 'b'): 'q2',
    ('q2', 'a'): 'q1',
    ('q2', 'b'): 'q0'
}

start_state = 'q0'
final_state = 'q2'

string = input("Enter String: ")

state = start_state
path = [state]

for ch in string:
    if (state, ch) in transitions:
        state = transitions[(state, ch)]
        path.append(state)
    else:
        print("Invalid Input")
        exit()

print("Transition Path:")
print(" -> ".join(path))

if state == final_state:
    print("Accepted")
else:
    print("Rejected")