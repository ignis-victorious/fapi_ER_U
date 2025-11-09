
NB SQLAlchemy grammar has somewhat changed. Here a quick update:
[How to Use SQLAlchemy in 2025 Pretty Printed](https://www.youtube.com/watch?v=Y-TxICRUy_k)

Some errors picked up:
1. Import Error
Use:
from . import models
Insteaf of:
import models
2. 


In the terminal run:

$ sqlite3 db-name.db
Alternatively use:
$ sqlite3
then
$ sqlite>.open FILENAME"  # to reopen on a persistent database.

then

sqlite>.schema # Shows the tables schema

sqlite>INSERT INTO todos (title, description, priority, complete) VALUES ('Go to store', 'To pick up eggs', 4, False);  # Insert data inside the table

sqlite>SELECT * FROM table_name;

sqlite>.mode column # Shows the table in a different format (other formats are: markdown, box, table)

sqlite> DELETE FROM todos WHERE id = 4;

Freely adapted from:
FastAPI Udemi course