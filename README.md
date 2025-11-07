
In the terminal run:

$ sqlite3 db-name.db

then

sqlite>.schema # Shows the tables schema

sqlite>INSERT INTO todos (title, description, priority, complete) VALUES ('Go to store', 'To pick up eggs', 4, False);  # Insert data inside the table

sqlite>SELECT * FROM table_name;

sqlite>.mode column # Shows the table in a different format (other formats are: markdown, box, table)

Freely adapted from:
FastAPI Udemi course