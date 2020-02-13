#!/usr/bin/env python

from dataclasses import asdict, dataclass


@dataclass
class Date:
    """Class for dates"""

    year: int
    month: int
    day: int

    def validate(self) -> None:
        for item in asdict(self):
            if type(item) != int:
                ValueError(
                    "Invalid input type " + item + ": " + str(type(item))
                )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Date):
            return NotImplemented
        if type(other) is type(self) and asdict(other) == asdict(self):
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"{self.year}/{self.month}/{self.day}"


class SmartDate(Date):
    """Class for smarter dates"""

    months_cnt = {
        0: 0,
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    days_mapping = {
        3: "Monday",
        4: "Tuesday",
        5: "Wednesday",
        6: "Thursday",
        0: "Friday",
        1: "Saturday",
        2: "Sunday",
    }

    def day_of_the_week(self) -> str:
        # Get day of week from 2020/1/1

        digits = int(str(self.year)[-2:])

        num_leap_years = digits // 4
        days_prior_months = 0
        for mth in range(0, self.month):
            days_prior_months += self.months_cnt[mth]

        final_days = (
            days_prior_months + num_leap_years + digits * 365 + self.day
        )
        day_of_week = self.days_mapping[final_days % 7]

        return day_of_week


def mystery(x: str) -> str:
    n = len(x)
    if n <= 1:
        return x
    a = x[0 : n // 2]
    b = x[n // 2 : n]
    return mystery(a) + mystery(b)


if __name__ == "__main__":
    x = Date(2020, 2, 11)
    y = Date(2020, 2, 11)
    z = Date(2020, 2, 12)
    assert x == y
    assert not x == z
    assert not x == 1

    smart_date1 = SmartDate(2020, 2, 12)
    smart_date2 = SmartDate(2000, 1, 6)
    assert smart_date1.day_of_the_week() == "Wednesday"
    assert smart_date2.day_of_the_week() == "Thursday"
