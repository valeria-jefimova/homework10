"""
– текст вопроса
– сложность вопроса
– верный вариант ответа

– задан ли вопрос (по умолчанию False)
– ответ пользователя (по умолчанию None)
– баллы за вопрос (вычисляется в момент инициализации)
"""

class Question:

  def __init__(self, text, difficulty, correct_answer):
    self.text = text
    self.difficulty = difficulty
    self.correct_answer = correct_answer

    self.is_asked = False
    self.user_answer = None
    self.score = self.difficulty * 10

  """Возвращает int, количество баллов.
    Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
    """
  def get_points(self):
    return self.score

  """Возвращает True, если ответ пользователя совпадает
    с верным ответов иначе False.
    """
  def is_correct(self):
    return self.user_answer == self.correct_answer

  """Возвращает вопрос в понятном пользователю виде, например:
  Вопрос: What do people often call American flag?
  Сложность 4/5
  """
  def build_question(self):
    return f"Вопрос: {self.text}\n" \
           f"Сложность {self.difficulty}/5"

  """Возвращает :
  Ответ верный, получено __ баллов
  Ответ неверный, верный ответ __
  """
  def build_feedback(self):
    if self.is_correct():
      return f"Ответ верный, получено {self.score} баллов"
    return f"Ответ неверный, верный ответ - {self.correct_answer}"

  """Возвращает :
  Ответ неверный, верный ответ __
  """

