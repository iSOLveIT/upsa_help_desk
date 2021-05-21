import json
from random import randint
from pymongo import MongoClient


client = MongoClient()
db = client.get_database('helpDESK')
col = db.get_collection('records')
file_path = "/home/isolveit/Documents/myCodes/Codes/help_desk/webapp/content/helpdesk_questions_data/admission.json"

with open(file_path, 'r') as file:
    gh = json.load(file)
    for item in gh:
        document = {
            "_questionID": randint(1_000_000, 1_000_000_000), "_title": item['title'], 
            "_answer": "lorem ipsum",
            "_category": item['category'], "_tags": item['tags']
        }
        col.insert_one(document)
        print(item, 'inserted')
