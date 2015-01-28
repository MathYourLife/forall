
class Session(object):
    name = None
    total_count = 0
    correct_count = 0
    notyet_count = 0

    def correct(self):
        self.correct_count += 1
        self.total_count += 1

    def notyet(self):
        self.notyet_count += 1
        self.total_count += 1

    def json(self):
        return {
            'name': self.name,
            'correct': self.correct_count,
            'notyet': self.notyet_count,
            'total': self.total_count,
        }

    def __str__(self):
        return "%s,%d,%d,%d" % (self.name, self.correct_count,
            self.notyet_count, self.total_count)

class Tracker(object):
    def __init__(self, f):
        self.f = f

    def correct(self, session, question):
        self.log(session, question, "correct")

    def notyet(self, session, question):
        self.log(session, question, "notyet")

    def log(self, session, question, status):
        data = {
            'time': time.time(),
            'session': session.json(),
            'q': question.json(),
            'status': status,
        }
        json.dump(data, self.f)
        self.f.write("\n")
        self.f.flush()
