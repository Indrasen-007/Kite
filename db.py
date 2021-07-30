import pyodbc
from DB.ConnectDB import cursor, cnxn
#https://github.com/mkleehammer/pyodbc/wiki/Cursor

def get_or_create_table_daily_progress_table():
    try:
        #Check if table exists
        if not cursor.tables(table='DailyProgress', tableType='TABLE').fetchone():
            print("DailyProgress table doesn't exist")
            # create table if doesn't exists
            cursor.execute('''
                CREATE TABLE DailyProgress(
                id int NOT NULL IDENTITY(1, 1),
                authorised_date date NULL,
                authorised_quantity int NULL,
                average_price float NULL,
                close_price float NULL,
                collateral_quantity int NULL,
                collateral_type varchar(50) NULL,
                day_change float NULL,
                day_change_percentage float NULL,
                discrepancy varchar(50) NULL,
                exchange varchar(50) NULL,
                instrument_token int NULL,
                isin varchar(50) NULL,
                last_price float NULL,
                opening_quantity int NULL,
                pnl float NULL,
                price float NULL,
                product varchar(50) NULL,
                quantity int NULL,
                realised_quantity int NULL,
                t1_quantity int NULL,
                tradingsymbol varchar(50) NULL,
                used_quantity int NULL,
                daily_pnl float NULL,
                created_on DATETIME NOT NULL DEFAULT GETDATE()
                )
            ''')
            print("Table DailyProgress created")
    except pyodbc.Error as err:
        print(err)
        cnxn.rollback()
    else:
        cnxn.commit()
  
def insert_into_daily_progress_table(data) :
    try:
        cursor.execute('''
            INSERT INTO DailyProgress
            (authorised_date
            ,authorised_quantity
            ,average_price
            ,close_price
            ,collateral_quantity
            ,collateral_type
            ,day_change
            ,day_change_percentage
            ,discrepancy
            ,exchange
            ,instrument_token
            ,isin
            ,last_price
            ,opening_quantity
            ,pnl
            ,price
            ,product
            ,quantity
            ,realised_quantity
            ,t1_quantity
            ,tradingsymbol
            ,used_quantity
            ,daily_pnl)
        VALUES
            (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        ''',data["authorised_date"],
            data["authorised_quantity"],
            data["average_price"],
            data["close_price"],
            data["collateral_quantity"],
            data["collateral_type"],
            data["day_change"],
            data["day_change_percentage"],
            str(data["discrepancy"]),
            data["exchange"],
            data["instrument_token"],
            data["isin"],
            data["last_price"],
            data["opening_quantity"],
            data["pnl"],
            data["price"],
            data["product"],
            data["quantity"],
            data["realised_quantity"],
            data["t1_quantity"],
            data["tradingsymbol"],
            data["used_quantity"],
            float(data["day_change"])*float(data["quantity"]))
        daily_change = float(data["day_change"])*float(data["quantity"])
        print("Inserted entry for Tradingsymbol = ",data["tradingsymbol"].ljust(15,' '), "Change", round(daily_change,2))
    except pyodbc.Error as err:
        print(err)
        cnxn.rollback()
    else:
        cnxn.commit()    

def get_or_create_table_total_daily_progress_table():
    try:
        #Check if table exists
        if not cursor.tables(table='DailyTotalProgress', tableType='TABLE').fetchone():
            print("DailyTotalProgress table doesn't exist")
            # create table if doesn't exists
            cursor.execute('''
                CREATE TABLE DailyTotalProgress(
                id int NOT NULL IDENTITY(1, 1),
                daily_pnl float NULL,
                created_on DATETIME NOT NULL DEFAULT GETDATE()
                )
            ''')
            print("Table DailyTotalProgress created")
    except pyodbc.Error as err:
        print(err)
        cnxn.rollback()
    else:
        cnxn.commit()
  
def insert_into_daily_total_progress_table(total) :
    try:
        cursor.execute('''INSERT INTO DailyTotalProgress (daily_pnl) VALUES (?)''',total)
        print("Inserted total profit/loss for today =",total)
    except pyodbc.Error as err:
        print(err)
        cnxn.rollback()
    else:
        cnxn.commit()    

def get_daily__total_progress_data():
    try:
        cursor.execute("SELECT * from DailyTotalProgress")
        for row in cursor:
             print(row)
    except pyodbc.Error as err:
        print(err)
        cnxn.rollback()
    else:
        cnxn.commit()  

def get_daily_progress_data():
    try:
        cursor.execute("SELECT * from DailyProgress")
        for row in cursor:
             print(row)
    except pyodbc.Error as err:
        print(err)
        cnxn.rollback()
    else:
        cnxn.commit()  
        
# get_daily_progress_data()
get_daily__total_progress_data()