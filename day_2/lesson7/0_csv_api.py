import csv


def csv_reader_print_all_rows():
    # default mode='r'
    with open('filename.txt') as f:
        reader = csv.reader(f, delimeter=',')
        for row in reader:
            print(row)


def csv_writer_write_a_row(mode='w'):
    if mode != 'w' or mode != 'a':
        return

    with open('hopefully_non_existing_file.txt', mode=mode) as f:
        writer = csv.writer(f, delimiter=',')
        first_name = input('Input first name:')
        last_name = input('Input last name: ')
        age = input('Input age:')
        writer.writerow([first_name, last_name, age])


if __name__ == '__main__':
    csv_writer_write_a_row()