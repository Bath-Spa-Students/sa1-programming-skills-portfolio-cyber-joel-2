# Correct password
correct_pass = "12345"
attempts = 0
max_attempts = 5

# Loop until max attempts reached
while attempts < max_attempts:
    password = input("\nEnter The Password: ")
    if password == correct_pass:
        print("\nAccess Granted!")
        break
    else:
        attempts += 1
        print(f"\nIncorrect Password. Attempts Remaining: {max_attempts - attempts}")
else:
    print("\nMaximum Attempts Reached.")
