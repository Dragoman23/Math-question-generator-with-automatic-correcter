import random

from datetime import datetime

from datetime import datetime


operations = []

counter1 = 1

valid_inputs = {"1", "2", "3", "4", "5", "6", "7"} #, "8", "9", "10"} 
#--------------------------------------------------------------------------------------------------------
# Get the current time
now = datetime.now()

# Calculate seconds since the start of the day
seconds_since_midnight1 = now.hour * 3600 + now.minute * 60 + now.second

seconds_per_question = 0

wrongAnswers = 0 

count = 0

print("1.Addition - (Range:0 - 9999)\n\n2.Subtraction - (Range:0 - 9999)\n\n3.Multiplication - (Range:0 - 100)\n\n4.Division - (Range:0 - 1000)\n\n5.Subtraction with Carrying - (Range:0 - 9999)\n\n6.Custom Range Multiplication\n\n7.Custom Range Divison")

while True:
    number_of_operations = input("\nHow many operations do you want: ")
    if number_of_operations.isdigit():
        number_of_operations = int(number_of_operations)

        if 1 <= number_of_operations <= 7:
            break
        else:
            print("\nPlease enter a number between 1 and 7.")

    else:
        print("\nPlease enter a valid whole number.")

while counter1 <= int(number_of_operations):
    operation = input(f"\nEnter one of the assigned numbers to choose operation number {counter1}: ")
    

    while operation.lower() not in valid_inputs:
        operation = input(f"\nInvalid operation. Enter one of the assigned numbers to choose operation number {counter1}: ")

    if int(operation) == 1:
        operations.append("a")

    if int(operation) == 2:
        operations.append("s")

    if int(operation) == 3:
        operations.append("m")
    
    if int(operation) == 4:
        operations.append("d")

    if int(operation) == 5:
        operations.append("swc")

    if int(operation) == 6:
        operations.append("crm")

        while True:
             # Get range for the first number
            range1_input = input("Desired range for the first number (Multiplication): ")
            try:
                lower_range1, upper_range1 = [int(x.strip()) for x in range1_input.split('-')]
                break 
            except ValueError:
                print("Invalid format for the first number's range. Try again.")
               

        while True:
            # Get range for the second number
            range2_input = input("Desired range for the second number (Multiplication): ")
            try:
                lower_range2, upper_range2 = [int(x.strip()) for x in range2_input.split('-')]
                break
            except ValueError:
                print("Invalid format for the second number's range. Try again.")
                

    if int(operation) == 7:
        operations.append("crd")

        while True:   
             # Get range for the first number
            range3_input = input("Desired range for the dividend: ")
            try:
                lower_range3, upper_range3 = [int(x.strip()) for x in range1_input.split('-')]
                break
            except ValueError:
                print("Invalid input format for the dividend's range.")
                
        while True:
            # Get range for the second number
            range2_input = input("Desired range for the divisor (CAN'T START AT ZERO): ")
            try:
                lower_range2, upper_range2 = [int(x.strip()) for x in range2_input.split('-')]
                break
            except ValueError:
                print("Invalid input format for the divisor's range.")

                

       
    counter1 += 1
print(operations) # test/check
    

desired_seconds_per_question = input("What is your desired seconds per question: ")

totalQuestions = int(input("How many questions would you like: "))

# Get the current time
now = datetime.now()

# Calculate seconds since the start of the day
seconds_since_midnight1 = (now.hour * 3600 + now.minute * 60 + now.second)-2

#----------------------------------------------------------------------------------------
while count < (totalQuestions):

    operation = random.choice(operations)


# Addition
    
    if operation == "a":
        num1 = random.randrange(0, 10000)
        num2 = random.randrange(0, 10000)
        correct = False
        mistakes = 0

        while not correct:

            try:
                playerAnswer = input(f"Question Number {count + 1}: {num1} + {num2} = ")

                if playerAnswer.lower() == "restart":
                    count = 0
                    wrongAnswers = 0
                    print("The question set has been reset.")
                    break

                elif playerAnswer.lower() == "end":
                    count = totalQuestions
                    quit()

                elif int(playerAnswer) == (num1 + num2):
                    print("Correct!")
                    count += 1
                    correct = True
                     
                    if count == totalQuestions:
                        print("The question set has been completed!")
                        break

                else:
                    newAnswer = input("Incorrect! Try Again: ")
                    wrongAnswers += 1
                    mistakes += 1

                    if newAnswer.lower() == "restart":
                        count = 0
                        wrongAnswers = 0
                        print("The question set has been reset.")

                    elif int(newAnswer) == (num1 + num2):
                        count += 1
                        print("Correct!")
                        correct = True

                    elif mistakes >= 1:
                        print(f"Incorrect again! The correct answer was {num1 + num2}. Moving to another question.")
                        break
                       
                    else:
                        print(f"Incorrect! The answer was {num1 + num2}. Try another problem.")
                        wrongAnswers += 1
            except Exception as e:
                print(f"Invalid input: {e}. Please try again.")
            

