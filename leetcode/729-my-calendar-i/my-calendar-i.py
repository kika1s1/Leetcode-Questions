class MyCalendar:

    def __init__(self):
        self.booked = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.booked:
            if start < e and end > s:
                return False
        self.booked.append((start, end))
        return True
