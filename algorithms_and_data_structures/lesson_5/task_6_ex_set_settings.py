import argparse # работа с ключами в командной строке
from collections import ChainMap


defaults = {'ip': 'localhost', 'port': 7777}

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--ip')
parser.add_argument('-p', '--port')

args = parser.parse_args()  # сохраняем введенные при запуске скрипта агрументы (ключи в key, а значения в val)
# проверяем есть ли значения в args и если есть, то создаем словарб new_dict с этими коючами
new_dict = {key: value for key, value in vars(args).items() if value}

settings = ChainMap(new_dict, defaults)
print(settings['ip'])
print(settings['port'])