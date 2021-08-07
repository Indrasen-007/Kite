class credentials:
    def __init__(self):
        self.userid = ""
        self.twofa_value=""
        self.password="" #url_encoded value

class db_credentials:
    def __init__(self):
        ### DB CREDS
        self.CONNECTION_STRING = "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/?retryWrites=true&w=majority"
        
class elastic_search :
    def __init__(self):
        self.private_key = ""        
