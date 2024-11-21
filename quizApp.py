import sys

# Global dictionaries for user data and quizzes
users = {}
quizzes = {
    'python': [
        {'question': "What is the output of print(len('Hello'))?", 'options': ['4', '5', '6', '7'], 'answer': '5'},
        {'question': "Which function is used to get input from a user in Python?", 'options': ['get()', 'input()', 'read()', 'scan()'], 'answer': 'input()'}
    ],
    'dsa': [
        {'question': "What is the time complexity of merging two sorted arrays?", 'options': ['O(n)', 'O(n log n)', 'O(1)', 'O(n^2)'], 'answer': 'O(n)'},
        {'question': "Which data structure uses LIFO principle?", 'options': ['Queue', 'Stack', 'Deque', 'Heap'], 'answer': 'Stack'}
    ],
    'cse': [
        {'question': "What does RAM stand for?", 'options': ['Random Access Memory', 'Read And Modify', 'Rapid Access Memory', 'Random Allocation Memory'], 'answer': 'Random Access Memory'},
        {'question': "Which device is primarily used for long-term data storage?", 'options': ['CPU', 'GPU', 'Hard Drive', 'RAM'], 'answer': 'Hard Drive'}
    ]
}


# Function to register a new user
def register():
    print("\nRegister")
    username = input("Enter username: ")
    if username in users:
        print("Username already exists. Please try again.")
    else:
        password = input("Enter password: ")
        users[username] = password
        print("Registration successful! Please login to continue.")

# Function to login
def login():
    print("\nLogin")
    username = input("Enter username: ")
    if username not in users:
        print("Username not found. Please register first.")
        return False
    password = input("Enter password: ")
    if users[username] == password:
        print("Login successful!")
        return True
    else:
        print("Incorrect password.")
        return False

# Function to display the quiz options and handle quiz attempt
def attempt_quiz():
    print("\nSelect a quiz:")
    print("1. Python")
    print("2. DSA")
    print("3. CSE")
    
    choice = input("Enter your choice (1-3): ")
    if choice == '1':
        quiz_type = 'python'
    elif choice == '2':
        quiz_type = 'dsa'
    elif choice == '3':
        quiz_type = 'cse'
    else:
        print("Invalid choice. Returning to main menu.")
        return

    # Start the selected quiz
    score = 0
    for question in quizzes[quiz_type]:
        print("\n" + question['question'])
        for i, option in enumerate(question['options'], start=1):
            print(f"{i}. {option}")
        answer = input("Your answer: ")
        if answer == question['answer']:
            score += 1

    print(f"\nQuiz completed! Your score: {score}/{len(quizzes[quiz_type])}")


while True:
        print("\nMain Menu")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            register()
        elif choice == '2':
            if login():
                while True:
                    print("\nQuiz Menu")
                    print("1. Attempt Quiz")
                    print("2. Logout")
                    
                    sub_choice = input("Enter your choice (1-2): ")
                    
                    if sub_choice == '1':
                        attempt_quiz()
                    elif sub_choice == '2':
                        print("Logged out. Returning to main menu.")
                        break
                    else:
                        print("Invalid choice.")
        elif choice == '3':
            print("Exiting the quiz app. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

