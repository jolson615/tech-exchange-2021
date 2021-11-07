#import PyMongo and seed data
import pymongo
from language_seed import language_seed

#connect to MongoDB database
client = pymongo.MongoClient("<url>")

#identify whether the database already exists
db_list = client.list_database_names()
print('databases: ',db_list)
if 'database' in db_list:
    print('database already exists')
else:
    print('creating database')

#intialize database variable
db = client.database

#identify whether the collection already exists
col_list = db.list_collection_names()
print('collections: ',col_list)
if 'languages' in col_list:
    print('languages collection already exists')
else:
    print('creating collection')
    db.create_collection('languages')

#intialize collection variable
langs = db.languages

#reset check
reset_check = input("Do you want to reset this collection from the seed file? (y/n)")
if (reset_check.lower() == 'y'):
    langs.drop()
    lang_seed = langs.insert_many(language_seed)
    print("Inserted: ",lang_seed)