from meeting import Meeting

busy = [
    {
        'start': '10:30',
        'stop': '10:50'
    },
    {
        'start': '18:40',
        'stop': '18:50'
    },
    {
        'start': '14:40',
        'stop': '15:50'
    },
    {
        'start': '16:40',
        'stop': '17:20'
    },
    {
        'start': '20:05',
        'stop': '20:20'
    }
]


def to_stand(str_time: str) -> str:
    """
    Turns string format time to "hh:mm" standard in case input is "h:mm"
    :param str_time: string format time input
    :return: "hh:mm" standard string format time
    """
    if len(str_time) == 4:
        return "0"+str_time
    return str_time


my_busy = [{'start': to_stand(x['start']), 'stop': to_stand(x['stop'])} for x in busy]

my_busy.sort(key=lambda x: x['start'])

all_meetings = []
start = "09:00"

while start <= "20:30":
    meeting = Meeting(start)
    if my_busy and meeting.check_in(my_busy[0]['start']):
        start = my_busy[0]['stop']
        my_busy.pop(0)
    else:
        all_meetings.append(meeting.dict())
        start = meeting.stop

for i, meeting in enumerate(all_meetings):
    print(f"Meeting #{i + 1}: from {meeting['start']} till {meeting['stop']}")
