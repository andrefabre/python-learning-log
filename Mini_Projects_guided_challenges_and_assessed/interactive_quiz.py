"""
# Purpose: Workshop 3 - Mini Project
# Group Name: Group 14
# Author/s: Andre Fabre & Joshua Williams
# Copyright: August 2025

Create a quiz game in Python that asks the user 10 multiple-choice questions and calculates their final score and percentage. 

"""
countCorrect = 0 # counter; counts number of correct answers
#------------------------------------------------------------------
# Question 1
#------------------------------------------------------------------
question1 = int(input("""
Q1. Which country is known as the “Land of the Rising Sun”?

    1. China
    2. Japan
    3. Thailand
    4. South Korea
    
Lock in your answer (1–4): """))

print(f"\nYour answer: {question1}")
answer1 = 2 # Japan
if answer1 == question1:
    countCorrect += 1
    answer1 = "Correct"
else:
    answer1 = "Incorrect"
#------------------------------------------------------------------
# Question 2
#------------------------------------------------------------------
question2 = int(input("""
Q2. In which year did the Titanic sink?

    1. 1910
    2. 1916
    3. 1914
    4. 1912
    
Choose wisely! Enter 1, 2, 3, or 4: """))

print(f"\nYour answer: {question2}")
answer2 = 4 # 1912
if answer2 == question2:
    countCorrect += 1
    answer2 = "Correct"
else:
    answer2 = "Incorrect"
#------------------------------------------------------------------
# Question 3
#------------------------------------------------------------------
question3 = int(input("""
Q3. Which element has the chemical symbol “K”?

    1. Krypton
    2. Calcium
    3. Potassium
    4. Chromium
    
What’s your pick? (1–4): """))

print(f"\nYour answer: {question3}")
answer3 = 3 # Potassium
if answer3 == question3:
    countCorrect += 1
    answer3 = "Correct"
else:
    answer3 = "Incorrect"
#------------------------------------------------------------------
# Question 4
#------------------------------------------------------------------
question4 = int(input("""
Q4. Who painted “The Persistence of Memory,” featuring melting clocks?

    1. Salvador Dalí
    2. Pablo Picasso
    3. Claude Monet
    4. Vincent van Gogh
    
Time to decide! Type 1–4: """))

print(f"\nYour answer: {question4}")
answer4 = 1 # Salvador Dalí
if answer4 == question4:
    countCorrect += 1
    answer4 = "Correct"
else:
    answer4 = "Incorrect"
#------------------------------------------------------------------
# Question 5
#------------------------------------------------------------------
question5 = int(input("""
Q5. What is the capital city of Canada?

    1. Toronto
    2. Vancouver
    3. Ottawa
    4. Montreal

Step right up! Pick 1, 2, 3, or 4: """))

print(f"\nYour answer: {question5}")
answer5 = 3 # Ottawa
if answer5 == question5:
    countCorrect += 1
    answer5 = "Correct"
else:
    answer5 = "Incorrect"
#------------------------------------------------------------------
# Question 6
#------------------------------------------------------------------
question6 = int(input("""
Q6. Which novel begins with the line, “Call me Ishmael”?

    1. Treasure Island
    2. Moby-Dick
    3. The Old Man and the Sea
    4. Twenty Thousand Leagues Under the Sea
    
The clock’s ticking… choose 1–4: """))

print(f"\nYour answer: {question6}")
answer6 = 2 # Moby-Dick
if answer6 == question6:
    countCorrect += 1
    answer6 = "Correct"
else:
    answer6 = "Incorrect"
#------------------------------------------------------------------
# Question 7
#------------------------------------------------------------------
question7 = int(input("""
Q7. Which planet in our solar system is the hottest?

    1. Mercury
    2. Jupiter
    3. Mars
    4. Venus

Make your move! (1–4): """))

print(f"\nYour answer: {question7}")
answer7 = 4 # Venus
if answer7 == question7:
    countCorrect += 1
    answer7 = "Correct"
else:
    answer7 = "Incorrect"
#------------------------------------------------------------------
# Question 8
#------------------------------------------------------------------
question8 = int(input("""
Q8. In which sport would you perform a “Fosbury Flop”?

    1. Pole Vault
    2. High Jump
    3. Gymnastics
    4. Diving
    
Which will it be? Type 1, 2, 3, or 4: """))

print(f"\nYour answer: {question8}")
answer8 = 2 # High Jump
if answer8 == question8:
    countCorrect += 1
    answer8 = "Correct"
else:
    answer8 = "Incorrect"
#------------------------------------------------------------------
# Question 9
#------------------------------------------------------------------
question9 = int(input("""
Q9. Which river flows through the city of Paris?

    1. Rhine
    2. Thames
    3. Seine
    4. Loire
    
Lock it in now — 1, 2, 3, or 4: """))

print(f"\nYour answer: {question9}")
answer9 = 3 # Seine
if answer9 == question9:
    countCorrect += 1
    answer9 = "Correct"
else:
    answer9 = "Incorrect"
#------------------------------------------------------------------
# Question 10
#------------------------------------------------------------------
question10 = int(input("""
Q10. Which company developed the video game “The Legend of Zelda”?

    1. Sega
    2. Sony
    3. Nintendo
    4. Capcom
    
Your final answer? (1–4): """))

print(f"\nYour answer: {question10}")
answer10 = 3 # Nintendo
if answer10 == question10:
    countCorrect += 1
    answer10 = "Correct"
else:
    answer10 = "Incorrect"

#------------------------------------------------------------------
# End of Questions
#------------------------------------------------------------------

# Display a preview of the attempt, which shows all the questions
# along with whether the answer entered was correct or incorrect

print("\n\nPreview of the Attempt")
print(f"""
 Q1:  {answer1}
 Q2:  {answer2}
 Q3:  {answer3}
 Q4:  {answer4}
 Q5:  {answer5}
 Q6:  {answer6}
 Q7:  {answer7}
 Q8:  {answer8}
 Q9:  {answer9}
 Q10: {answer10}

""")

# Display the final score; countCorrect out of 10
print(f"Final Score: {countCorrect}/10\n")

# Calculate and display percentageCorrect
percentageCorrect = (countCorrect / 10) * 100
print(f"Percentage: {percentageCorrect:.1f}%\n")

# Use percentageCorrect to display performanceMessage
if percentageCorrect == 100:
    performanceMessage = "Excellent! You got everything right!."
elif 80 <= percentageCorrect < 100:
    performanceMessage = "Good job! Keep it up!."
elif 50 <= percentageCorrect < 80:
    performanceMessage = "Not bad, but you can do it better."
else:
    performanceMessage = "Better luck next time! Keep practicing"

print(f"{performanceMessage}\n")