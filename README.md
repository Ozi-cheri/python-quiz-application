
# Python Quiz Application

![Welcome image](/images/screenshot21.png)

## Introduction
The Python quiz application  is a simple command-line quiz game. It provides the player with a series of multiple-choice questions about Python and general computer science knowledge. The player must answer each question by selecting from  the options a,b,c or d. Ater completing the quiz, the player's score and feedback are displayed,and they are given the option to play again or quit.

## User Stories

- **As a** user,i want to see my quiz score immediately after completing a quiz so that i can know how i performed.
- **As a** user, i want to see the correct answer to the question i got wrong so i can learn,increase my knowledge and avoid making mistakes in future.
- **As a** user, i want a question with multiple choice options.
- **As a** user, if i mistakenly enter an invalid answer,i will be reminded to enter the valid given answers.
- **As a** user, i will like to be guided with rules to ensure i flow along easily with the quiz.
- **As a** user, i will like to replay the game especially if i did not do well.
## Typography

* I decided to go for Courier New Monosapce as font family since it is a default font on many systems and apllication, commonly used in text editors,command line interfaces and terminal applications.


## Features
### Existing Features

- **Topic Definition**: The quiz has a readable and defined topic.
- **Multiple Choice Questions**: The quiz contains 8 questions, each with 8 multiple-choice options.
- **Use of Data Structures**:
  - **Dictionary**: To store questions and their corresponding options and answers.
  - **List**:  Manages multiple-choice options for each question.
  - **Tuple**: Defines the immutable correct answers.
- **Score Calculation**: The player's score is calculated and displayed at the end of the quiz.
- **Feedback**: Feedback is provided based on the player's score.

## Quiz Structure

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
    - The quiz presents 8 questions with multiple-choice options.
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
      Validation is used to ensure they enter only valid alphabical answer.

      ![Refrence image](/images/screenshot1.png)

3. **Score Calculation Feedback And Replay**:
    - As the questions are been answered, the player receives  score and feedback based on their performance.
    - Example feedback based on score:
      - **4-7**: "Good job! 
      - **8**: "Excellent! Congratulations You got all the questions correct!"

      ![Reference image](/images/screenshot14.png)

  In the above reference image,the function is wrapped in a while True loop to ensure the game keeps running until the player decides to quit.
  The quiz function (play_quiz()) is called if the player wants to replay.The game exits with a farewell message when the player chooses "no".If the player inputs anything other than "yes" or "no", the function will demand again for valid input.This function ensures smooth navigation between replaying the quiz or quitting, making the game more interactive and user-friendly.

  ![Reference image](/images/screenshot13.png)

  ![Reference image](/images/screenshot16.png)

  ## General Structure of How to Play
  * Enter your name:

You will be prompted to enter your name. The name should contain only alphabetic characters and spaces.
If the input is invalid, you will be prompted to re-enter your name until a valid name is provided.
  * Answering questions:

After the quiz begins, you will be presented with one multiple-choice question at a time.
Type either 'a', 'b', 'c', or 'd' as your answer, then press Enter.
If you provide an invalid answer, you will be prompted to try again.
  * Score feedback:

Once all questions are answered, your score will be displayed. You will receive feedback based on your performance.
  * Play again or quit:

After completing the quiz, you will be asked whether you want to play again.
Type 'yes' to start a new game or 'no' to quit.

## Lucid Chart
This was used to create the quiz flowchart which presents the appliication structure.
 ![Reference image](/images/screenshot20.png)

## Code Functions
* Quiz_app.py: This is the main Python script containing the quiz logic.
* Validate_name(name): Validate the player's name to ensure it only contains alphabetic characters and spaces.
* Validate_answer(answer): Validates the player's answer to ensure it correspond to one of the options:a,b,c or d.
* Play_quiz(): Handles the quiz logic,as well as asking questios, checking answers and displaying scores.
* Main(): Manages the flow of the game,including replaying or quitting based on the player's choice.

## Code Structure Example

![Reference image](/images/screenshot22.png)

## Features Left to Implement
* I would implement a multiplayer mode where two or more players can compete by answering questions in turns in future.


## Technologies used

* Python
* Regular expression for input(re module).
* pip for installing python packages.
* GitHub for storing the repository online during development.
* Gitpod as a cloud based IDE.

## External Python Package Used
* Pyfiglet, a library to convert text to ascii.

## Testing

* As the apllication was being developed,i performed manual testing regulary in the terminal making sure i get required outputs.

## Challenges Faced
* During validation, there were few errors indicating no new line at the end of file. Example;
```
if__name__=="__main__":
      main()
This was corrected by ensuring i starts new lines at the end of files.
```



## Code Validation
* The code was validated using the code institute python linter.
* No issues or error where found.
![Reference image](/images/screenshot23.png)

## Deployment

  * Sign up for Heroku account and create free account. Create new app on Heroku by filling the form. Add the buildparks starting with Python,save then nodejs and save as well respectively. Locate the deploy section,select Github and connect to it. Search for Github repository name and connect to link up the Heroku app to my Github repository code. Finally i deployed manually.
       
## Credits
### Content 

- Code institute (https://codeinstitute.net/) 
  * I made use of the LMS python essentials walkthrough videos to get the general knowledge of the Python project and as i develop the project. The questions used was generated from LMS. Code institute python essential template was also used for the development of the application.

- Stack Overflow (https://stackoverflow.com)
  * For the code to validate player's name and input of correct answer.

- w3school(https://www.w3schools.com)
  * W3school was used as the project was being develpoed.


        