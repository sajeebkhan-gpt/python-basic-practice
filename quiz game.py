def quiz_game():
    # List of questions and answers
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["1. Berlin", "2. Paris", "3. Madrid", "4. Rome"],
            "answer": 2
        },
        {
            "question": "Which programming language is known as 'snake case'?",
            "options": ["1. Python", "2. Java", "3. C++", "4. JavaScript"],
            "answer": 1
        },
        {
            "question": "What is 5 + 3?",
            "options": ["1. 6", "2. 7", "3. 8", "4. 9"],
            "answer": 3
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["1. Venus", "2. Mars", "3. Jupiter", "4. Saturn"],
            "answer": 2
        }
    ]

    # Initialize score
    score = 0

    print("Welcome to the Quiz Game!")
    print("--------------------------\n")

    # Loop through each question
    for i, q in enumerate(questions):
        print(f"Question {i + 1}: {q['question']}")
        for option in q["options"]:
            print(option)
        try:
            user_answer = int(input("Enter the option number (1-4): "))
            if user_answer == q["answer"]:
                print("Correct!\n")
                score += 1
            else:
                print("Wrong answer.\n")
        except ValueError:
            print("Invalid input. Moving to the next question.\n")

    # Show the final result
    print(f"Quiz Over! You scored {score} out of {len(questions)}.\n")
    if score == len(questions):
        print("🎉 Excellent! You got a perfect score!")
    elif score > len(questions) // 2:
        print("Good job! Keep practicing. 👍")
    else:
        print("Don’t worry, try again and you'll improve! 😊")


# Call the quiz game function
quiz_game()
