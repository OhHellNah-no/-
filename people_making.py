from faker import Faker
import csv
import random
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h",
            "i", "j", "k", "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u", "v", "w", "x",
            "y", "z"]
domens = ["@yandex.ru", "@mail.ru", "@Gmail.com",
          "@hc.ru", "@r01.ru", "@reg.ru", "@sweb.ru"]
nickname = []
a = 1
mail = ""
fake = Faker()
is_Sur_Name = False
i_name = []
i_Sur_Name = []
phone = ["7"]
name = ""
sur_Name = ""
with open("users_100.csv", "a", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(
        ("Name", "Surname", "Phone", "Nickname", "Email")
    )
while (a < 100):
    person = list(fake.name())
    while (person[2] == "."):
        person = list(fake.name())
    for i in person:
        if (i != " " and is_Sur_Name == False):
            i_name.append(i)
        else:
            is_Sur_Name = True
        if (is_Sur_Name == True and i != " "):
            i_Sur_Name.append(i)
    name = "".join(i_name)
    sur_Name = "".join(i_Sur_Name)
    for _ in range(10):
        phone.append(str(random.randint(0, 9)))
    phone.insert(1, "-")
    phone.insert(5, "-")
    phone.insert(9, "-")
    phone.insert(12, "-")
    phone = "".join(phone)
    for _ in range(9, 19):
        if (random.randint(0, 1) == 0):
            nickname.append(alphabet[random.randint(0, len(alphabet)-1)])
        else:
            nickname.append(str(random.randint(0, 9)))
    nickname.insert(random.randint(1, len(nickname)-2), "_")
    nickname = "".join(nickname)
    mail = nickname + domens[random.randint(0, len(domens)-1)]
    with open("users_1000000.csv", "a", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(
            (name, sur_Name, phone, nickname, mail)
        )
    nickname = []
    mail = ""
    is_Sur_Name = False
    i_name = []
    i_Sur_Name = []
    phone = ["7"]
    name = ""
    sur_Name = ""
    a += 1

