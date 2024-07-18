import re

def is_valid_nickname(nickname):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$'
    return re.match(pattern, nickname) is not None

# Read the input nickname
nickname = input()

# Check if the nickname is valid
if is_valid_nickname(nickname):
    print("YES")
else:
    print("NO")