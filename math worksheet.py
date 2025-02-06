import random

from datetime import datetime

from datetime import datetime



# Get the current time
now = datetime.now()

# Calculate seconds since the start of the day
seconds_since_midnight1 = now.hour * 3600 + now.minute * 60 + now.second

seconds_per_question = 0
wrongAnswers = 0 
count = 0

operation = input("Choose from add, sub, sub with carry, or mixed: ")
valid_operations = ["add", "sub", "mixed", "sub with carry", "swc"]

while operation.lower() not in valid_operations:
    print("Invalid operation.")
    operation = input("Choose from add, sub, sub with carry, or mixed: ")
    

desired_seconds_per_question = input("What is your desired seconds per question: ")

totalQuestions = int(input("How many questions would you like: "))

# Get the current time
now = datetime.now()

# Calculate seconds since the start of the day with a small buffer to account for the start
seconds_since_midnight1 = (now.hour * 3600 + now.minute * 60 + now.second)-2


#----------------------------------------------------------------------------------------
while count < (totalQuestions):

    if operation.lower() == "add":
        num1 = random.randrange(0, 100)
        num2 = random.randrange(0, 100)

        playerAnswer = input(f"Question Number {count + 1}: {num1} + {num2} = ")
            
        if playerAnswer.lower() == "restart":
            count = 0
            wrongAnswers = 0
            print("The question set has been reset.")

        elif playerAnswer.lower() == "end":
            count = totalQuestions

        elif int(playerAnswer) == (num1 + num2):
            print("Correct!")
            count += 1
                
            if count == totalQuestions:
                print("The question set has been completed!")
                break

        else:
            newAnswer = input("Incorrect! Try Again: ")
            wrongAnswers += 1

            if newAnswer.lower() == "restart":
                count = 0
                wrongAnswers = 0
                print("The question set has been reset.")

            elif int(newAnswer) == (num1 + num2):
                count += 1
                print("Correct!")
    
            else:
                print(f"Incorrect! The answer was {num1 + num2}. Try another problem.")
                wrongAnswers += 1

#------------------------------------------------------------------------------------------
    elif operation.lower() == "sub":
        num1 = random.randrange(0, 100)
        num2 = random.randrange(0, num1 + 1)
                
        playerAnswer = input(f"Question Number {count + 1}: {num1} - {num2} = ")
                
        if str(playerAnswer).lower() == "restart":
            count = 0
            wrongAnswers = 0
            print("The question set has been reset.")


        elif playerAnswer.lower() == "end":
            count = totalQuestions


        elif int(playerAnswer) == (num1 - num2):
            print("Correct!")
            count += 1
                
            if count == totalQuestions:
                print("The question set has been completed!")
                break

           
        else:
            newAnswer = input("Incorrect! Try Again: ")
            wrongAnswers += 1

            if newAnswer.lower() == "restart":
                count = 0
                wrongAnswers = 0
                print("The question set has been reset.")
                
            elif int(newAnswer) == (num1 - num2):
                count += 1
                print("Correct")
            else:
                print(f"Incorrect! The answer was {num1 - num2}. Try another problem.")
                wrongAnswers += 1
#-----------------------------------------------------------------------------------------------
    elif operation.lower() == "mixed":
        picker = random.randrange(1, 3)  # Randomly pick addition or subtraction
        if picker == 1:  # Addition
            num1 = random.randrange(0, 100)
            num2 = random.randrange(0, 100)

            playerAnswer = input(f"Question Number {count + 1}: {num1} + {num2} = ")

            if str(playerAnswer).lower() == "restart":
                count = 0
                wrongAnswers = 0
                print("The question set has been reset.")


            elif playerAnswer.lower() == "end":
                count = totalQuestions

            elif int(playerAnswer) == (num1 + num2):
                print("Correct!")
                count += 1
                
                if count == totalQuestions:
                    print("The question set has been completed!")
                    break

            
            else:
                newAnswer = input("Incorrect! Try Again: ")
                wrongAnswers += 1

                if newAnswer.lower() == "restart":
                    count = 0
                    wrongAnswers = 0
                    print("The question set has been reset.")
                
                elif int(newAnswer) == (num1 + num2):
                    count += 1
                    print("Correct!")
                else:
                    print(f"Incorrect! The answer was {num1 + num2}. Try another problem.")
                    wrongAnswers += 1
