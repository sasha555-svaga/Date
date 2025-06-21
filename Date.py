class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        self._validate_date()
        
    def _validate_date(self):
        if self.month < 1 or self.month > 12:
            raise ValueError("Місяць має бути від 1 до 12")
        if self.day < 1 or self.day > 31:
            raise ValueError("День має бути від 1 до 31")

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __eq__(self, other):
        return (self.day, self.month, self.year) == (other.day, other.month, other.year)

    def __lt__(self, other):
        return (self.year, self.month, self.day) < (other.year, other.month, other.day)

    def is_leap_year(self): #високосний рік
        year = self.year
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        else:
            return year % 400 == 0

if __name__ == "__main__": #дати
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
