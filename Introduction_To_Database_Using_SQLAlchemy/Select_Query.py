from sqlalchemy import create_engine
from sqlalchemy.sql import select
engine = create_engine('sqlite:///census.sqlite')

# Create a connection on engine
connection = engine.connect()

# Build select statement for census table: stmt
stmt = 'select * from census'

# Execute the statement and fetch the results: results
#fetchall() : will fetch 
results = connection.execute(stmt).fetchall()

# Print results
print(results)

##In sqlAlchemy
#=================================================================================================================

# Import select
from sqlalchemy import Table,select

# Reflect census table via engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Build select statement for census table: stmt
stmt = select([census])

# Print the emitted statement to see the SQL string
print(stmt)

# Execute the statement on connection and fetch 10 records: result
#execute : will execute the statment
#fetchmany(size=----) : will fetch the number of rows mentioned as size in the function parameter
results = connection.execute(stmt).fetchmany(size=10)

# Execute the statement and print the results
print(results)


#=========================================================================================================

   # ResultProxy: The object returned by the .execute() method. It can be used in a variety of ways to get the data returned by the query.
   # ResultSet: The actual data asked for in the query when using a fetch method such as .fetchall() on a ResultProxy.
# Get the first row of the results by using an index: first_row
first_row = results[0]

# Print the first row of the results
print(first_row)

# Print the first column of the first row by accessing it by its index
print(first_row[0])

# Print the 'state' column of the first row by using its name
print(first_row.state)
