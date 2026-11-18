psql -U postgres
>> enter password

createdb <database_name> ///  CREATE DATABASE <database_name>

Destroy a database
dropdb <database_name>

Reset a database
dropdb <database_name> && createdb <database_name>

## Useful basic psql commands
psql <dbname> [<username>]

Starts psql with a connection to dbname. Optionally use another user than current user

In psql:

# \l

List all databases on the server, their owners, and user access levels

# \c <dbname>

Connect to a database named

# \dt

Show database tables

# \d <tablename>

Describe table schema

# \q

Quit psql, return to the terminal

# \?

Get help, see list of available commands