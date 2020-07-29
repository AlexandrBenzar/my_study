from utils import time_track
import multiprocessing
import os
import numpy as np
from queue import Empty


# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку my_study\multiprocessor_style

class Manager:
    def __init__(self, folder_name, quantity_performers):
        self.folder_name = folder_name
        self.list_of_path = []
        self.quantity_performers = quantity_performers
        self.list_volatility = []
        self.list_zero_volatility = []

    def get_files(self):
        for root, _, files in os.walk(self.folder_name):
            for filename in files:
                path = os.path.join(root, filename)
                self.list_of_path.append(path)
        return self.list_of_path

    def run_performers(self):
        divided_list_of_path = np.array_split(self.get_files(), self.quantity_performers)
        queue_volatility = multiprocessing.Queue(maxsize=4 * self.quantity_performers)
        performers = [CounterVolatility(list_of_path=one_peace, queue=queue_volatility) for one_peace in
                      divided_list_of_path]

        for performer in performers:
            performer.start()

        while True:
            try:
                volatility = queue_volatility.get(timeout=1)
                if volatility[1]:
                    self.list_volatility.append(volatility)
                else:
                    self.list_zero_volatility.append(volatility[0])

            except Empty:
                print(f'В очереди пусто в течении 1 секунды', flush=True)
                if not any(performer.is_alive() for performer in performers):
                    break
        for performer in performers:
            performer.join()

        self.print_data()

    def print_data(self):
        self.list_volatility.sort(key=lambda i: i[1])
        self.list_zero_volatility.sort(key=lambda i: i[0])
        max_volatility = self.list_volatility[-1:-4:-1]
        min_volatility = self.list_volatility[:3]

        print('Максимальная волатильность:')
        for ticket, volatility in max_volatility:
            print(f'{ticket} - {volatility}')

        print('\n' + 'Минимальная волатильность:')
        for ticket, volatility in min_volatility:
            print(f'{ticket} - {volatility}')

        print('\n' + 'Нулевая волатильность:')
        print(', '.join(self.list_zero_volatility))


class CounterVolatility(multiprocessing.Process):
    def __init__(self, list_of_path, queue, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list_of_path = list_of_path
        self.queue = queue

    def run(self):
        list_of_price = []
        for path in self.list_of_path:
            with open(path, 'r') as r_file:
                for line in r_file:
                    secid, _, price, _ = line.split(',')
                    if price.isalpha():
                        continue
                    list_of_price.append(float(price))
                volatility = self.count(list_of_price)
                list_of_price.clear()
                self.queue.put((secid, volatility))

    def count(self, list_of_price):
        max_volatility = max(list_of_price)
        min_volatility = min(list_of_price)
        half_sum = (max_volatility + min_volatility) / 2
        volatility = ((max_volatility - min_volatility) / half_sum) * 100
        return volatility


@time_track
def main():
    manager = Manager(folder_name='trades', quantity_performers=8)
    manager.run_performers()


if __name__ == '__main__':
    main()
