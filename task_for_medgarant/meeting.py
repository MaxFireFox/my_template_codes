class Meeting:

    def __init__(self, start):
        self.start = start
        self.stop = start
        if self.stop[3] >= "3":
            self.stop = str(int(self.stop[:2])+1) + ":" + str(int(self.stop[3])-3) + self.stop[4]
            if len(self.stop) < 5:
                self.stop = "0" + self.stop
        else:
            self.stop = self.stop[:3] + str(int(self.stop[3]) + 3) + self.stop[4]

    def check_in(self, time):
        return self.start <= time < self.stop

    def dict(self):
        return {
            'start': self.start,
            'stop': self.stop
        }
