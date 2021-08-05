def get_database():
    import pymongo
    from Credentials import db_credentials
    conn_str = db_credentials().CONNECTION_STRING
    client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
    return client['Kite']

def insert_many_into_collection(data, collection):
    try:
        db_name = get_database()
        collection_name = db_name[collection]
        collection_name.insert_many(data)
        print('Inserted data into '+collection)
    except Exception as e:
        print (e)

