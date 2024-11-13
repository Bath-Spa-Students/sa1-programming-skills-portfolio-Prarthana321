# Basic requirements: Single question about the capital of France.
print("Basic")
print("---------------------------")
#Code for asking the input from the user.
answer = input("What is the capital of France? ").strip()
#Code for checking whether the answer is correct.
if answer.lower() == "paris":
    print("Correct! The answer is Paris.")
else:
    print("Incorrect. The correct answer is Paris.")

# Advanced requirements: Quiz with multiple questions
print("advanced ")
print("---------------------------")
#Code for Quiz of 10 european countries.
questions = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Denmark": "Copenhagen"
}
#Code for initializing the score.  
score = 0
#Code for checking the answer regardless of capitalization.
for country, capital in questions.items():
    answer = input(f"What is the capital of {country}? ").strip()
    if answer.lower() == capital.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {capital}.")
    
    print(f"\nYour final score: {score}/{len(questions)}")

