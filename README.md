# csv_to_sql


While the final product of **V1csv_to_sql** and **V1csv_to_sql** is ultimately the same, **V1csv_to_sql** is **MUCH** cleaner.
After becoming more comfortable with generators and property decorators I realized that my initial attempt at this project was a bit of a mess.
Revisiting the program allowed me to:
- Utilize better attribute and method names
- make proper use of property decorators to create "getters/setters"
- clean up missmatched use of print(file=) and X.write()
- Utilize generators to improve memroy performance

This program and its subsequent revisitation improved my knowledge in the following areas:
- property decoration
- generator behavior
- context managers
- i/o
- custom iteration(tools, limits, and pitfalls)
- utilizing GUI for filedialog input
