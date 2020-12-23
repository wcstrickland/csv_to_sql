import csv
import sqlite3
import time
from tkinter import filedialog


def csv_insert_db():
    """
    procedure to select a CSV file
    cast datatype to each field
    create or select a database
    create a table and insert
    the contents of the csv file into the db.
    :return: None
    """

    # get source file
    save_files = [('csv', '*.csv')]
    source_file = filedialog.askopenfilename(filetypes=save_files, defaultextension=save_files)

    # name destination file
    files = [('database', '*.db')]
    target = filedialog.asksaveasfilename(filetypes=files, defaultextension=files)

    # create connection
    conn = sqlite3.connect(target)
    cursor = conn.cursor()

    # prohibited symbols
    prohibited = [" ", "/", "\\", "%", "$", "#", "@", "!", "(", ")", "-"]

    # input table name
    # try table name with no columns to check if in db already
    # if the name is good we drop the table and add it back with columns later
    while True:
        table_name = input("Please input desired table name: ")
        if not table_name:
            print("Invalid table name")
            continue
        if table_name:
            for char in table_name:
                if char in prohibited:
                    table_name = str(table_name).replace(char, "_")
            try:
                create_query = f"""CREATE TABLE {table_name} (throw_away TEXT)"""
                cursor.execute(create_query)
                break
            except sqlite3.OperationalError:
                print("Table already exists")
                continue

    # establish input choices(SQLite3)
    valid_choices = ["1", "2", "3", "4"]
    choices = {"1": "INTEGER", "2": "REAL", "3": "TEXT", "4": "BLOB"}

    # open csv file. count and create list of headers(properly formatted)
    with open(source_file, 'r') as f:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            counter = 0
            fields = [x for x in line]
            for field in line:
                counter += 1
            break
        # empty list scrub each field for prohibited symbols and add to this list. replace old list at end
        new_fields = []
        for each in fields:
            for letter in each:
                if letter in prohibited:
                    each = str(each).replace(letter, "_")
            new_fields.append(each)
        fields = new_fields

        # cli input of data types
        columns = []
        for column in fields:
            while True:
                user_input = input(f"""
    Data type choices:
        1: Integer
        2: Decimal
        3: Text
        4: Object
        
    Please enter desired data type for {str(column).upper()} field: """)
                if str(user_input) not in valid_choices:
                    print("\nInvalid input. Please choose a listed data type")
                else:
                    columns.append(column + " " + choices[str(user_input)])
                    break

    # format inputs into string to be placed in queries
    columns = ", ".join(columns)
    place_holders = ", ".join(["?" for x in range(counter)])

    # create queries
    insert_query = f"""INSERT INTO {table_name} VALUES({place_holders})"""
    create_query = f"""CREATE TABLE {table_name} ({columns})"""
    drop_table_query = f"DROP TABLE {table_name}"

    # create table(drop placeholder check from before)
    cursor.execute(drop_table_query)
    cursor.execute(create_query)

    # terminal message to indicate runtime and initialize a timer
    print("*" * 80)
    print("Please wait while your table is created :)")
    print("*" * 80)
    start = time.perf_counter()

    # read source file for data and insert each row into db
    with open(source_file, 'r') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        for line in csv_reader:
            data = tuple(line)
            cursor.execute(insert_query, data)

    # terminal message indicating result and time
    stop = time.perf_counter()
    run_time = stop - start
    print(f"Success! your table was created in {run_time:0.6f} seconds")

    # commit and close connection
    conn.commit()
    cursor.close()


if __name__ == '__main__':
    csv_insert_db()
