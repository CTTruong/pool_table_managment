from datetime import datetime

import tablemanager
import interface

state_file = './' + datetime.now().strftime('%m-%d-%Y') + '.json'
number_of_tables = 12

if __name__ == '__main__':
    interface.intro_message()

    manager = tablemanager.init_table_manager(number_of_tables, state_file)

    quit = False
    while not quit:
        action = interface.poll_user_action()

        # Incorrect action input is handled in the interface
        if action == 'h':
            interface.show_help()

        elif action == 'd':
            interface.show_tables(manager.tables_info())

        elif action == 'r':
            number = interface.get_table()
            # Subtracting 1 because index is number - 1
            output = manager.rent_table(number - 1)
            if not output:
                interface.show_failed_rent(number)
            else:
                interface.show_success_rent(number)
                interface.show_tables(output)
                # Save changes to disk
                manager.save_tables(state_file)

        elif action == 'c':
            number = interface.get_table()
            # Subtracting 1 because index is number - 1
            output = manager.close_table(number - 1)
            if not output:
                interface.show_failed_close(number)
            else:
                interface.show_success_close(number)
                interface.show_tables(output)
                # Save changes to disk
                manager.save_tables(state_file)

        elif action == 'q':
            manager.save_tables(state_file)
            quit = True

        else:
            print("You must be bored so much to get this output...")
