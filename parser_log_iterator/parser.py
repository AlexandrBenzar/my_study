# -*- coding: utf-8 -*-
from collections import defaultdict


class File:
    def __init__(self, path_to_file):
        self.path = path_to_file
        self.statistic = defaultdict(int)
        self.last_ts = 0

    def __iter__(self):
        self.last_ts = 0
        self.f = open(self.path, 'r', encoding='utf-8')
        return self

    def __next__(self):
        for line in self.f:
            time_stamp, event_type = line[1:17], line[29:32]
            if 'NOK' != event_type:
                continue
            self.statistic[time_stamp] += 1
            if time_stamp != self.last_ts:
                return_ts = self.last_ts
                self.last_ts = line[1:17]
                return return_ts, self.statistic[return_ts]

        if self.statistic:
            return_ts = self.last_ts
            return_nok = self.statistic[self.last_ts]
            self.statistic.clear()
            return return_ts, return_nok
        else:
            self.f.close()
            raise StopIteration


print_events = File('events.txt')

for event in print_events:
    print(event)


