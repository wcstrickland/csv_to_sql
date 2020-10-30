import csv
import itertools
import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


class InsertStatement(object):
    """
    a class with methods for converting a csv file into an SQL insert statement
    """

    def __init__(self, read_file, write_file, table_name):

        self.read_file = read_file
        self.reader = self.open_csv()
        self.write_file = write_file
        self.table_name = str(table_name)
        self.header_columns_list = self.get_headers()
        self.values_list = self.get_values()

    def open_csv(self):
        """
        opens a csv file with a csv reader.dict_reader and returns the open file
        :return:
        """
        with open(self.read_file, 'r') as f:
            csv_reader = csv.DictReader(f)
            return csv_reader

    def get_headers(self):
        """
        slices the first line of a csv file to create field names for an sql statement
        also attempts to scrub them of symbols incompatible with SQL
        :return: a list of 'headers'
        """
        with open(self.read_file, 'r') as f:
            csv_reader = csv.DictReader(f)
            first_row = itertools.islice(csv_reader, 0, 1)
            self.header_columns_list = []
            for row in first_row:
                for key in row:
                    clean_key = key.replace(" ", "_")
                    clean_key = clean_key.replace("<", "less_than")
                    clean_key = clean_key.replace(">", "greater_than")
                    clean_key = clean_key.strip("_")
                    self.header_columns_list.append(clean_key + " " + "TYP " + ",")
            return self.header_columns_list

    def del_trailing(self, places=-1):
        """
        opens a file in binary write mode and seeks to the end of
        the file deleting the last 'n' places
        :param places: number of places deleted from end of file
        :return:
        """
        with open(self.write_file, 'rb+') as g:
            g.seek(places, os.SEEK_END)
            g.truncate()

    def get_values(self):
        """
        reads the lines of a csv file creating a list of tuples of each line
        :return: list of tuples
        """
        with open(self.read_file, 'r') as f:
            csv_reader = csv.DictReader(f)
            self.values_list = []
            for line in csv_reader:
                self.values_list.append(tuple(line.values()))
            return self.values_list

    def construct_statement(self):
        """
        formats an sql statement and writes it to a text file
        :return: none
        """
        with open(self.write_file, 'w') as wf:
            print("CREATE TABLE {}".format(self.table_name), "(", file=wf)
            for header in self.header_columns_list:
                wf.write(header + "\n")
        self.del_trailing(-3)
        with open(self.write_file, 'a') as wf:
            print(");\nINSERT INTO {} \nVALUES".format(self.table_name), file=wf)
            for value in self.values_list:
                wf.write(str(value) + ",\n")
        self.del_trailing(-3)
        with open(self.write_file, 'a') as wf:
            print("\n;", file=wf)


if __name__ == '__main__':

    def generate():
        """
        called by tkinter button to return text value in entry box to the main as a
        variable. Also `quits` the main loop.
        :return: entry box string value
        """
        try:
            value = str(table.get())
            root.quit()
            return value
        except ValueError:
            pass


    # ############# ROOT WINDOW
    root = Tk()
    root.title("table name")
    root.geometry('150x100+900+500')
    root['padx'] = 20
    # ############# MAIN FRAME
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    # ############# TABLE NAME TEXT ENTRY
    table = StringVar()
    table_entry = ttk.Entry(mainframe, width=13, textvariable=table)
    table_entry.grid(column=0, row=1, sticky=(W, E))
    # ############# 'CONFIRM' BUTTON
    ttk.Button(mainframe, text="generate", command=generate).grid(column=0, row=2,
        sticky=W)
    ttk.Label(mainframe, text="table name").grid(column=0, row=0, sticky=W)
    # ############# MAINFRAME PADDING
    for child in mainframe.winfo_children():
        child.grid_configure(padx=10, pady=5)
    # ############# SET FOCUS OF WIDGET BIND RETURN KEY TO FUNCTION CALL
    table_entry.focus()
    root.bind("<Return>", generate)
    # ############# MAINLOOP
    root.mainloop()

    t_name = str(generate())  # table name variable from entry box
    source_file = filedialog.askopenfilename()  # original file open
    files = [('text', '*.txt')]  # file definitions for asksaveasfilename
    target = filedialog.asksaveasfilename(filetypes=files, defaultextension=files)  #
    # target filename assignment

    file = InsertStatement(source_file, target, t_name)  # create object
    file.construct_statement()  # call method
