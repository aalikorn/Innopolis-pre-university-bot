class Variables:
    def __init__(self):
        self.current_question = 0
        self.points = 0
        self.questions = None
        self.topic = None
        self.max_points = 0

    def to_dict(self):
        return {
            'current_question': self.current_question,
            'points': self.points,
            'questions': self.questions,
            'topic': self.topic,
            'max_points': self.max_points
        }

    @staticmethod
    def from_dict(data):
        obj = Variables()
        obj.current_question = data['current_question']
        obj.points = data['points']
        obj.questions = data['questions']
        obj.topic = data['topic']
        obj.max_points = data['max_points']
        return obj

