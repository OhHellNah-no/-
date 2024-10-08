from faker import Faker
import csv
import random
import string

fake = Faker()
USERS_GOAL = 10
alphabet = string.ascii_lowercase + string.digits
domens = ["@yandex.ru", "@mail.ru", "@Gmail.com",
          "@hc.ru", "@r.ru", "@reg.ru", "@sweb.ru"]

rchoiсe = lambda x: random.choice(x)
rint = lambda x, y: random.randint(x, y)


def generation():

    with open(f"users_{USERS_GOAL}.csv", "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(
            ("Name", "Surname", "Phone",
             "Nickname", "Email")
        )

    for _ in range(USERS_GOAL):
        person = fake.name()
        while ("." in person):
            person = fake.name()
        name, surname = person.split(" ")[:2]

        nums = ''.join([str(rint(0, 9))for _ in range(10)])
        phone = f"+7-{nums[:3]}-{nums[3:6]}-{nums[6:8]}-{nums[8:]}"

        nickname = ''
        for _ in range(rint(9, 19)):
            nickname += rchoiсe(alphabet)
        nickname = f"{nickname[:2]}_{nickname[2:]}"

        mail = nickname + rchoiсe(domens)

        with open(f"users_{USERS_GOAL}.csv", "a", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(
                (name, surname, phone, nickname, mail)
            )


if __name__ == "__main__":
    generation()
