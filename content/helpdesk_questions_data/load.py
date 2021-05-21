import json
from random import randint
from pymongo import MongoClient


client = MongoClient()
db = client.get_database('helpDESK')
col = db.get_collection('records')
main_path = "/home/isolveit/Documents/myCodes/Codes/help_desk/webapp/content/helpdesk_questions_data"
json_files = ["admission.json", "campus_related.json",
              "fees_interpay.json", "school_hostel.json",
              "school_related.json", "vclass.json"]
file_paths = [f"{main_path}/{item}" for item in json_files]
for file_path in file_paths:
    with open(file_path, 'r') as file:
        gh = json.load(file)
        for item in gh:
            document = {
                "_questionID": randint(1_000_000, 1_000_000_000), "_title": item['title'],
                "_answer": item['answer'],
                "_category": item['category'], "_tags": item['tags']
            }
            col.insert_one(document)
            print(item, 'inserted')
