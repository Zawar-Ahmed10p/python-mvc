from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.mongoData
posts = db.userData
'''post_data = {
    'id': 1,
    'name': 'user2',
    'age': 24
}
'''