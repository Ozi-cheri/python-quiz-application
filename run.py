
"""Welcoming the player."""

print("Welcome to Python Quiz Application:")
player_name = input("Please enter your name:")
print(f"Hello, {player_name}! let's start the quiz.\n")

"""Define the quiz questions,options and other variables."""
quiz = {
    "What is the full meaning of PEP?":{
        "options":["a) Python element particles", 
"b) Prepared elected python" ,
"c) Python pack project" , "d) Python enhancement proposal"] ,
        "answer" : "d"
  },
    "What is the full meaning of Ram?":{
      "options":["a) Remedy after memory","b) Random acess memory",
"c) Release access memory", "d) Ready at memory"],
      "answer":"b"
  },   
    "What is RAM?":{
      "options":["a) Media for coding" , "b) Computer disk" ,
"c) A storage medium for computers" , "d) A file"] ,
      "answer": "c"
  },
    "What will you get if you use a variable name before a variable is assigned?":{
      "options":["a) Function", "b) File", "c) String", "d) Error"] ,
      "answer": "d"
      
    }
}

"""Initialize score."""

score = 0

"""Iterate through the quiz questions."""

for question,details in quiz.items():
  print(question)
  for option in details["options"]:
    print(option)
  
  """Get the player's answer."""
  
  answer = input("Please enter your the answer:").lower()
  
  """Check if the answer is correct."""
  
  if answer == details["answer"]:
    print("Correct!\n")
    
    score += 1
  else:
     print(f"Wrong! The correct answer is {details['answer']}. \n")
  
  """Provide feedback based on score."""
  
  print(f"Your score is {score}/{len(quiz)}")
  if score == len(quiz):
      
      if score == len(quiz):
       print("Excellent!You got all the questions correct.")
  elif score >= len(quiz) // 2:
      print("Good Job")
  else:
    ("Good luck next time. Keep learning.Thank you for participating.")
    

      
     
     

     

    
     

    





        
    

    
    
    



    




    

    

    
    



    



