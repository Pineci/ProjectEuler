
class Date:

    def __init__(self, day, month, year, weekday):
        self.day = day
        self.month = month
        self.year = year
        self.weekday = weekday

    def monthString(self):
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        return months[self.month-1]

    def weekdayString(self):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days[self.weekday]

    def leapYear(self):
        return self.year % 400 == 0 or (self.year % 4 == 0 and self.year % 100 != 0)

    def daysInMonth(self):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.month == 2 and self.leapYear():
            return 29
        else:
            return days[self.month-1]


    def nextDay(self):
        self.weekday = (self.weekday + 1) % 7
        if self.day < self.daysInMonth():
            self.day += 1
        else:
            self.day = 1
            if self.month < 12:
                self.month += 1
            else:
                self.month = 1
                self.year += 1

    def __str__(self):
        return self.weekdayString() + ", " + self.monthString() + " " + str(self.day) + " " + str(self.year)

d = Date(1, 1, 1900, 0)
count = 0
while d.year < 2001:
    if d.day == 1 and d.weekday == 6 and d.year >= 1901:
        count += 1
    d.nextDay()
print(count)