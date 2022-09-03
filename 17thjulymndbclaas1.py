import pymongo
client = pymongo.MongoClient("mongodb+srv://deban:8098@cluster0.en0k2jq.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d={
    "name": "Debanjan",
    "surname":"Chakraborty",
    "mail_id": "debanchkrabaorty09@gmail.com",
    "contactno":"+917003225802"
}
db1=client['mongotest']
collection=db1['test']
collection.insert_one(d)
