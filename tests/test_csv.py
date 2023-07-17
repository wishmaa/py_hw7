import csv
import os.path
# TODO оформить в тест, добавить ассерты и использовать универсальный путь
csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../resources/eggs.csv'))


def test_csv():
    with open(csv_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])


def test_csv_2():
    with open(csv_path) as opencsv:
        csvreader = csv.reader(opencsv)
    for row in csvreader:
        assert len(row) == 3
    os.remove(csv_path)
