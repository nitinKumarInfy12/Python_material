# DB API : returns a tuple for each row

# Database                               > Python package
# Firebird (and Interbase)              >  KInterbasDB
# IBM DB2                               > PyDB2
# Informix                               > informixdb
# Ingres                                 >  ingmod
# Microsoft SQL Server                  > pymssql
# MySQL                                 > pymysql
# ODBC                                  > pyodbc
# Oracle                                >  cx_oracle
# PostgreSQL                            >  psycopg
# SAP DB (also known as "MaxDB")        > sapdbapi
# SQLite                                > sqlite3
# Sybase                                > Sybase

# Connecting to a Server
# • Import appropriate library
# • Use connect() to get a database object
# • Specify host, database, username, password
# close() method on the connection object


# =========================Example===========================
import sqlite3
slconn = sqlite3.connect('web_content')


import pymysql
myconn = pymysql.connect (host = "myserver1",
                           user = "adeveloper",
                           passwd = "s3cr3t",
                           db = "web_content")

# make queries, etc. here ...
# myconn.close()


# ===============Creating a Cursor   == using cursor()
# • Cursor is object that can execute SQL statements
# • Several kinds of cursors usually available
# • Other cursors leave data on server, etc.
mycursor = myconn.cursor()



# Executing a Statement   using execute() method
# • Executing cursor sends SQL to server
# • Data not returned until asked for
# • Returns number of lines in result set for queries
# • Returns lines affected for other statements
# Once you have a cursor, you can use it to perform queries, or to execute arbitrary SQL statements via the execute() method.
# The first argument to execute() is a string containing the SQL statement to run

mycursor.execute("select hostname,ostype,user from hostinfo")
mycursor.execute('insert into hostinfo values ("foo",5,"2.6","arch","net",2055,3072,"bob",0)')


# ===============================Fetching Data
# • Use one of the fetch methods from the cursor object
# • Syntax
# ◦ rec = cursor.fetchone()   : returns the next available row from the query results
# ◦ recs = cursor.fetchall()  : returns a tuple of all rows
# ◦ recs = cursor.fetchmany(n) : returns up to n rows. This is useful when the query returns a large number of rows

mycursor.execute("select color, quest from knights where name = 'Robin'")
(color,quest) = mycursor.fetchone()

mycursor.execute("select color, quest from knights")
rows = mycursor.fetchall()

mycursor.execute("select * from huge_table")
while True:
    rows = mycursor.fetchmany(1000)
    if rows == []:
        break
    for row in rows:
        # process row
        print('')


# Example


with sqlite3.connect("../DATA/PRESIDENTS") as s3conn:
    s3cursor = s3conn.cursor()
    # select first name, last name from all presidents
    s3cursor.execute('''select lname, fname from presidents''')
    print("Sqlite3 does not provide a row count\n")

    for row in s3cursor.fetchall():
        print(' '.join(row))


# ============================ Parameterized Statements
# • More efficient updates
# • Use cursor.execute() or cursor.executemany()
# • Use placeholders in query
# • Pass iterable of parameters

# The execute() method takes a query, plus an iterable of VALUES to fill in the placeholders.
# The database manager will only parse the query once, then reuse it for subsequent calls to execute()

# The executemany() method takes a query, and an iterable of ITERABLES. It will call execute() once for each nested iterable

# Different database modules use different placeholders.
# To see what kind of placeholder a module uses, check MODULE.paramstyle.
# Types include 'format', meaning '%s', and 'qmark', meaning '?'

singledata = ("Smith","John","green"),
multidata = [
        ("Smith","John","green"),
        ("Douglas","Sam","pink"),
        ("Robinson","Alberta","blue"),
            ]
query = "insert into people (lname,fname,color) values (%s,%s,%s)"
rows_added = mycursor.execute(query, singledata)
rows_added = mycursor.executemany(query, multidata)



# =============== Placeholders for SQL Parameters
# Python package        >  Placeholder for parameters
# pymysql               >  %s                :with the exception of pymssql the same placeholder is used for all column types
# cx_oracle             > :param_name
# pyodbc                >  ?
# pgdb                  >  %s
# pymssql               >  %d int %s str etc.
# Psychopg              >  %s or %(param_name)s
# sqlite3               >  ?


