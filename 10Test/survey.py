class AnonymousSurvey:
    def __init__(self, question):
        self.question = question
        self.answers = []

    def show_question(self):
        print(self.question)

    def store_response(self, response):
        self.answers.append(response)

    def show_results(self):
        print(self.answers)
        for response in self.answers:
            print(response)