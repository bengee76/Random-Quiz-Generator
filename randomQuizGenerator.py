import random
import os

#quiz data should be formatted like this
pairs = {
    'Mazowieckie': 'Warszawa',
    'Opolskie': 'Opole',
    'Podkarpackie': 'Rzeszów',
    'Podlaskie': 'Białystok',
}

def doAnswers(pairs):
    keyList = list(pairs.keys())
    characters = ["A", "B", "C", "D"]
    characterList = []
    random.shuffle(keyList)
    for _ in range(len(pairs)):
        characterList.append(random.choice(characters))
    return keyList, characterList, characters

def saveQuiz(keyList, characterList, possibilities, characters, pairs, dir, index):
    fileName = f"Quiz_{index+1}.txt"
    filePath = os.path.join(dir, fileName)
    with open(filePath, "w") as file:
        file.write("Quiz: U.S. states and thier capitals.\n\n") #Quiz name
        for i in range(len(keyList)):
            possible_answers = possibilities.copy()
            correct_answer = pairs[keyList[i]]
            possible_answers.remove(correct_answer)
            random.shuffle(possible_answers)
            file.write(f"\n{i+1}. {keyList[i]}:\n\n")
            for x in range(len(characters)):
                if characterList[i] == characters[x]:
                    file.write(f"{characters[x]}. {correct_answer}\n")
                else:
                    file.write(f"{characters[x]}. {possible_answers.pop()}\n")

def saveAnswers(characterList, dir, index):
    fileName = f"QuizAnswer_{index+1}.txt"
    filePath = os.path.join(dir, fileName)
    with open(filePath, "w") as file:
        for i in range(len(characterList)):
            file.write(f"{i+1}. {characterList[i]}\n")

home_dir = os.path.expanduser("~")
main_dir = os.path.join(home_dir, "RandomQuiz")
answers_dir = os.path.join(main_dir, "answers")
quiz_dir = os.path.join(main_dir, "tests")

for directory in [main_dir, answers_dir, quiz_dir]:
    os.makedirs(directory, exist_ok=True)
print(f"Directory '{os.path.basename(main_dir)}' was created in your user directory.")

possibilities = list(pairs.values())

for i in range(10): #specify amount of quizzes
    keyList, characterList, characters = doAnswers(pairs)
    saveQuiz(keyList, characterList, possibilities, characters, pairs, quiz_dir, i)
    saveAnswers(characterList, answers_dir, i)

print("Quizzes and Answers saved in RandomQuiz directory.")