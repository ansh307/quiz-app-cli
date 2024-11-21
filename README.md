# Quiz Application cli

This is a simple command-line quiz application built with Python. It allows users to register, log in, and attempt quizzes on topics such as Python, Data Structures and Algorithms (DSA), and Computer Science Essentials (CSE). The program also keeps track of user accounts for a personalized experience.

---

## Features
- **User Registration**: Allows new users to create an account.
- **User Login**: Validates user credentials for secure access.
- **Quiz Selection**: Users can choose from three quiz topics:
  - Python
  - DSA
  - CSE
- **Scoring System**: Provides a score summary at the end of the quiz.
- **Logout and Exit Options**: Enables users to securely log out or exit the application.

---

## Requirements
- Python 3.6 or higher

---

## How to Run
1. Clone or download the project to your local system.
2. Open a terminal and navigate to the folder containing the program.
3. Run the program using:
   ```bash
   python quiz_app.py

## Example Usage
# Register
```
Main Menu
1. Register
2. Login
3. Exit
Enter your choice (1-3): 1

Register
Enter username: ansh
Enter password: password123
Registration successful! Please login to continue.
```
# Login
```
Main Menu
1. Register
2. Login
3. Exit
Enter your choice (1-3): 2

Login
Enter username: ansh
Enter password: password123
Login successful!
```
# Attempt Quiz
```
Quiz Menu
1. Attempt Quiz
2. Logout
Enter your choice (1-2): 1

Select a quiz:
1. Python
2. DSA
3. CSE
Enter your choice (1-3): 1

What is the output of print(len('Hello'))?
1. 4
2. 5
3. 6
4. 7
Your answer: 2

Which function is used to get input from a user in Python?
1. get()
2. input()
3. read()
4. scan()
Your answer: 2

Quiz completed! Your score: 2/2
```
