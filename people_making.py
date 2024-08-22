from faker import Faker
import csv
import random
import string
fake = Faker()
users = 0
USERSGOAL = 10
alphabet = string.ascii_lowercase + string.digits
domens = ["@yandex.ru", "@mail.ru", "@Gmail.com",
          "@hc.ru", "@r.ru", "@reg.ru", "@sweb.ru"]
with open("users_"+str(USERSGOAL)+".csv", "a", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(
        ("Name", "Surname", "Phone", "Nickname", "Email")
    )
chose = lambda x: random.choice(x)
rint = lambda x, y: random.randint(x, y)
while users < USERSGOAL:
    person = fake.name()
    while ("." in person):
        person = fake.name()
    name, surname = person.split(" ")[:2]
    nums = ''.join([str(rint(0, 9)) for _ in range(10)])
    phone = f'+7-{nums[:3]}-{nums[3:6]}-{nums[6:8]}-{nums[8:]}'
    nickname = ''
    for _ in range(10):
        nickname += chose(alphabet)
    nickname = f"{nickname[:2]}_{nickname[2:]}"
    mail = nickname + chose(domens)
    with open("users_"+str(USERSGOAL)+".csv", "a", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(
            (name, surname, phone, nickname, mail)
        )
    users += 1
