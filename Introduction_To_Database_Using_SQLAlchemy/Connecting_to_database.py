from sqlalchemy import create_engine
#Creating a engine
engine=create_engine('Database link') #'sqlite:///census_nyc.sqlite , Here database is sql lite
#making connection of engine
connection=engine.connect()
# Will tell you the list of tables
print(engine.table_names())


#TO use database we need
#Reflection : reads database and build sqlalchemy table objects
from sqlalchemy import Metadata , Table
metadta=Metadata()
#Now we create the object of table using the info we used earlier
census=Table('census', metadata, autoload=True, autoload_with=engine)

print(repr(census)) #will be used to see the deatils of the table 