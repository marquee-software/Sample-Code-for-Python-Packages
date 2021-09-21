#!/usr/bin/env python
# coding: utf-8

# # Reading 
# # https://docs.mongodb.com/drivers/pymongo/
# # https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb
# # https://pymongo.readthedocs.io/en/stable/tutorial.html

# In[21]:


import pymongo
import pprint
from pymongo import MongoClient


# In[ ]:


client = MongoClient()


# In[ ]:


#client = MongoClient('localhost', 27017)            # connect on the default host and port
client = MongoClient('mongodb://remote-server-name-or-ip:27017/')   # Or use the MongoDB URI format


# In[ ]:


db = client.test_database
# db = client['test-database']                        # you can use dictionary style access instead


# # Getting a Collection

# In[ ]:


collection = db.test_collection
#collection = db['test-collection']


# In[ ]:


import datetime
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}


# # Inserting a Document

# In[ ]:


posts = db.posts
post_id = posts.insert_one(post).inserted_id
post_id


# In[ ]:


db.list_collection_names()


# # Getting a Single Document

# In[ ]:


pprint.pprint(posts.find_one())
pprint.pprint(posts.find_one({"author": "Mike"}))
posts.find_one({"author": "Eliot"})


# # Querying By ObjectId

# In[ ]:


post_id
pprint.pprint(posts.find_one({"_id": post_id}))
post_id_as_str = str(post_id)
posts.find_one({"_id": post_id_as_str}) # No result


# In[ ]:


# A common task in web applications is to get an ObjectId from the request URL and find the matching document. 
# It’s necessary in this case to convert the ObjectId from a string before passing it to find_one:
from bson.objectid import ObjectId

def get(post_id):
    # Convert from string to ObjectId:
    document = client.db.collection.find_one({'_id': ObjectId(post_id)})


# # Bulk Inserts

# In[ ]:


new_posts = [{"author": "Mike",
               "text": "Another post!",
               "tags": ["bulk", "insert"],
               "date": datetime.datetime(2009, 11, 12, 11, 14)},
              {"author": "Eliot",
               "title": "MongoDB is fun",
               "text": "and pretty easy too!",
               "date": datetime.datetime(2009, 11, 10, 10, 45)}]
result = posts.insert_many(new_posts)
result.inserted_ids


# # Querying for More Than One Document

# In[ ]:


for post in posts.find():
   pprint.pprint(post)
for post in posts.find({"author": "Mike"}):
   pprint.pprint(post)


# # Counting

# In[ ]:


posts.count_documents({})


# In[ ]:


posts.count_documents({"author": "Mike"})


# # Range Queries

# In[ ]:


d = datetime.datetime(2009, 11, 12, 12)
for post in posts.find({"date": {"$lt": d}}).sort("author"):
    pprint.pprint(post)


# # Indexing

# In[ ]:


result = db.profiles.create_index([('user_id', pymongo.ASCENDING)], unique=True)
sorted(list(db.profiles.index_information()))


# In[ ]:


user_profiles = [
     {'user_id': 211, 'name': 'Luke'},
     {'user_id': 212, 'name': 'Ziltoid'}]
result = db.profiles.insert_many(user_profiles)


# In[ ]:


new_profile = {'user_id': 213, 'name': 'Drew'}
duplicate_profile = {'user_id': 212, 'name': 'Tommy'}
result = db.profiles.insert_one(new_profile)  # This is fine.
result = db.profiles.insert_one(duplicate_profile)

