# csv_to_sql


While the final product of **V1csv_to_sql** and **V2csv_to_sql** is ultimately the same, **V2 and V3** are **MUCH** cleaner.


While the custom iteration slicing present in **V2** was the initial desired concept, and an eye opening adventure into custom iteration, the "janky" "seek to end of file and replace comma with semicolon method used in **V1** is considerably faster, especially with large files. For that reason **V3** inherits the overall improved structure of **V2**, but abandons the custom iteration and substitutes **V1's** end seeking behavior.
After becoming more comfortable with generators and property decorators I realized that my initial attempt at this project was a bit of a mess.
Revisiting the program allowed me to:
- Utilize better attribute and method names
- make proper use of property decorators to create "getters/setters"
- clean up mismatched use of print(file=) and X.write()
- Utilize generators to improve memory performance

This program and its subsequent revisitations improved my knowledge in the following areas:
- property decoration
- generator behavior
- context managers
- i/o
- custom iteration(tools, limits, and pitfalls)
- utilizing GUI for file-dialog input
