
# Function to validate the player's name (only alphabetic characters and spaces)
import re
def validate_name(name):
    if re.match("^[A-Za-z ]+$", name):
        return True
    else:
        print("Invalid name. Please enter a name using alphabetic characters only.")
        return False

# Function to validate the player's answer (must be a single character a, b, c, or d)
def validate_answer(answer):
    if re.match("^[a-dA-D]$", answer):
        return True
    else:
        print("Invalid answer. Please enter a valid option (a, b, c, or d).")
        return False

# Function to run the quiz
def play_quiz():
    print(f"Hello, {player_name}! Let's start the quiz.\n")
    print("Rules: Enter either a, b, c, or d for the correct answer to each question.")

    # Define the quiz questions, options, and other variables
    quiz = {
        "What is the full meaning of PEP?": {
            "options": ["a) Python element particles", 
                        "b) Prepared elected python",
                        "c) Python pack project", 
                        "d) Python enhancement proposal"],
            "answer": "d"
        },
        "What is the full meaning of RAM?": {
            "options": ["a) Remedy after memory",
                        "b) Random access memory",
                        "c) Release access memory", 
                        "d) Ready at memory"],
            "answer": "b"
        },
        "What is RAM?": {
            "options": ["a) Media for coding",
                        "b) Computer disk",
                        "c) A storage medium for computers",
                        "d) A file"],
            "answer": "c"
        },
        "What will you get if you use a variable name before a variable is assigned?": {
            "options": ["a) Function", 
                        "b) File", 
                        "c) String", 
                        "d) Error"],
            "answer": "d"
        }
    }

    # Initialize score
    score = 0

    # Iterate through the quiz questions
    for question, details in quiz.items():
        print(question)
        for option in details["options"]:
            print(option)
        # Get the player's answer with validation
        while True:
            answer = input("Please enter your answer: ").lower()
            if validate_answer(answer):
                break
        # Check if the answer is correct
        if answer == details["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {details['answer']}.\n")

    # Provide feedback based on score
    print(f"Your score is {score}/{len(quiz)}")
    if score == len(quiz):
        print("Excellent! You got all the questions correct.")
    elif score >= len(quiz) // 2:
        print("Good Job!")
    else:
        print("Good luck next time!")

# Main function to control whether the player wants to play again
def main():
    while True:
        play_quiz()

        # Ask if they want to replay or quit
        while True:
            choice = input("Do you want to play again? (yes/no): ").lower()
            if choice == 'no':
                print("Thanks for playing! Goodbye.")
                return  # Exit the entire program
            elif choice == 'yes':
                print("Starting a new game...\n")
                break  # Breaks inner loop and starts the quiz again
            else:
                print("Invalid choice, please type 'yes' or 'no'.")

# Run the main function if the script is executed
if __name__ == "__main__":
    print("Welcome to Python Quiz Application:")
    while True:
        player_name = input("Please enter your name: ")
        if validate_name(player_name):
            break
    
    main()




      
     
     

     

    
     

    





        
    

    
    
    



    




    

    

    
    



    



