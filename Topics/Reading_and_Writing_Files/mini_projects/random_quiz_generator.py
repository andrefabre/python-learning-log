"""
1. Creates 35 different quizzes
2. Creates 50 multiple choice questions for each quiz, in random order
3. Provides the correct answer and three random wrong answers for each question in random order
4. Writes the quizzes to 35 text files
5. Writes the answer keys to 35 text files

The code will need to do the following:
1. Store the states and capitals in a dictionary
2. Call open(), write(), and close() for the quiz and answer ky text files
3. Use random.shuffle() to randomise the order of the questions and multiple choice questions
"""

#1. Store the Quiz Data in a dict

import random

# The quiz data. Keys are US States and values are their capitals
capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne"
}

# Generate 35 quiz files
for quizNum in range(5):
    # TODO: Create the quiz and answer key files
    quizFile = open(f"capitalsquiz{quizNum + 1}.txt", "w")
    answerKeyFile = open(f"capitalsquiz_answers{quizNum + 1}.txt", "w")
    
    # TODO: Write out the header for the quiz
    quizFile.write("Name:\n\nDate:\n\nPeriod:\n\n")
    quizFile.write((" " * 20) + f"State Capitals Quiz (Form({quizNum + 1}))")
    quizFile.write("\n\n")
    
    # TODO: Shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)
    
    # TODO: Loop through all 50 states, making a question for each.

    for questionNum in range(50):
        
        # get right and wrong answers
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        
        # write the question and the answer options to the quiz file
        quizFile.write(f"{questionNum + 1}. What is the capital of {states[questionNum]}?\n")
        for i in range(4):
            quizFile.write(f"    {"ABCD"[i]}. { answerOptions[i]}\n")
        quizFile.write("\n")
        
        # Write the answer key to a file
        answerKeyFile.write(f"{questionNum + 1}. {"ABCD"[answerOptions.index(correctAnswer)]}")
    
    quizFile.close()
    answerKeyFile.close()
        
# 2. Create the Quiz File and Shuffle the Question Order

