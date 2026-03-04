# Dictionary of countries and their capitals
quiz = {"France": "Paris","Germany": "Berlin","Italy": "Rome","Spain": "Madrid","Portugal": "Lisbon","Netherlands": "Amsterdam","Belgium": "Brussels","India": "Delhi","Norway": "Oslo","United Arab Emirates": "Abu Dhabi"}

score = 0 # Initialize score

# Loop through each country in the quiz
for country in quiz:
    answer = input("What is the capital of " + country + "?")
    if answer.lower() == quiz[country].lower():
        print("Correct!\n")
        score= score + 1
    else:
        print("Wrong! The capital is " + quiz[country]+"\n")
        
# Feedback
print("Your score is", score, "out of", len(quiz))

