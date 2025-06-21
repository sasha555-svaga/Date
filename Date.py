class Date:
    def init(self, day, month, year):
        if month < 1 or month > 12:
            raise ValueError("неправильний місяць (1-12)")
        if day < 1 or day > 31:
            raise ValueError("неправильний день (1-31)")
        self.day = day
        self.month = month
        self.year = year

    def str(self):
        return f"{self.day}.{self.month}.{self.year}"

    def eq(self, other):
        return (self.day, self.month, self.year) == (other.day, other.month, other.year)

    def lt(self, other):
        return (self.year, self.month, self.day) < (other.year, other.month, other.day)

    def is_leap_year(self): #високосний рік
        year = self.year
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        else:
            return year % 400 == 0

if name == "main": #дати
    d1 = Date(15, 5, 2023)
    d2 = Date(20, 5, 2023)

    print(f"дата 1: {d1}")
    print(f"дата 2: {d2}")
    #порівняння
    print(f"d1 < d2: {d1 < d2}")
    print(f"d1 == d2: {d1 == d2}")
    #високосний рік
    leap_date = Date(1, 1, 2020)
    print(f"2020 високосний: {leap_date.is_leap_year()}")