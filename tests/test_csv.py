import csv
import os.path
# TODO оформить в тест, добавить ассерты и использовать универсальный путь

def test_csv():
    csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../resources/eggs.csv'))
    with open(csv_path, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    with open(csv_path) as csvfile:
        csvreader = csv.reader(csvfile)
    for row in csvreader:
        assert len(row) == 3
    os.remove(csv_path)