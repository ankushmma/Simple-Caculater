#PROJECT KBC GAME
import random

questions = [
    {"question": "What is the capital of India?", "options": ["New Delhi", "Mumbai", "Kolkata", "Chennai"], "answer": "New Delhi"},
    {"question": "Who is the Prime Minister of India?", "options": ["Narendra Modi", "Rahul Gandhi", "Manmohan Singh", "Amit Shah"], "answer": "Narendra Modi"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
    {"question": "Who wrote 'Harry Potter'?", "options": ["J.K. Rowling", "J.R.R. Tolkien", "George R.R. Martin", "Suzanne Collins"], "answer": "J.K. Rowling"},
    {"question": "Which is the largest ocean on Earth?", "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "answer": "Pacific Ocean"}
]

def ask_question(question_data):
    print("\n" + question_data["question"])
    for i, option in enumerate(question_data["options"], 1):
        print(f"{i}. {option}")
    
    while True:
        try:
            user_answer = int(input("\nChoose your option (1-4): "))
            if user_answer < 1 or user_answer > 4:
                print("Please choose a valid option (1-4).")
                continue
            if question_data["options"][user_answer - 1] == question_data["answer"]:
                print("Correct answer!")
                return True
            else:
                print(f"Wrong answer! The correct answer was: {question_data['answer']}")
                return False
        except ValueError:
            print("Invalid input, please choose a number between 1 and 4.")

def play_game():
    print("Welcome to Kaun Banega Crorepati!")
    score = 0
    question_count = 1
    random.shuffle(questions)
    for question_data in questions:
        print(f"\nQuestion {question_count}")
        if ask_question(question_data):
            score += 1
        question_count += 1
    print(f"\nYour final score is: {score} out of {len(questions)}")

if __name__ == "__main__":
    play_game()
