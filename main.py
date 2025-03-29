from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    session = db_session.create_session()

    user1 = User()
    user1.surname = 'Scott'
    user1.name = 'Ridley'
    user1.age = 21
    user1.position = 'captain'
    user1.speciality = 'research engineer'
    user1.address = 'module_1'
    user1.email = 'scott_chief@mars.org'
    user1.hashed_password = "cap"
    user1.set_password(user1.hashed_password)
    session.add(user1)

    user2 = User()
    user2.surname = 'Johnson'
    user2.name = 'Emily'
    user2.age = 28
    user2.position = 'navigator'
    user2.speciality = 'astrogation, orbital mechanics'
    user2.address = 'module_2'
    user2.email = ' johnson.emily@mars.org'
    user2.hashed_password = "navi"
    user2.set_password(user2.hashed_password)
    session.add(user2)

    user3 = User()
    user3.surname = 'Ramirez'
    user3.name = 'Carlos'
    user3.age = 36
    user3.position = 'chief medical officer'
    user3.speciality = 'aerospace medicine, surgery'
    user3.address = 'module_3'
    user3.email = 'ramirez_cmo@mars.org'
    user3.hashed_password = "medic"
    user3.set_password(user3.hashed_password)
    session.add(user3)

    user4 = User()
    user4.surname = 'Johanssen'
    user4.name = 'Beth'
    user4.age = 28
    user4.position = 'systems operator'
    user4.speciality = 'computer engineer'
    user4.address = 'module_2'
    user4.email = 'johanssen_systems@mars.org'
    user4.hashed_password = "sys_operator"
    user4.set_password(user4.hashed_password)
    session.add(user4)

    session.commit()


if __name__ == '__main__':
    main()
