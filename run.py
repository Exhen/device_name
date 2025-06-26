import pandas as pd
import json
import os
excel_path = "device.xlsx"
path = "."
df = pd.read_excel(excel_path)
for index, row in df.iterrows():
    device_name = row["device_name"]

    j = {
        "device_name": device_name,
        "price": row["price"],
        "price_update_date": row["price_update_date"],
        "ahs_id": row["ahs_id"],
        "cn_name": row["cn_name"],
    }

    with open(f"{path}/{device_name}.json", "w") as f:
        f.write(json.dumps(j, ensure_ascii=False))
    # break