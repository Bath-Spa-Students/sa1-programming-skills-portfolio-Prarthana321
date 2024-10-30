# Basic requirements: Single question about the capital of France.
print("Basic")
print("---------------------------")
answer = input("What is the capital of France? ").strip()
if answer.lower() == "paris":
    print("Correct! The answer is Paris.")
else:
    print("Incorrect. The correct answer is Paris.")

# Advanced requirements: Quiz with multiple questions
print("advanced ")
print("---------------------------")
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
    
score = 0
    
for country, capital in questions.items():
    answer = input(f"What is the capital of {country}? ").strip()
    if answer.lower() == capital.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {capital}.")
    
    print(f"\nYour final score: {score}/{len(questions)}")

