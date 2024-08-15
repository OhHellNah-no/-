from faker import Faker
import csv
import random
import string
fake = Faker()
alphabet = string.ascii_lowercase
domens = ["@yandex.ru", "@mail.ru", "@Gmail.com",
          "@hc.ru", "@r.ru", "@reg.ru", "@sweb.ru"]
with open("users_10000.csv", "a", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(
        ("Name", "Surname", "Phone", "Nickname", "Email")
    )
for _ in range(10000):
    nickname = []
    name = ""
    surname = ""
    person = fake.name()
    while ("." in list(person)):
        person = fake.name()
    person = person.split(" ")
    name = person[0]
    surname = person[1]
    phone = []
    for _ in range(10):
        phone.append(str(random.randint(0, 9)))
    phone.insert(0, "+7")
    phone.insert(1, "-")
    phone.insert(5, "-")
    phone.insert(9, "-")
    phone.insert(12, "-")
    phone = "".join(phone)
    for _ in range(9, 19):
        nickname.append(random.choice(alphabet))
    nickname.insert(random.randint(1, len(nickname)-2), "_")
    nickname = "".join(nickname)
    mail = nickname + random.choice(domens)
    with open("users_10000.csv", "a", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(
            (name, surname, phone, nickname, mail)
        )
