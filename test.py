from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))
db = client["mongo"]  # Your database name
print("Connected to MongoDB! Databases:", client.list_database_names())