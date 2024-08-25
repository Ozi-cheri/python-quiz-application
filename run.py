

print("Python Quiz Application")


print("***********************")
name = input("Please enter your name.")
print(f"Hello {name}")
print("***********************")
print("Welcome To Python Quiz Application")
user = input("Do you want to continue?\n Yes or No\n")
if user == "yes":
    print("let's start the quiz")
else:
        print("Thanks for stopping by")
        quit()
print("Rules \nSelect from the letters A-D the correct options of each question.")

questions = [
    "What is the full meaning of PEP in python?", "What is the full meaning of RAM?", "What is RAM?", "What will you get if you use a variable name before it has a value assigned?", "Computers have a hardware called."]
      
options = (("A. Python element particle", "B. Prepared enhancement python", "C. Python enhancement proposal","D. Pet python pen"),
          ("A. Remedy at memory","B. Random acces memory","C . Release acces memory","D. Ready at memory"),
          ("A. A medim of coding","B. Computer disk","C. A storage medium for computers", "D. A file"),
          ("A. Function", "B. error", "C. string", "D. File"),
          ("A. storage", "B. pattern", "C. git", "D. code"))

option = 0
user_answer = 0
score = 0
question_num = 0

for question in questions:
    print("**********************************")
    print(question)
    for option in options[question_num]:
        print(option)
    
    question_num += 1

    

    
    



    



