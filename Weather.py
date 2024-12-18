import GlobalLists
import random


class WeatherCalendar:
    dayList = []

    def __init__(self, climate: str, month: str, first: int, final: int):
        self.climate = climate
        self.month = month
        self.first = first
        self.final = final

    def setDayList(self):
        self.dayList = []
        r = range(self.first, self.final + 1)
        weathType = random.randint(0, len(GlobalLists.WEATHER_DICT[self.climate.upper()]["WEATHER"]) - 1)
        dCount = 0

        for d in r:
            if random.randint(0, 9) >= 6: weathType = random.randint(0, len(GlobalLists.WEATHER_DICT[self.climate.upper()]["WEATHER"]) - 1)
            newDay = "Day " + str(self.first + dCount) + " of " + self.month + ": " + GlobalLists.WEATHER_DICT[self.climate.upper()]["WEATHER"][weathType]
            self.dayList.append(newDay)
            dCount += 1

    def printDayList(self):
        dayString = "Weather from days " + str(self.first) + " through " + str(self.final) + " of " + self.month + ":\n"

        for d in self.dayList:
            dayString = dayString + "- " + d + "\n"

        return dayString

