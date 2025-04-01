import csv
from typing import List


def test() -> List[List[str]]:
    """
    Reads data for a CSV file and returns it as a list of records.

    Each record is represented as a list of strings, with each string corresponding to a field in the CSV file.

    :param file_name: The name of the csv file to be read.
    :return: A list of records, where each record is a list of strings.
    """
    file_name = 'test.csv'
    records = []
    with open('test.csv', 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)

        # skip the header row
        next(csv_reader, None)
        for row in csv_reader:
            records.append(row)
    return records


test()
