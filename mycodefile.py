import pandas as pd
import os

mydata = {
    "name": [
        "goli",
        "bhide",
        "popatlal",
        "tarak mehta",
        "anjali mehta",
        "jethalal gada"
    ],
    "age": [15, 45, 40, 38, 35, 40],
    "job": [
        "student",
        "teacher",
        "teacher",
        "reporter",
        "writer",
        "businessman"
    ]
}

df = pd.DataFrame(mydata)

data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

filepath = os.path.join(data_dir, "sample_data.csv")

df.to_csv(filepath, index=False)

print(f"CSV saved to {filepath}")