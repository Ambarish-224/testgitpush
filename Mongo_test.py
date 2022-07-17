import pymongo

client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    'name' : "Ambarish",
    'email' : "ambarish.singh224@gmail.com",
    'surname': "Singh"
     }

db1 = client['mongo_test']
coll = db1['test']
coll.insert_one(d)
