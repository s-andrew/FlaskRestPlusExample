from collections import namedtuple

from mimesis.providers import Person as PersonGenerator
from mimesis.enums import Gender

person = PersonGenerator('en')

Person = namedtuple('Person', 'title surname name email username password')

if __name__ == '__main__':
    with open('users.txt', 'w') as file:
        for i in range(20):
            gender = Gender.FEMALE if i % 2 == 0 else Gender.MALE
            person_ = {
                'id': i,
                'title': person.title(gender),
                'surname': person.surname(gender),
                'name': person.name(gender),
                'email': person.email(),
                'username': person.username(),
                'password': person.password()
            }

            file.write(repr(person_))
            file.write('\n')


with open('users.txt') as file:
    users = [eval(row) for row in file.readlines()]

print(users)