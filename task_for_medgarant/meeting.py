"""
    This class has objects start and stop -- string depicting start and finish of the meeting

    It also has methods:
    * check_in -- whether certain time is inside the time interval of the meeting or not
    * dict -- returns dictionary of objects of this class instance
"""


class Meeting:

    def __init__(self, start: str):
        """
        Gets str format start time of the meeting as input, creates stop time according to the task
        (30 min later), also in str format
        :param start: string for meeting start time
        """

        self.start = start
        self.stop = start
        if self.stop[3] >= "3":
            self.stop = str(int(self.stop[:2])+1) + ":" + str(int(self.stop[3])-3) + self.stop[4]
            if len(self.stop) < 5:
                self.stop = "0" + self.stop
        else:
            self.stop = self.stop[:3] + str(int(self.stop[3]) + 3) + self.stop[4]

    def check_in(self, time: str):
        """
        Checks whether certain time is inside the time interval of the meeting or not
        :param time: string for the time we check
        :return: boolean answer
        :rtype bool
        """

        return self.start <= time < self.stop

    def dict(self):
        """
        Returns dictionary of objects of this class instance
        :return: dictionary of start and stop time
        :rtype dict
        """
        return {
            'start': self.start,
            'stop': self.stop
        }
