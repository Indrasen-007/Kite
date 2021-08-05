import requests
import json
from Login import login_user
from MongoDB import insert_many_into_collection

def get_holdings(enctoken):
    url = "https://kite.zerodha.com/oms/portfolio/holdings"
    payload = {}
    headers = {
    'authorization': 'enctoken {0}'.format(enctoken)
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return json.loads(response.text)

def play_with_holding(holdings):

    try:
        if(holdings["status"] == "success"):
            data = holdings["data"]
            day_pnl = 0
            total_invested = 0
            total_pnl = 0
            current_value = 0
            for val in data:
                quantity = float(val["quantity"])
                day_change = float(val["day_change"]) * quantity
                average_price = float(val["average_price"]) * quantity
                pnl = float(val["pnl"]) 
                day_pnl += day_change
                total_invested += average_price
                total_pnl += pnl
                print("Tradingsymbol = ",val["tradingsymbol"].ljust(15,' '), "Change", round(day_change,2))

            current_value = total_pnl + total_invested
            kite_daily_overview = {
                "day_pnl" : day_pnl,
                "total_pnl" : total_pnl,
                "total_invested" : total_invested,
                "current_value" : current_value
            }
            print(kite_daily_overview)
            
            insert_many_into_collection([kite_daily_overview],'KiteDailyOverview')
    except Exception as e:
        print (e)
    
def main():
    enctoken = login_user()
    holdings = get_holdings(enctoken)
    play_with_holding(holdings)
    insert_many_into_collection(holdings["data"],'KiteDailyProgress')
    
if __name__ == "__main__":
    main()