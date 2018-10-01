import json
import os.path

from math import ceil
from datetime import datetime
from table import PoolTable

# Time format is the same everywhere
timestamp_format = '%m-%d-%Y %H:%M:%S'

class PoolTableManager():
    # A class to manage pool tables

    # Give it something to manage first
    # We don't load actual resources here so we can attach a different 
    def __init__(self, pool_tables = list()):
        self.pool_tables = pool_tables


    # Load pool tables data from a file
    # Filenames are strings with the correct filesystem path
    # load_tables() overwrites current table list!
    def load_tables(self, filename):
        with open(filename, 'r') as f:
            pool_tables = list()
            loaded_tables_data = json.load(f)

            for table in loaded_tables_data:
                pool_tables.append(PoolTable(table))
            self.pool_tables = pool_tables


    # Save pool tables data to disk in JSON format
    def save_tables(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.pool_tables, f, default = vars, ensure_ascii = False)


    # Manager logic section
    # All of the tables are addressed by their indices
    # Index = Number of the table - 1

    # Rent a table, returns tables_info() report in case of success, False otherwise
    def rent_table(self, index):
        if not self.pool_tables[index].occupied:
            self.pool_tables[index].occupied = True
            self.pool_tables[index].start_time = datetime.now().strftime(timestamp_format)

            report = self.tables_info()
            return report
        else:
            return False


    # Calculate the cost, returns the current cost if the elapsed time > 0, otherwise returns 0
    def calculate_cost(self, index):
        if self.pool_tables[index].start_time != 0:
            if self.pool_tables[index].end_time != 0:
                end_time = datetime.strptime(self.pool_tables[index].end_time, timestamp_format)
            else:
                end_time = datetime.now()
            total_time = end_time - datetime.strptime(self.pool_tables[index].start_time, timestamp_format)

            # Return 0 in case the time delta is negative
            # Either the player ended session before starting it or you'll have to check your time settings
            if total_time.days < 0:
                return 0
            else:
                cost = ceil(total_time.seconds / 3600) * PoolTable.service_charge
                return cost
        else:
            # The table is free, nothing to calculate
            return 0


    # Close a rented table, returns tables_info() report in case of success, False otherwise
    def close_table(self, index):
        if self.pool_tables[index].occupied:
            end_time = datetime.now().strftime(timestamp_format)
            self.pool_tables[index].end_time = end_time
            self.pool_tables[index].cost = self.calculate_cost(index)

            # Save session info to a separate file in the "Table 1 @ 01-01-1970.json" format
            with open('./Table ' + str(index + 1) + ' @ ' + end_time + '.json', 'w') as f:
                json.dump(vars(self.pool_tables[index]), f, ensure_ascii = False)

            # Save tables info before freeing up the closed table
            report = self.tables_info()

            # Free up the table for another customer
            # The table info is not saved in JSON here, we call save_tables() from the outside (main.py) on demand
            self.pool_tables[index].occupied = False
            self.pool_tables[index].start_time = 0
            self.pool_tables[index].end_time = 0
            self.pool_tables[index].cost = 0

            return report

        else:
            return False


    # Returns time elapsed in the range between start time and end time, returns 0 if start > end
    def elapsed_time(self, start_time, end_time = datetime.now()):
            # Subtract start time from the current time
            # Start time must be a formatted string, end time is converted if it's a string

            if type(start_time) is not str:
                return '0s'

            if type(end_time) is str:
                end_time = datetime.strptime(end_time, timestamp_format)
            else:
                if end_time is not datetime:
                    end_time = datetime.now()

            time_delta = end_time - datetime.strptime(start_time, timestamp_format)
            if time_delta.days < 0:
                return 0
            else:
                elapsed = '{0}h {1}m {2}s'.format(time_delta.seconds // 3600, time_delta.seconds // 60 % 60, time_delta.seconds % 60)
                return elapsed


    # Display table information, returns list of tabulated strings each containing corresponding table info
    def tables_info(self,):
        report = list()

        # Recalculate the cost for each table separately
        for idx in range(len(self.pool_tables)):
            self.pool_tables[idx].cost = self.calculate_cost(idx)

        for table in self.pool_tables:
            # timestamp_format is 19 characters long and elapsed_time is 9 chars long
            report.append(('{number:<6}{occupied:<11}{start:<21}{end:<21}{elapsed:<14}${cost:<6}').format(
                    number = table.number,
                    occupied = table.occupied and 'Yes' or 'No',
                    start = table.start_time,
                    end = table.end_time,
                    elapsed = self.elapsed_time(table.start_time, table.end_time),
                    cost = table.cost
                    )
            )
        return report


def init_table_manager(number_of_tables, state_file):
    manager = PoolTableManager()
    if os.path.exists(state_file):
        print("Using existing pool tables info from " + state_file)
        manager.load_tables(state_file)
    else:
        # Creating and numbering the tables
        print('Pool tables info is missing, creating it...')

        # The index of each new table corresponds to its number + 1
        for idx in range(number_of_tables):
            manager.pool_tables.append(PoolTable())
            manager.pool_tables[idx].number = idx + 1
        manager.save_tables(state_file)
    return manager
