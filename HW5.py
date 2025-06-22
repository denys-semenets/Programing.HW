import requests as r
import pandas as pd


req = r.get(f"https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,wind_speed_10m").json()["hourly"]
df = pd.DataFrame(req)
df.columns = ["time","temperature","wind_speed"]

da = df[:72]
wind = len(df[df["wind_speed"] > df["wind_speed"].mean()])
print(da["temperature"].min(),da["temperature"].max(),da["temperature"].mean())
print(wind)
