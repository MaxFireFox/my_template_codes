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

my_busy = busy.copy()

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