#------------------------------------------------------------------------------------------
# Subtraction
    
    elif operation == "s":
        num1 = random.randrange(0, 10000)
        num2 = random.randrange(0, num1 + 1)
        correct = False
        mistakes = 0

        while not correct:

            try:
                
                playerAnswer = input(f"Question Number {count + 1}: {num1} - {num2} = ")
                        
                if str(playerAnswer).lower() == "restart":
                    count = 0
                    wrongAnswers = 0
                    print("The question set has been reset.")


                elif playerAnswer.lower() == "end":
                    count = totalQuestions
                    quit()


                elif int(playerAnswer) == (num1 - num2):
                    print("Correct!")
                    count += 1
                    correct = True
                        
                    if count == totalQuestions:
                        print("The question set has been completed!")
                        break

                   
                else:
                    newAnswer = input("Incorrect! Try Again: ")
                    wrongAnswers += 1
                    mistakes += 1

                    if newAnswer.lower() == "restart":
                        count = 0
                        wrongAnswers = 0
                        print("The question set has been reset.")
                        
                    elif int(newAnswer) == (num1 - num2):
                        count += 1
                        correct =True

                    elif mistakes >= 1:
                        print(f"Incorrect again! The correct answer was {num1 - num2}. Moving to another question.")
                        break
                    
                    else:
                        print(f"Incorrect! The answer was {num1 - num2}. Try another problem.")
                        wrongAnswers += 1

            except Exception as e:
                print(f"Invalid input: {e}. Please try again.")
                