#---------------------------------------------------------------------------------------------------------------
        elif picker == 2:  # Subtraction
            num1 = random.randrange(0, 100)
            num2 = random.randrange(0, num1 + 1)
                
            playerAnswer = input(f"Question Number {count + 1}: {num1} - {num2} = ")

            if str(playerAnswer).lower() == "restart":
                count = 0
                wrongAnswers = 0
                print("The question set has been reset.")
   


            elif playerAnswer.lower() == "end":
                count = totalQuestions


            elif int(playerAnswer) == (num1 - num2):
                print("Correct!")
                count += 1
                
                if count == totalQuestions:
                    print("The question set has been completed!")
                    break

            else:
                newAnswer = input("Incorrect! Try Again: ")
                wrongAnswers += 1

                if newAnswer.lower() == "restart":
                    count = 0
                    wrongAnswers = 0
                    print("The question set has been reset.")
                
                elif int(newAnswer) == (num1 - num2):
                    count += 1
                    print("Correct")
                else:
                    print(f"Incorrect! The answer was {num1 - num2}. Try another problem.")
                    wrongAnswers += 1
#--------------------------------------------------------------------------------------------------------------------------------------------------

    elif operation.lower() == "sub with carry" or "swc":
        while count < totalQuestions:
        # Generate two random numbers where borrowing will definitely happen
            num1 = random.randint(10, 999)  # Minuend
            num2 = random.randint(1, num1 - 1)  # Subtrahend
        
        # Ensure borrowing in ones place (for two-digit numbers)
            if num1 % 10 >= num2 % 10:
                num1 = random.randint(10, 99)  # Regenerate num1 if borrowing in ones is not happening
                num2 = random.randint(1, num1 - 1)
        
        # Ensure borrowing in the tens place if needed
            if num1 >= 100:
                if (num1 // 10) % 10 >= (num2 // 10) % 10:  # Borrowing happens in the tens place
                    num1 = random.randint(100, 999)
                    num2 = random.randint(1, num1 - 1)

        # Ask the player for the answer
           
            playerAnswer = input(f"Question {count + 1}: {num1} - {num2} = ")
            
            if playerAnswer.lower() == "restart":
                count = 0
                wrongAnswers = 0
                print("The question set has been reset.")
                break
        
            elif playerAnswer.lower() == "end":
                print(f"Total wrong answers: {wrongAnswers}")
                    
            
            elif int(playerAnswer) == (num1 - num2):
                print("Correct!")
                count += 1
                
                
                if count == totalQuestions:
                    print("The question set has been completed!")
                    break

            else:
                newAnswer = input("Incorrect! Try Again: ")
                wrongAnswers += 1

                if newAnswer.lower() == "restart":
                    count = 0
                    wrongAnswers = 0
                    print("The question set has been reset.")
                
                elif int(newAnswer) == (num1 - num2):
                    count += 1
                    print("Correct")
                else:
                    print(f"Incorrect! The answer was {num1 - num2}. Try another problem.")
                    wrongAnswers += 1


#--------------------------------------------------------------------------------------------------------------


if wrongAnswers > 5:
    print(f"You got a total of {wrongAnswers} questions wrong.")

elif 0 < wrongAnswers <= 5:
    print(f"You got most of the questions right. Only {wrongAnswers} question were wrong. Good Job!")

elif wrongAnswers == 0:
    print(f"You got all of the questions right. Good Job!")
#else:
    #print(f"You got a total of {wrongAnswers} questions wrong. :(")

    

#--------------------------------------------------------------------------------------------------------------------------
    
# Get the current time
now = datetime.now()

# Calculate seconds since the start of the day
seconds_since_midnight2 = now.hour * 3600 + now.minute * 60 + now.second

seconds_taken = seconds_since_midnight2 - seconds_since_midnight1


seconds_per_question = seconds_taken/totalQuestions

if seconds_per_question > int(desired_seconds_per_question):
    print(f"You took {seconds_per_question} seconds per question on average. Try to go faster next time.")
else:
    print(f"You only took {seconds_per_question} seconds per question on average. Good Job!")