# example
with sqlite3.connect("../DATA/PRESIDENTS") as s3conn:
    s3cursor = s3conn.cursor()
    party_query = '''select lname, fname from presidents where party = ?'''

for party in 'Federalist', 'Whig':
    print(party)
    s3cursor.execute(party_query, (party,))
    print(s3cursor.fetchall())


# ===============Dictionary Cursors========================================
# DB API returns a tuple for each row whereas dictionary cursor returns a dictionary for each row, where the keys are the column names
# • Indexed by column name
# • Not standardized in the DB API
# • Returns a dictionary for each row, where the keys are the column names

# example ===================================================================
s3conn = sqlite3.connect("../DATA/PRESIDENTS")
# uncomment to make _all_ cursors dictionary cursors
# conn.row_factory = sqlite3.Row
NAME_QUERY = '''select lname, fname from presidents where num < 5'''

cur = s3conn.cursor()
# select first name, last name from all presidents
cur.execute(NAME_QUERY)
for row in cur.fetchall():
    print(row)
    print('-' * 50)

# dictionary cursor
dcur = s3conn.cursor()
# make _this_ cursor a dictionary cursor
dcur.row_factory = sqlite3.Row
# select first name, last name from all presidents
dcur.execute(NAME_QUERY)
for row in dcur.fetchall():
    print(row['fname'], row['lname'])
    print('-' * 50)
# ============================================================================================


# =================Metadata ==================================
# • cursor.description returns tuple of tuples
# • Fields
#    ◦ name
#    ◦ type_code
#    ◦ display_size
#    ◦ internal_size
#    ◦ precision
#    ◦ scale
#   ◦ null_ok

# For non-query statements, cursor.description returns None

# Once a query has been executed, the cursor’s description() method returns information about the query as a tuple of tuples.
# There is one tuple for each column in the query; each tuple contains a tuple of 7 values describing the column.
# For instance, to get the names of the columns, you could say:
names = [ d[0] for d in mycursor.description ]


s3conn = sqlite3.connect("../DATA/PRESIDENTS")
c = s3conn.cursor()
def row_as_dict(cursor):
    '''Generate rows as dictionaries'''
    column_names = [desc[0] for desc in cursor.description]
    for row in cursor.fetchall():
        row_dict = dict(zip(column_names, row))
        yield row_dict

# select first name, last name from all presidents
num_recs = c.execute('''select lname, fname from presidents''')

for row in row_as_dict(c):
    print(row['fname'], row['lname'])



# ========================= Transactions on connection object
# • Transactions allow safer control of updates
# • commit() to save transactions
# • rollback() to discard
# • Default is autocommit off
# • autocommit\=True to turn on

# By default, you must explicitly save your data using connection.commit()

try:
    for info in list_of_tuples:
        mycursor.execute(query,info)
except SQLError:
    s3conn.rollback()
else:
    s3conn.commit()


# =========================Object-relational Mappers (ORM)
# • No SQL required
# • Maps a class to a table
# • All DB work is done by manipulating objects
# • Most popular Python ORMs
#   ◦ SQLAlchemy
#   ◦ Django (which is a complete web framework)

# An Object-relational mapper is a module or framework that creates a level of abstraction above the actual database tables and SQL queries.
# As the name implies, a Python class (object) is mapped to the actual table.

# Instead of querying the database, call a search method on an object representing a table.
# To add a row to the table, create a new instance of the table class, populate it, and call a method like save().
# it can Create a large, complex database system, complete with foreign keys, composite indices,
# and all the other attributes near and dear to a DBA, without writing the first line of SQL.

# there ar 2 ways o use Python ORMs.
# =================One way is to design the database with the ORM.
# To do this, you create a class for each table in the database, specifying the columns with predefined classes from the ORM.
# Then you run an ORM command which executes the queries needed to build the database.
# If you need to make changes, you update the class definitions, and run an ORM command to synchronize the actual DBMS to your classes.

# =====================The second way is to map tables to an existing database.
# You create the classes to match the schemas that have already been defined in the database.
# Both SQLAlchemy and the Django ORM have tools to automate this process.
