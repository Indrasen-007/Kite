def push_data_to_elastic_search_engine(payload, engine_name) :
    import requests
    from Credentials import elastic_search

    url = "https://kite.ent.southeastasia.azure.elastic-cloud.com/api/as/v1/engines/{0}/documents".format(engine_name).lower()
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {0}'.format(elastic_search().private_key)
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    if(response.status_code != 200 and response.status_code != 201) :
        print("Error for ", engine_name, "\n Error : ", response.text)
    else :
        print("Inserted data to elastic search engine ",engine_name)
        
