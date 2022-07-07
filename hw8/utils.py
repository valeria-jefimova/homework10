import json

from question import Question


def load_questions(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    questions = []
    for item in data:
        text = item['q']
        difficulty = int(item['d'])
        correct_answer = item['a']
        question = Question(text, difficulty, correct_answer)
        questions.append(question)
    return questions


def build_statistics(questions):
    score = 0
    count = 0

    for question in questions:
        if question.is_correct():
            score = score + question.score
            count = count + 1

    return f'Вот и всё!\n'\
           f'Отвечено {count} вопроса из 5\n'\
           f'Набрано баллов: {score}'


"""Вот и всё!
Отвечено 4 вопроса из 10
Набрано баллов: 120"""