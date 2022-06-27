def main():
    # opens the password file
    output_file = open("ITWorks_password_log.txt", "r")

    # creates an empty list to store the password logs
    log_list = []

    # creates the password counting variables
    count_pw_too_small = 0
    count_pw_too_large = 0

    # for each line in the output_file:
    for line in output_file:
        # add the line to the log_list
        log_list.append(line)

    # closes the output file
    output_file.close()

    # a for each loop iterating over the log file
    for line in log_list:
        # prints the line to the screen
        print(line, end='')
        # checks if "< 6" is in the line. if it is:
        if '< 6' in line:
            # increment count_pw_too_small
            count_pw_too_small += 1
        else:
            # increment count_pw_too_large
            count_pw_too_large += 1

    print()
    # prints the counts to the screen
    print(f"Passwords too small: {count_pw_too_small}")
    print(f"Passwords too large: {count_pw_too_large}")


main()
