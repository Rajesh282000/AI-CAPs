from pymongo.mongo_client import MongoClient

client = MongoClient("mongodb://localhost:27017/")

#Database 
db = client["myBlogs"]

#Table or Collection
blogsCollection = db["blogs"]
usersCollection = db["users"]

try:
    client.admin.command("ping")
    print("Connected to MongoDB successfully!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")