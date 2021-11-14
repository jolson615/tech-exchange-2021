#import PyMongo 
import pymongo

#connect to MongoDB database
#intialize database and collection variables
client = pymongo.MongoClient("<url>")
db = client.database
langs = db.languages

'''Find'''
#1. Return the first entry in the collection

#2. Return all entries in the collection

#3. Return only the language name and designer for all entries in the collection
# this can improve performance when accessing databases with many fields

#4. Return only the language name and file extensions for all entries in the collection
# print each language name and its file extensions as a formatted string

#5 Return all entries in the collection sorted by the year of their first appearance
# print each language name and its first appearance as a formatted string

'''Query'''
#6. Return all entries that first appeared in 1993
# print each language name and its first appearance as a formatted string

#7. Return all entries that first appeared after 1993
# print each language name and its first appearance as a formatted string

#8. Return all entries not designed by the World Wide Web Consortium
# print each language name and its designer's name(s) as a formatted string

'''Lists'''
#9. Return the entry which includes the file extension .class
# print the language name and its file extension as a formatted string

#10. Return all entries with only one file extension
# print each language name and its file extension as a formatted string

#11. Define a function search_extension() with one parameter named ext(str) that prints the language that uses that file extension.
# call search_extension(".csx") and search_extension(".phar")

'''Regular Expressions'''
#12. Define a function find_by_letter() with one parameter named letter(str) that prints all languages that begin with the specified letter.
# call find_by_letter("R") and find_by_letter("P")
# note that this requires the use of regular expressions

#13. Define a function find_by_last_name() with one parameter named letter(str) that prints all designers whose last name(s) begin(s) with the specified letter.
# call find_by_last_name("G") and find_by_last_name("H")
# note that this requires the use of regular expressions

#14. Define a function search_name() with one parameter named name(str) that prints the designer(s) whose names include the specified string.
# call search_name("boyce") and search_name("pike")
# searches should not be case-sensitive
# note that this requires the use of regular expressions

