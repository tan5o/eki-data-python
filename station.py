import pandas as pd
import numpy as np

df_station = pd.read_csv("csv/station20200316free.csv")
df_company = pd.read_csv("csv/company20200309.csv")
df_join = pd.read_csv("csv/join20200306.csv")
df_line = pd.read_csv("csv/line20200306free.csv")
df_pref = pd.read_csv("csv/pref.csv")

def get_df():
    return {"station": df_station, "company": df_company, "join": df_join, "line": df_line, "pref": df_pref}

def get_station():
    return df_station

def get_pref_cd(pref_name):
    val = df_pref[df_pref["pref_name"] == pref_name]["pref_cd"].values

    if len(val) == 0:
        raise ValueError(pref_name + " is not exist")
    return val[0]

def get_station_from_pref(pref_name):
    pref_cd = get_pref_cd(pref_name)
    return df_station[df_station["pref_cd"] == pref_cd]

def get_lat_lng_from_station(station_name):
    station = df_station[df_station["station_name"] == station_name]
    val = station[["lat","lon"]].values
    if len(val) == 0:
        raise ValueError(station_name + " is not exist")
    print(type(val[0].astype(float)))
    return val[0]

#print(get_pref_cd("北海道"))
#print(get_lat_lng_from_station("東京"))