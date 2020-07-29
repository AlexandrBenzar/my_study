# -*- coding: utf-8 -*-
from collections import defaultdict
from operator import itemgetter
from abc import ABC, abstractmethod


class FileReader(ABC):
    def __init__(self, file_name):
        self.file_name = file_name
        self.statistic = defaultdict(int)

    def read_file(self):
        with open(self.file_name, 'r', encoding='utf-8') as file:
            for line in file:
                time_stamp, event_type = self.parse_line(line=line)
                if 'NOK' in event_type:
                    self.statistic[time_stamp] += 1

    def write_in_file(self):
        list_statistic = sorted(self.statistic.items(), key=itemgetter(0))
        print(list_statistic)
        with open('file_result.txt', 'w', encoding='utf-8') as file:
            for time, quantity in list_statistic:
                file.write(f'[{time}] {str(quantity)} \n')

    @abstractmethod
    def parse_line(self, line):
        pass


class QuantityPerMinute(FileReader):
    def parse_line(self, line):
        return line[1:17], line[29:32]


class QuantityPerHour(FileReader):
    def parse_line(self, line):
        return line[1:14], line[29:32]


class QuantityPerDay(FileReader):
    def parse_line(self, line):
        return line[1:11], line[29:32]


class QuantityPerYear(FileReader):
    def parse_line(self, line):
        return line[1:5], line[29:32]


file_read = QuantityPerHour(file_name='events.txt')
file_read.read_file()
file_read.write_in_file()


