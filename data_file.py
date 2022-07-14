import pandas as pd
from sqlalchemy import create_engine
import psycopg2
engine=create_engine("postgresql+psycopg2://nunam:nunam@165.232.183.174:5432/nunam")

def sheets(data, file):
    if(data=='Cycle_67_3_5'):
        df=pd.read_excel(file,"Cycle_67_3_5")
        df.to_sql(name='details_cycle6735', con=engine, if_exists='append', index=False)
    elif(data=='DetailTemp_67_3_5'):
        df=pd.read_excel(file, "DetailTemp_67_3_5")
        df.to_sql(name='details_detailtemp6735', con=engine, if_exists='append', index=False)
    elif(data=='DetailVol_67_3_5'):
        df=pd.read_excel(file, "DetailVol_67_3_5")
        df.to_sql(name='details_detailvol6735', con=engine, if_exists='append', index=False)
    elif(data=='Detail_67_3_5'):
        df=pd.read_excel(file, "Detail_67_3_5")
        df.to_sql(name='details_detail6735', con=engine, if_exists='append', index=False)
    elif(data=='Statis_67_3_5'):
        df=pd.read_excel(file, "Statis_67_3_5")
        df.to_sql(name='details_statis6735', con=engine, if_exists='append', index=False)

def sheets1(data, file):
    if(data=='Cycle_67_3_1'):
        df=pd.read_excel(file,"Cycle_67_3_1")
        df.to_sql(name='details_cycle6731', con=engine, if_exists='append', index=False)
    elif(data=='DetailTemp_67_3_1'):
        df=pd.read_excel(file, "DetailTemp_67_3_1")
        df.to_sql(name='details_detailtemp6731', con=engine, if_exists='append', index=False)
    elif(data=='DetailVol_67_3_1'):
        df=pd.read_excel(file, "DetailVol_67_3_1")
        df.to_sql(name='details_detailvol6731', con=engine, if_exists='append', index=False)
    elif(data=='Detail_67_3_1'):
        df=pd.read_excel(file, "Detail_67_3_1")
        df.to_sql(name='details_detail6731', con=engine, if_exists='append', index=False)
    elif(data=='Statis_67_3_1'):
        df=pd.read_excel(file, "Statis_67_3_1")
        df.to_sql(name='details_statis6731', con=engine, if_exists='append', index=False)
        
with pd.ExcelFile('5329.xls') as xls:
    for sheet_name in xls.sheet_names:
        print("name:=======>", sheet_name)
        sheets1(sheet_name, xls)
        
        
with pd.ExcelFile('5308.xls') as xls:
    for sheet_name in xls.sheet_names:
        print("name:=======>", sheet_name)
        sheets(sheet_name, xls)
        
