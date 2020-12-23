# csv_to_sql

This program prompts the user to select a CSV file and then create a database or select an existing one. It then asks for a table name and prompts the user if the table already exists. Each field header is displayed  to the user via CLI and they select the data type via input options to prevent incompatible data types. After this the table is created and the values are inserted. The user is given visual confirmation and a readout of how long the process took.  The original version simply formatted the CSV file into a SQL script and is retained as there is likely a use case. 


Revisiting the program allowed me to:

- Utilize better attribute and method names
- make proper use of property decorators

This program and its subsequent revisitations improved my knowledge in the following areas:

- property decoration
- generator behavior
- context managers
- i/o
- custom iteration(tools, limits, and pitfalls)
- utilizing GUI for file-dialog input

![alt text](1.png)![alt text](2.png)
![alt text](3.png)![alt text](4.png)
