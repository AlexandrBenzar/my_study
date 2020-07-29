# -*- coding: utf-8 -*-
class NotNameError(Exception):
    def __str__(self):
        return 'В имени есть цифры!'


class NotEmailError(Exception):
    def __str__(self):
        return 'Ошибка в поле емайл'


class NotAgeError(Exception):
    def __str__(self):
        return 'Ошибка в возрасте'


def check_line_of_data(name, email, age):
    if not name.isalpha():
        raise NotNameError
    elif '@' not in email or '.' not in email:
        raise NotEmailError
    elif not age.isdigit() or not 10 < int(age) < 99:
        raise NotAgeError


file_name = 'registrations.txt'
with open(file_name, 'r', encoding='utf-8') as file:
    for line in file:
        try:
            name, email, age = line.split()

            check_line_of_data(name=name, email=email, age=age)
            with open('registrations_good.log', 'a', encoding='utf-8') as good_file:
                good_file.write(name + ' ' + email + ' ' + str(age) + '\n')

        except (NotNameError, NotEmailError, NotAgeError) as exc:
            with open('registrations_bad.log', 'a', encoding='utf-8') as bad_file:
                bad_file.write(str(exc) + ' ' + line)

            # print(f'{name} {email} {str(age)} Поймано ичключение {exc}')
        except ValueError as vexc:
            with open('registrations_bad.log', 'a', encoding='utf-8') as bad_file:
                bad_file.write('Недостаточно значений ' + str(vexc) + ' ' + line)
            # print(f'{line[:-1]} Поймано исключение. Недостаточно значений, {vexc}')
