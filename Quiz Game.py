import requests
from random import shuffle


# menu
def menu():
    category = int(input('''
    Select the subject: -
    1. Computer Science
    2. Vehicles
    3. Mathematics
    '''))

    difficulty = int(input('''
    Difficulty: -
    1. Easy
    2. Medium
    3. Hard
    '''))

    if category in range(1, 4):
        categories = {1: 18, 2: 28, 3: 19}
        category = categories[category]
    else:
        category = -1

    if difficulty in [1, 2]:
        difficulties = {1: 'easy', 2: 'medium'}
        difficulty = difficulties[difficulty]
    else:
        difficulty = 'hard'

    fetch_data(category, difficulty)


# fetch data from the server
def fetch_data(category, difficulty):
    if category == -1:
        url = f"https://opentdb.com/api.php?amount=10&difficulty={difficulty}&type=multiple"
    else:
        url = f"https://opentdb.com/api.php?amount=10&category={category}&difficulty={difficulty}&type=multiple"
    data = requests.get(url)
    extract_data(data.json())


# to extract and arrange data from the url
def extract_data(test_data):
    all_questions = []
    all_options = []
    all_correct = []

    for result in test_data['results']:
        all_questions.append(result['question'])
        all_correct.append(result['correct_answer'])
        options = []
        options.append(result['correct_answer'])
        options.extend(result['incorrect_answers'])
        shuffle(options)
        all_options.append(options)

    conduct_test(all_questions, all_options, all_correct)


# display questions and receive answers
def conduct_test(all_questions, all_options, all_correct):
    user_answers = []
    for i in range(len(all_questions)):
        print(chr(i + 65), '. ', all_questions[i], sep='')
        for j in range(len(all_options[i])):
            print('     ', j+1, '. ', all_options[i][j], sep='')
        user_answers.append(int(input('     Choose the correct option (1/2/3/4) = ')))
    check_answers(user_answers, all_correct, all_options)


# to check the answers
def check_answers(user_answers, all_correct, all_options):
    result = {'correct': 0, 'incorrect': 0}
    for i in range(len(user_answers)):
        if all_correct[i] == all_options[i][user_answers[i]-1]:
            result['correct'] += 1
        else:
            result['incorrect'] += 1
    print(result)
    final_result(result)


def final_result(result):
    marks = result['correct'] * 3 - result['incorrect'] * 1
    print("Marks Obtained: ", marks)


menu()