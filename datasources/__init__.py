import pandas as pd
import os

india_data = pd.read_csv(os.path.join("datasources", "india.csv"), parse_dates=True, infer_datetime_format=True)
us_data = pd.read_csv(os.path.join("datasources", "us.csv"), parse_dates=True, infer_datetime_format=True)
india_data['country'] = "India"
us_data['country'] = "US"

def get_data():
    data = india_data.append(us_data, ignore_index=True)
    data["Positvity Rate %"] = (data["Number of Covid + Cases"] / (data["Number of Covid + Cases"]+data["Number of Covid - Cases"])) * 100
    data['Date'] = data['Date'].astype('datetime64[ns]')
    return data
