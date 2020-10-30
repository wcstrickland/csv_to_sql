import csv
import itertools
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


class CsvSQL(object):

    def __init__(self, read_file, write_file, table_name):
        self.read_file = read_file
        self.write_file = write_file
        self.table_name = str(table_name)

    @staticmethod
    def clean(key):
        key = key.replace(" ", "_")
        key = key.replace("<", "less_than")
        key = key.replace(">", "greater_than")
        key = key.strip("_")
        key = key.replace("(", '')
        key = key.replace(")", '')
        return key

    @property
    def line_count(self):
        count = 0
        with open(self.read_file, 'r') as f:
            csv_reader = csv.DictReader(f)
            for line in csv_reader:
                count += 1
            return count

    @property
    def header_count(self):
        count = 0
        with open(self.read_file, 'r') as f:
            csv_reader = csv.DictReader(f)
            first_row = itertools.islice(csv_reader, 0, 1)
            for row in first_row:
                for key in row:
                    count += 1
            return count

    @property
    def get_headers(self):
        with open(self.read_file, 'r') as f:
            csv_reader = csv.DictReader(f)
            first_row = itertools.islice(csv_reader, 0, 1)
            for row in first_row:
                for key in row:
                    clean_key = CsvSQL.clean(key)
                    yield clean_key

    @property
    def get_values(self):
        with open(self.read_file, 'r') as f:
            csv_reader = csv.DictReader(f)
            for line in csv_reader:
                yield tuple(line.values())

    def get_statement(self):
        with open(self.write_file, 'w') as wf:
            print(f"CREATE TABLE {self.table_name}", "(", file=wf)
            for header in itertools.islice(self.get_headers, 0, self.header_count - 1):
                print(header, " TYP ,", file=wf)
            for header in itertools.islice(self.get_headers, self.header_count - 1,
                    self.header_count):
                print(header, " TYP );", file=wf)
            print(f"\nINSERT INTO {self.table_name} \nVALUES", file=wf)
            for value in itertools.islice(self.get_values, 0, self.line_count - 1):
                print(str(value) + ",\n", end='', file=wf)
            for value in itertools.islice(self.get_values, self.line_count - 1,
                    self.line_count):
                print(str(value) + ";", end='', file=wf)


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

    file = CsvSQL(source_file, target, t_name)  # create object
    file.get_statement()  # call method
