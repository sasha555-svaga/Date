class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        self._validate_date()

    def _validate_date(self):
        if not (1 <= self.month <= 12):
            raise ValueError("місяць має бути від 1 до 12")

        days_in_month = self._days_in_month(self.month)
        if not (1 <= self.day <= days_in_month):
            raise ValueError(f"у місяці {self.month} {self.year} року має бути від 1 до {days_in_month} днів")

    def _days_in_month(self, month):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            return 29 if self.is_leap_year() else 28

    def is_leap_year(self):  # високосний рік
        if self.year % 4 != 0:
            return False
        elif self.year % 100 != 0:
            return True
        else:
            return self.year % 400 == 0

    def __str__(self):
        return f"{self.day:02d}.{self.month:02d}.{self.year}"

    def _ensure_date(self, other):
        if not isinstance(other, Date):
            raise TypeError("операція можлива лише з іншим об'єктом Date")

    def __eq__(self, other):
        self._ensure_date(other)
        return (self.year, self.month, self.day) == (other.year, other.month, other.day)

    def __ne__(self, other):
        self._ensure_date(other)
        return not self == other

    def __lt__(self, other):
        self._ensure_date(other)
        return (self.year, self.month, self.day) < (other.year, other.month, other.day)

    def __le__(self, other):
        self._ensure_date(other)
        return self < other or self == other

    def __gt__(self, other):
        self._ensure_date(other)
        return not self <= other

    def __ge__(self, other):
        self._ensure_date(other)
        return not self < other
if __name__ == "__main__":
    d1 = Date(29, 2, 2024)  # високосний рік
    d2 = Date(28, 2, 2023)  

    print(f"дата 1: {d1}")
    print(f"дата 2: {d2}")
    print(f"d1 < d2: {d1 < d2}")
    print(f"d1 == d2: {d1 == d2}")
    print(f"d1 > d2: {d1 > d2}")
    print(f"d1 != d2: {d1 != d2}")
    print(f"2024 високосний: {d1.is_leap_year()}")
    print(f"2023 високосний: {d2.is_leap_year()}")
