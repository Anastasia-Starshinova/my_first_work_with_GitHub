from random import *

quantity_of_password_new, length_of_password_new = "количество паролей", "длину пароля"
actual_name = ""
digit = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_."

print("Привет!")


def return_number(actual_name):
    print("Укажите", actual_name, "для генерации")
    quantity = input()
    if quantity.isdigit():
        print("Супер!")
        return int(quantity)
    elif not quantity.isdigit():
        print("Пожалуйста, введите ", actual_name, " в виде цифры", "\n",
              "Например: 2", sep="")
        quantity = input()
        if quantity.isdigit():
            print("Молодец!")
            return int(quantity)
        elif not quantity.isdigit():
            print("К сожалению, вы не ввели", actual_name, "как было указано, начинаем заново")
            return return_number(actual_name)


count_of_password = return_number(quantity_of_password)
len_of_password = return_number(length_of_password)

print("Количество паролей = ", count_of_password, "\n", "Длина пароля = ", len_of_password, sep="")

filling_in_the_password = []


def generate_password():

    number_of_entered_yes = 0
    while number_of_entered_yes <= len_of_password:

        print("Включать ли цифры: ", digit, " . Напиши 'да' или 'нет'", sep="")
        answer_for_digit = input()
        if answer_for_digit.lower() == "да" and number_of_entered_yes < len_of_password:
            number_of_entered_yes += 1
            filling_in_the_password.append(digit)
            if len(filling_in_the_password) < len_of_password:
                print("Осталось набрать ещё ", len_of_password - len(filling_in_the_password), " символов", sep="")
            else:
                break

        print("Включать ли прописные буквы: ", uppercase_letters, " . Напиши 'да' или 'нет'", sep="")
        answer_for_uppercase_letters = input()
        if answer_for_uppercase_letters.lower() == "да" and number_of_entered_yes < len_of_password:
            number_of_entered_yes += 1
            filling_in_the_password.append(uppercase_letters)
            if len(filling_in_the_password) < len_of_password:
                print("Осталось набрать ещё ", len_of_password - len(filling_in_the_password), " символов", sep="")
            else:
                break

        print("Включать ли строчные буквы: ", lowercase_letters, " . Напиши 'да' или 'нет'", sep="")
        answer_for_lowercase_letters = input()
        if answer_for_lowercase_letters.lower() == "да" and number_of_entered_yes < len_of_password:
            number_of_entered_yes += 1
            filling_in_the_password.append(lowercase_letters)
            if len(filling_in_the_password) < len_of_password:
                print("Осталось набрать ещё ", len_of_password - len(filling_in_the_password), " символов", sep="")
            else:
                break

        print("Включать ли символы: ", punctuation, " . Напиши 'да' или 'нет'", sep="")
        answer_for_punctuation = input()
        if answer_for_punctuation.lower() == "да" and number_of_entered_yes < len_of_password:
            number_of_entered_yes += 1
            filling_in_the_password.append(lowercase_letters)
            if len(filling_in_the_password) < len_of_password:
                print("Осталось набрать ещё ", len_of_password - len(filling_in_the_password), " символов", sep="")
            else:
                break

    print(len_of_password, "\n", filling_in_the_password, sep = "")
    return filling_in_the_password


generate_password()

final_password = []
for i in range(count_of_password):
    new_password = ""
    for x in filling_in_the_password:
        new_password += choice(x)
    final_password.append(new_password)

# print("Ваши пароли готовы:", "\n", *final_password, sep="")
print("Ваши пароли готовы:", "\n", ", ".join(final_password), sep="")
