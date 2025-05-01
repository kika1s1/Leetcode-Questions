class MyCalendarTwo:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        self.events.append((start, 1))
        self.events.append((end, -1))
        self.events.sort()

        active_events = 0
        for _, event_type in self.events:
            active_events += event_type
            if active_events >= 3:
                self.events.remove((start, 1))
                self.events.remove((end, -1))
                return False

        return True
