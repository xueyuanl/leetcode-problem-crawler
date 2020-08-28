class Problem(object):
    def __init__(self, name,
                 number=None,
                 acceptance=None,
                 difficulty='',
                 likes=None,
                 dislikes=None,
                 accepted=None,
                 submissions=None,
                 contributor='',
                 companies=[],
                 topic_tags=[],
                 similar_questions=[]):
        self.name = name
        self.number = number
        self.acceptance = acceptance
        self.difficulty = difficulty
        self.likes = likes
        self.dislikes = dislikes
        self.accepted = accepted
        self.submissions = submissions
        self.contributor = contributor
        self.companies = companies
        self.topic_tags = topic_tags
        self.similar_questions = similar_questions
        self.is_paid_only = None

    def set_number(self, _p):
        self.number = _p['question']['questionId']

    def set_is_paid_only(self, _p):
        self.is_paid_only = _p['question']['isPaidOnly']

    def set_difficulty(self, _p):
        self.difficulty = _p['question']['difficulty']

    def set_likes(self, _p):
        self.likes = _p['question']['likes']

    def set_dislikes(self, _p):
        self.dislikes = _p['question']['dislikes']

    def set_topic_tags(self, _p):
        self.topic_tags = [i['name'] for i in _p['question']['topicTags']]


class Topic(object):
    def __init__(self, problems=[]):
        self.problems = problems


class Company(object):
    def __init__(self, problems=[]):
        self.problems = problems
