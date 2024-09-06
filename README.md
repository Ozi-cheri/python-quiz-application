
# Python Quiz Application

# Introduction
The Python quiz application  is a simple command-line quiz game. It provides the player with a series of multiple-choice questions about Python and general computer science topics. The player must answer each question by selecting from  the options a,b,c or d. Ater completing the quiz, the player's score is displayed,and they are given the option to play again or quit.

## User Stories

- **As a** user,i want to see my quiz score immediately after completing a quiz so that i can know how i performed.
- **As a** user, i want to see the correct answer to the question i got wrong so i can learn,increase my knowledge and avoid making mistakes in future.
- **As a** user, i want a question with multiple choice options.
- **As a** user, if i mistakenly enter an invalid answer,i will be reminded to enter a valid given. 
- **As a** user, i will like to be guided with rules to ensure i flow along easily with the quiz.
- **As a** user, i will like to replay the game especially if i got bad score.
## Typography

I decided to go for Courier New Monosapce because it almost matches the text of that of the Python Terminal.


## Features
### Existing Features

- **Topic Definition**: The quiz has a readable and defined topic.
- **Multiple Choice Questions**: The quiz contains 4 questions, each with 4 multiple-choice options.
- **Use of Data Structures**:
  - **Dictionary**: To store questions and their corresponding optionns and answers.
  - **List**:  Manages multiple-choice options for each question.
  - **Tuple**: Defines the immutable correct answers.
- **Score Calculation**: The player's score is calculated and displayed at the end of the quiz.
- **Feedback**: Feedback is provided based on the player's score.

### Quiz Structure

1. **Welcome and Player Input**:
    - The player is welcomed and prompted to enter their name.
    - Example:
      ```
      Welcome to the Python Quiz!
      Please enter your name: Ada
      ```
      Validation is used here to ensure they enter a name using alphabetical characters only. If the name is not in alphabetical character,the player will be reminded to enter a valid name.
     
      ![Reference image](/images/screenshot8.png)


2. **Quiz Questions**:
    - The quiz presents 4 questions with multiple-choice options.
    - The player selects an answer by typing the corresponding letter e.g., a, b, c or d.
    - Example:
      ```
      Q1: What is the full meaning  of PEP?
      A. Python element particles
      B. Prepaid elected python
      C. Python pack project
      D. Python enhancement proposal
      Enter your answer: D
      ```
      Validation is used to ensure they enter only valid answer.When they enter an invalid answer,a message pops up reminding them to enter a valid answer.

      ![Refrence image](/images/screenshot1.png)

      

3. **Score Calculation Feedback And Replay**:
    - As the questions are been answered, the player receives  score and feedback based on their performance.
    - Example feedback based on score:
      - **2-3**: "Good job! 
      - **4**: "Excellent! Congratulations You got all the questions correct!"

      ![Reference image](/images/screenshot5.png)

      The player is given an option to play again or eist.

      ![Reference image]

### Code Overview
#### Key Files
-quiz_app.py: This is the main Python script containing the quiz logic.
#### Code Functions
1.Validate_name(name): Validate sthe player's name to ensure it only contzains alphabetic characters and spaces.
2.Validat_answer(answer): Validates the player's answer to ensure it correspond to one of the options:a,b,c or d.
3.Play_quiz(): Handles the quiz logic,as well as asking questios, checking answers and displaying scores.
4.Main(): Manages the flow of the game,including replaying or quitting based on the player's choice.



### Code Structure Example
```

#  Define the quiz topic
"Python Quiz Application"

#  Welcome the player
print(f"Welcome to the {Python} Quiz! Application")
player_name = input("Please enter your name: ")
if validate_name(player_name) :
    break

#  Defines the quiz questions,options and other variables
quiz= {
    "What is the full meaning of PEP?: 
}

correct_answers = ('d', 'b, 'c', 'd')

#  Initialize 
score = 0

#  Iterate through the quiz questions

    for question,details in quiz.items():
        print(question)
        for option in details("options"):
            print(option)
               
```

![Reference image](/images/screenshot3.png)

![Reference image](/images/screenshot6.png)

### Features Left to Implement


### Technologies used

-Python(Version 3.x)
-Regular expression for input(re module)
No additional dependencies were used for this project,it only relies on Python's built in libraries.





### Testing



### Challenges Faced



### Code Validation


### Deployment
       

### Credits
### Content 

- Code institute for the deployment terminal
- LMS
- w3school(https://www.w3schools.com)

        