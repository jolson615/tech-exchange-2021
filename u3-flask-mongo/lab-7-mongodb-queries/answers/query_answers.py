#import PyMongo 
import pymongo

#connect to MongoDB database
#intialize database and collection variables
client = pymongo.MongoClient("<url>")
db = client.database
langs = db.languages

'''Find'''
#1. Return the first entry in the collection
first_entry = langs.find_one()
print(first_entry)

#2. Return all entries in the collection
all_entries = langs.find()
for e in all_entries:
    print(e['language'])

#3. Return only the language name and designer for all entries in the collection
# this can improve performance when accessing databases with many fields
designers = langs.find({},{"_id":0, "language":1, "designer":1})
for e in designers:
    print(e)

#4. Return only the language name and file extensions for all entries in the collection
# print each language name and its file extensions as a formatted string
file_exts = langs.find({},{"_id":0, "language":1, "file_extensions":1})
for e in file_exts:
    ext_list = ""
    for i in e['file_extensions']:
        ext_list += (i + " ")
    print(f"{e['language']} file extensions: {ext_list}")

#5 Return all entries in the collection sorted by the year of their first appearance
# print each language name and its first appearance as a formatted string
sorted_langs = langs.find().sort("first_appeared")
for e in sorted_langs:
    print(f"{e['language']}: {e['first_appeared']}")

'''Query'''
#6. Return all entries that first appeared in 1993
# print each language name and its first appearance as a formatted string
from_1993 = langs.find({"first_appeared":1993})
for e in from_1993:
    print(e['language']+" first appeared in 1993")

#7. Return all entries that first appeared after 1993
# print each language name and its first appearance as a formatted string
after_1993 = langs.find({"first_appeared":{"$gt":1993}})
for e in after_1993:
    print(f"{e['language']} first appeared in {e['first_appeared']}")

#8. Return all entries not designed by the World Wide Web Consortium
# print each language name and its designer's name(s) as a formatted string
designers_a_b = langs.find({"designer":{"$ne":"World Wide Web Consortium"}})
for e in designers_a_b:
    print(e['language'])



'''Lists'''
#9. Return the entry which includes the file extension .class
# print the language name and its file extension as a formatted string
class_ext = langs.find_one({ "file_extensions": ".class"} )
print(f"{class_ext['language']} uses {class_ext['file_extensions']}")

#10. Return all entries with only one file extension
# print each language name and its file extension as a formatted string
one_file_ext = langs.find({ "file_extensions": { "$size": 1 } } )
for e in one_file_ext:
    print(f"{e['language']} uses {e['file_extensions'][0]}")

#11. Define a function search_extension() with one parameter named ext(str) that prints the language that uses that file extension.
# call search_extension(".csx") and search_extension(".phar")
def search_extension(ext):
    '''Returns the language whose extension matches the parameter ext (str)'''
    ext_match = langs.find_one({ "file_extensions": ext } )
    print(f"{ext_match['language']} uses {ext_match['file_extensions']}")

search_extension(".csx")
search_extension(".phar")

'''Regular Expressions'''
#12. Define a function find_by_letter() with one parameter named letter(str) that prints all languages that begin with the specified letter.
# call find_by_letter("R") and find_by_letter("P")
# note that this requires the use of regular expressions
def find_by_letter(letter):
    '''Returns all languages that begin with the specified letter (str)'''
    query = {"language":{"$regex":f"^{letter}"}}
    entries = langs.find(query)
    for e in entries:
        print(e['language'])
    
find_by_letter("R")
find_by_letter("P")

#13. Define a function find_by_last_name() with one parameter named letter(str) that prints all designers whose last name(s) begin(s) with the specified letter.
# call find_by_last_name("G") and find_by_last_name("H")
# note that this requires the use of regular expressions
def find_by_last_name(letter):
    '''Returns all designers whose last name(s) begin(s) with the specified letter (str)'''
    query = {"designer":{"$regex":f"\s{letter}"}}
    entries = langs.find(query)
    for e in entries:
        print(e['designer'])
    
find_by_last_name("G")
find_by_last_name("H")

#14. Define a function search_name() with one parameter named name(str) that prints the designer(s) whose names include the specified string.
# call search_name("boyce") and search_name("pike")
# searches should not be case-sensitive
# note that this requires the use of regular expressions
def search_name(name):
    '''Returns the designer whose name is entered as name (str)'''
    query = {"designer":{"$regex":name,"$options":"i"}}
    entry = langs.find_one(query)
    print(entry['designer'])
    
search_name("boyce")
search_name("pike")
