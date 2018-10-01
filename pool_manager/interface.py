from main import number_of_tables

actions_info = {
        'h': '(h)elp on the available commands',
        'd': '(d)isplay the summary on the pool tables',
        'r': '(r)ent a table',
        'c': '(c)lose a table',
        'q': '(q)uit the program'
        }


def intro_message():
    print('Pool Tables Management')
    print('Type (h)elp to list available commands\n')


def poll_user_action():
    while True:
        try:
            action = input('> ')
        except EOFError:
            # Ignore it, we don't want to leave accidentally
            # print() so there's a line break
            print()
            continue

        if action in actions_info:
            return action
        else:
            print('Incorrect input, type h to get help')


def show_help():
    print('Available commands are:')
    for key in sorted(actions_info.keys()):
        print(key + '\t' + actions_info[key])


def get_table():
    while True:
        try:
            number = int(input('Enter the number of the table: '))
        except EOFError:
            # Ignore it, we don't want to leave accidentally
            # print() so there's a line break
            print()
            continue

        if number in range(1, number_of_tables + 1):
            return number
        else:
            print('Incorrect number, there are ' + str(number_of_tables) + ' tables available')


def show_tables(data):
    # timestamp_format gives us string that is 19 characters long, so we should add padding
    # total time elapsed is 9 chars long
    # reserving 6 chars for both number and the cost
    print(
            '{:<6}'.format('No.') +
            '{:<11}'.format('Occupied') +
            '{:<21}'.format('Start') +
            '{:<21}'.format('End') +
            '{:<14}'.format('Total') +
            '{:<6}'.format('Cost')
            )
    for table_info in data:
        print(table_info)


def show_failed_close(number):
    print('Cannot close table ' + str(number) + ', it is free for rent')


def show_failed_rent(number):
    print('Cannot rent the table ' + str(number) + ', it is still occupied')


def show_success_close(number):
    print('Table ' + str(number) + ' was closed successfully')


def show_success_rent(number):
    print('Table ' + str(number) + ' was rented successfully')