#-----------------------------------------------------------------------------------------------
# Substitution with Carrying
    
    elif operation == "swc":

        correct = False
        mistakes = 0
        
        while count < totalQuestions:
        # Generate two random numbers where borrowing will definitely happen
            num1 = random.randint(10, 9999)  # Minuend
            num2 = random.randint(1, num1 - 1)  # Subtrahend

            if num1 % 1000 >= num2 % 1000:
                num1 = random.randint(10,9999)
                num2 = random.randint(1,num1 - 1)

            elif num1 % 100 >= num2 % 100:
                num1 = random.randint(10,999)
                num2 = random.randint(1,num1 - 1)
        
        # Ensure borrowing in ones place (for two-digit numbers)
            elif num1 % 10 >= num2 % 10:
                num1 = random.randint(10, 99)  # Regenerate num1 if borrowing in ones is not happening
                num2 = random.randint(1, num1 - 1)
        
        # Ensure borrowing in the tens place if needed
            if num1 >= 100:
                if (num1 // 10) % 10 >= (num2 // 10) % 10:  # Borrowing happens in the tens place
                    num1 = random.randint(100, 999)
                    num2 = random.randint(1, num1 - 1)

        # Ask the player for the answer
            while not correct:

                try:

                    playerAnswer = input(f"Question {count + 1}: {num1} - {num2} = ")
            
                    if playerAnswer.lower() == "restart":
                        count = 0
                        wrongAnswers = 0
                        print("The question set has been reset.")
                        break
                
                    elif playerAnswer.lower() == "end":
                        print(f"Total wrong answers: {wrongAnswers}")
                        quit()
                            
                    
                    elif int(playerAnswer) == (num1 - num2):
                        print("Correct!")
                        count += 1
                        correct = True
                        
                        
                        if count == totalQuestions:
                            print("The question set has been completed!")
                            break

                    else:
                        newAnswer = input("Incorrect! Try Again: ")
                        wrongAnswers += 1
                        mistakes += 1

                        if newAnswer.lower() == "restart":
                            count = 0
                            wrongAnswers = 0
                            print("The question set has been reset.")
                        
                        elif int(newAnswer) == (num1 - num2):
                            count += 1
                            print("Correct")
                            correct = True

                        elif mistakes >= 1:
                            print(f"Incorrect again! The correct answer was {num1 - num2}. Moving to another question.")
                            break
                            
                        else:
                            print(f"Incorrect! The answer was {num1 - num2}. Try another problem.")
                            wrongAnswers += 1

                except Exception as e:
                    print(f"Invalid input: {e}. Please try again.")

#---------------------------------------------------------------------------------------------
# Multiplication
    
    elif operation == "m":
        num1 = random.randrange(0, 100)
        num2 = random.randrange(0, 100)
        correct = False
        mistakes = 0

        while not correct:
            try:
                

                playerAnswer = input(f"Question Number {count + 1}: {num1} x {num2} = ")
                    
                if playerAnswer.lower() == "restart":
                    count = 0
                    wrongAnswers = 0
                    print("The question set has been reset.")

                elif playerAnswer.lower() == "end":
                    count = totalQuestions
                    quit()

                elif int(playerAnswer) == (num1 * num2):
                    print("Correct!")
                    count += 1
                    correct = True
                        
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

                    elif int(newAnswer) == (num1 * num2):
                        count += 1
                        print("Correct!")
                        correct = True

                    elif mistakes >= 1:
                        print(f"Incorrect again! The correct answer was {num1 * num2}. Moving to next question.")
                        count += 1
                        break
                    
                    else:
                        print(f"Incorrect! The answer was {num1 * num2}. Try another problem.")
                        wrongAnswers += 1

            except Exception as e:
                print(f"Invalid input: {e}. Please try again.")
                


#------------------------------------------------------------------------------------------------------------
# Division
    
    elif operation.lower() == "d":
        num1 = random.randrange(0, 1000)
        num2 = random.randrange(0, 100)
        correct = False
        mistakes = 0
        

        remainder = num1 % num2
        num1 -= remainder

        while not correct:
            try:

                playerAnswer = input(f"Question Number {count + 1}: {num1} ÷ {num2} = ")
                    
                if playerAnswer.lower() == "restart":
                    count = 0
                    wrongAnswers = 0
                    print("The question set has been reset.")

                elif playerAnswer.lower() == "end":
                    count = totalQuestions
                    quit()

                elif int(playerAnswer) == (num1 / num2):
                    print("Correct!")
                    count += 1
                    correct = True
                        
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

                    elif int(newAnswer) == (num1 / num2):
                        count += 1
                        print("Correct!")
                        correct = True

                    elif mistakes >= 1:
                        print(f"Incorrect again! The correct answer was {num1 / num2}. Moving to next question.")
                        count += 1
                        break
            
                    else:
                        print(f"Incorrect! The answer was {num1 / num2}. Try another problem.")
                        wrongAnswers += 1

            except Exception as e:
                print(f"Invalid input: {e}. Please try again.")


#---------------------------------------------------------------------------------------------
# Custom Range Multiplication

    elif operation.lower() == "crm":
        num1 = random.randrange(int(lower_range1), int(upper_range1))
        num2 = random.randrange(int(lower_range2), int(upper_range2))
        correct = False
        mistakes = 0

        while not correct:
            try:

                playerAnswer = input(f"Question Number {count + 1}: {num1} x {num2} = ")
                    
                if playerAnswer.lower() == "restart":
                    count = 0
                    wrongAnswers = 0
                    print("The question set has been reset.")

                elif playerAnswer.lower() == "end":
                    count = totalQuestions
                    quit()

                elif int(playerAnswer) == (num1 * num2):
                    print("Correct!")
                    count += 1
                    correct = True
                        
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

                    elif int(newAnswer) == (num1 * num2):
                        count += 1
                        print("Correct!")
                        correct = True

                    elif mistakes >= 1:
                        print(f"Incorrect again! The correct answer was {num1 * num2}. Moving to next question.")
                        count += 1
                        break
            
                    else:
                        print(f"Incorrect! The answer was {num1 * num2}. Try another problem.")
                        wrongAnswers += 1

            except Exception as e:
                print(f"Invalid input: {e}. Please try again.")

#--------------------------------------------------------------------------------------------------------
#Custom Range Division
    elif operation.lower() == "crd":
        num1 = random.randrange(int(lower_range3), int(upper_range3))
        num2 = random.randrange(int(lower_range4), int(upper_range4))
        correct = False
        mistakes = 0

        remainder = num1 % num2
        num1 -= remainder

        while not correct:
            try:

                playerAnswer = input(f"Question Number {count + 1}: {num1} ÷ {num2} = ")
                    
                if playerAnswer.lower() == "restart":
                    count = 0
                    wrongAnswers = 0
                    print("The question set has been reset.")

                elif playerAnswer.lower() == "end":
                    count = totalQuestions
                    quit()

                elif int(playerAnswer) == (num1 / num2):
                    print("Correct!")
                    count += 1
                    correct = True
                        
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

                    elif int(newAnswer) == (num1 / num2):
                        count += 1
                        print("Correct!")
                        correct = True

                    elif mistakes >= 1:
                        print(f"Incorrect again! The correct answer was {num1 / num2}. Moving to next question.")
                        count += 1
                        break
            
                    else:
                        print(f"Incorrect! The answer was {num1 / num2}. Try another problem.")
                        wrongAnswers += 1

            except Exception as e:
                print(f"Invalid input: {e}. Please try again.")



#-------------------------------------------------------------------------------------------------------                
if wrongAnswers > 5:
    print(f"You got a total of {wrongAnswers} questions wrong.")

elif 1 < wrongAnswers <= 5:
    print(f"You got most of the questions right. Only {wrongAnswers} questions were wrong. Good Job!")

elif wrongAnswers == 1:
    print(f"You got most of the questions right. Only {wrongAnswers} question was wrong. Good Job!")
    
elif wrongAnswers == 0:
    print(f"You got all of the questions right. Great Job!")

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

