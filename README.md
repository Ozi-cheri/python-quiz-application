
# Python Quiz Application

This is a Python quiz application that allows a player to answer multiple-choice questions on a particular topic. The application uses dictionaries, lists, and tuples to manage the quiz data and provide a smooth user experience. Players are welcomed, they are asked to enter their names, and then participate in a quiz consisting of 4 questions. The quiz provides feedback based on the player's score at the end.

## User Stories

- **As a** user,i want to see my quiz score immediately after completing a quiz so that i can know ho i performed.
- **As a** user, i want to see the correct the answer to the question i got wrong so i can learn,increase my knowledge and avoid making mistakes in future.
- **As a** user,i want a question with multiple choice options.



## Features

- **Topic Definition**: The quiz has a defined topic.
- **Player Interaction**: The player is welcomed and asked to input their name.
- **Multiple Choice Questions**: The quiz contains 4 questions, each with multiple-choice options.
- **Use of Data Structures**:
  - **Dictionary**: To store questions and their corresponding optionns and answers.
  - **List**:  Manages multiple-choice options for each question.
  - **Tuple**: Defines the immutable correct answers.
- **Score Calculation**: The player's score is calculated and displayed based on each correct answers.
- **Feedback**: Feedback is provided based on the player's score.
### Quiz Structure

1. **Welcome and Player Input**:
    - The player is welcomed and prompted to enter their name.
    - Example:
      ```
      Welcome to the Python Quiz!
      Please enter your name: Ada
      ```

2. **Quiz Questions**:
    - The quiz presents 4 questions with multiple-choice options.
    - The player selects an answer by typing the corresponding letter e.g., a, b, c, d.
    - Example:
      ```
      Q1: What is the full meaning  of PEP?
      A. Python element particles
      B. Prepaid elected python
      C. Python pack project
      D. Python enhancement proposal
      Enter your answer: D
      ```

3. **Score Calculation and Feedback**:
    - As the questions are been answered, the player receives  score and feedback based on their performance.
    - Example feedback based on score:
      - **2-3**: "Good job! 
      - **4**: "Excellent! Congratulations You got all the questions correct!"

### Variables and Data Structures

- **`topic`**: A string variable that defines the quiz topic.
- **`player_name`**: A variable to store the player's name input.
- **`questions`**: A dictionary where keys are questions and values are lists of possible answers.
- **`correct_answers`**: A tuple containing the correct answers for the questions.
- **`score`**: An integer variable to track the player's score.

### Code Structure
```
"""Define the quiz topic"""
"Python Quiz Application"

"""Welcome the player"""
print(f"Welcome to the {Python} Quiz! Application")
player_name = input("Please enter your name: ")

"""Dictionary to store questions and their multiple-choice options"""
quiz= {
    "What is the full meaning of PEP?
}

correct_answers = ('d', 'b, 'c', 'd')

"""Initialize score"""
score = 0

""" define questions and get answers"""

    for question,details in quiz.items():
        print("question")
        for option in details("options"):
            print(option)
       if answer == details ("answer")
       print("correct!\n")
       score +=1
```
       
###  Credit 

- Code institute for the deployment terminal
- LMS
- w3school(https://www.w3schools.com)

        