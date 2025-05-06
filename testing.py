from pymongo import MongoClient

# Replace <password> with your actual password
connection_string = ""

# Create a MongoClient
client = MongoClient(connection_string)

# Access the demoDB database
db = client["demoDB"]

# Replace "your_collection_name" with the actual collection name
collection_name = "logs"
collection = db[collection_name]

# Query the collection and print the documents
documents = collection.find()

for document in documents:
    print(document)
