
import datetime


def main():
    MIN_PASSWORD_LEN = 6
    MAX_PASSWORD_LEN = 10

    input_file = open("password_log.txt", "a")

    password = input("Enter password: ")

    password_length = len(password)

    while password_length < MIN_PASSWORD_LEN or password_length > MAX_PASSWORD_LEN:
        if len(password) < MIN_PASSWORD_LEN:
            input_file.write(f"{datetime.datetime.today()}, password < 6\n")
        if len(password) > MAX_PASSWORD_LEN:
            input_file.write(f"{datetime.datetime.today()}, password > 10\n")

        print("Password not correct length of six to ten characters.")

        password = input("Enter password: ")
        password_length = len(password)

    if password.isalpha():
        strength = "password weak - only contains letters"
    elif password.isnumeric():
        strength = "password weak - only contains numbers"
    else:
        strength = "Password strong"

    print(f"Password length: {len(password)}")
    print(strength)

    input_file.close()

    read_file()


def read_file():
    output_file = open("password_log.txt", "r")

    log_list = []

    count_pw_too_small = 0
    count_pw_too_large = 0

    for line in output_file:
        log_list.append(line)

    output_file.close()

    for line in log_list:
        print(line, end='')
        if '< 6' in line:
            count_pw_too_small += 1
        else:
            count_pw_too_large += 1

    print()
    print(f"Passwords too small: {count_pw_too_small}")
    print(f"Passwords too large: {count_pw_too_large}")


main()
