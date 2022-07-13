import pandas as pd
from sqlalchemy import create_engine
import psycopg2
engine=create_engine("postgresql+psycopg2://nunam:nunam@165.232.183.174:5432/nunam")

def sheets(data, file):
    if(data=='Cycle_67_3_5'):
        df=pd.read_excel(file,"Cycle_67_3_5")
        df.to_sql(name='Cycle_67_3_5', con=engine, if_exists='append', index=False)
    elif(data=='DetailTemp_67_3_5'):
        df=pd.read_excel(file, "DetailTemp_67_3_5")
        df.to_sql(name='DetailTemp_67_3_5', con=engine, if_exists='append', index=False)
    elif(data=='DetailVol_67_3_5'):
        df=pd.read_excel(file, "DetailVol_67_3_5")
        df.to_sql(name='DetailVol_67_3_5', con=engine, if_exists='append', index=False)
    elif(data=='Detail_67_3_5'):
        df=pd.read_excel(file, "Detail_67_3_5")
        df.to_sql(name='Detail_67_3_5', con=engine, if_exists='append', index=False)
    elif(data=='Statis_67_3_5'):
        df=pd.read_excel(file, "Statis_67_3_5")
        df.to_sql(name='Statis_67_3_5', con=engine, if_exists='append', index=False)


with pd.ExcelFile('5308.xls') as xls:
    for sheet_name in xls.sheet_names:
        print("name:=======>", sheet_name)
        sheets(sheet_name, xls)
        
