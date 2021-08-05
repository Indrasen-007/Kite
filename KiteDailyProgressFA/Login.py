import requests
import json
from Credentials import credentials

userid = credentials().userid
twofa_value= credentials().twofa_value
password= credentials().password #url_encoded value

def login():
    url = "https://kite.zerodha.com/api/login"
    payload = 'user_id={0}&password={1}'.format(userid,password)
    headers = {
    'content-type': 'application/x-www-form-urlencoded',
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return json.loads(response.text)["data"]["request_id"], get_cookie_value (response.cookies,"kf_session")

def two_factor_authentication(request_id,kf_session):
    url = "https://kite.zerodha.com/api/twofa"
    payload = 'user_id={0}&request_id={1}&twofa_value={2}&skip_session='.format(userid,request_id,twofa_value)
    headers = {
    'content-type': 'application/x-www-form-urlencoded',
    'x-kite-userid': '{0}'.format(userid), 
    'Cookie': 'kf_session={0}; user_id={1}'.format(kf_session,userid)
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return get_cookie_value (response.cookies,"enctoken")

def get_cookie_value(cookies, key):
    for cookie in cookies:
        if(cookie.name == key):
            return cookie.value
    return ''    

def login_user():
    request_id,kf_session = login()
    return two_factor_authentication(request_id,kf_session)