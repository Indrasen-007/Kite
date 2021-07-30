class credentials:
    def __init__(self):
        self.userid = ""
        self.twofa_value=""
        self.password="" #url_encoded value

class db_credentials:
    def __init__(self):
        ### DB CREDS
        self.server = ''
        self.database = ''
        self.username = ''
        self.password = ''  