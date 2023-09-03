# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.name = username
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
#
# user1 = User("001", "Angela")
# user2 = User("002", "Saruu")
# user1.follow(user2)
# print(user1.followers)
# print(user1.following)
# print(user2.followers)
# print(user2.following)


from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []
for d in question_data:
    question_bank.append(Question(d["text"], d["answer"]))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")
