from survey import AnonymousSurvey

question = 'What language do you live in?'
# 实例化类并给question传参
language_survey = AnonymousSurvey(question)

language_survey.show_question()
print('Enter q at any time to quit.\n')

while True:
    responses = input('Language:')
    if responses == 'q':
        break
    language_survey.store_response(responses)

print('thank you')
language_survey.show_results()

