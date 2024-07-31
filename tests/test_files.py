import csv
import pytest
import re

DELIMITER = ';'
FILENAME_FORMAT = 'users_{count}.csv'
TITLES = ['Name', 'Surname', 'Phone', 'Nickname', 'Email']

NAME_PATTERN = re.compile(r'^[A-Z][a-z]*$')
SURNAME_PATTERN = re.compile(r'^[A-Z][a-z]*$')
PHONE_PATTERN = re.compile(r'^\++7-\d{3}-\d{3}-\d{2}-\d{2}$')
NICKNAME_PATTERN = re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9_]*[a-zA-Z0-9]$')
EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9_]*[a-zA-Z0-9]@([a-zA-Z]+\.)+[a-zA-Z]+$')

INCORRECT_NUMBER_FEEDBACK = 'Incorrect number of users in file. Expected {expected}, got {got}'


@pytest.mark.parametrize('users_count', [10000, 50000, 100000, 250000, 500000, 1000000])
def test_users_file(users_count):
    filename = FILENAME_FORMAT.format(count=users_count)
    try:
        with (open(filename, 'r', encoding='utf-8') as file):
            reader = csv.reader(file, delimiter=DELIMITER)
            rows = set()
            assert [title.strip() for title in reader.__next__()], TITLES
            for row in reader:
                row_str = DELIMITER.join(row)
                assert row_str not in rows, f'Found repeated row: "{row_str}"'
                assert len(row) == 5, f'"{row_str}" has incorrect number of columns'
                name, surname, phone, nickname, email = row

                # check with regular expressions
                assert NAME_PATTERN.match(name.strip()), f'Name "{name}" has wrong format'
                assert SURNAME_PATTERN.match(surname.strip()), f'Surname "{surname}" has wrong format'
                assert PHONE_PATTERN.match(phone.strip()), f'Phone "{phone}" has wrong format'
                assert NICKNAME_PATTERN.match(nickname.strip()), f'Nickname "{nickname}" has wrong format'
                assert EMAIL_PATTERN.match(email.strip()), f'Email "{email}" has wrong format'

                rows.add(row_str)

            assert len(rows) == users_count, INCORRECT_NUMBER_FEEDBACK.format(expected=users_count, got=len(rows))

    except FileNotFoundError:
        pytest.fail(f'File {filename} not found')