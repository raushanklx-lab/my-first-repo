#---------- Q2. Check if a string is a palindrome ----------



# Get input from the user
s = input("Enter the Name: ")

# Convert to lowercase and remove non-alphanumeric characters
cleaned = ""
for char in s:
    if char.isalnum():  # keeps letters and numbers only
        cleaned += char.lower()

# Check palindrome
if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
