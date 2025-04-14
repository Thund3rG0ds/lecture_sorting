import os
import csv
import numpy

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))

    return data

def selection_sort(number_array, direction="ascending"):
    sorted_array = []
    i = 0
    while i < len(number_array):
        if direction == "ascending":
            sorted_array.insert(i,max(number_array))
            number_array.remove(max(number_array))
        elif direction == "descending":
            sorted_array.insert(i,min(number_array))
            number_array.remove(min(number_array))
        else:
            print("chyba")

    return sorted_array

def main():
    data = read_data("numbers.csv")
    print(data)

    my_array = [4,5,7,6,8]
    print(selection_sort(data["series_1"]))
    print(selection_sort(data["series_2"],"descending"))
    print(selection_sort(data["series_3"]))
    pass


if __name__ == '__main__':
    main()
