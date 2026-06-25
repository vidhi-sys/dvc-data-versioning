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
new_member={
    "name":'Dr.Haathi',
    "age":'45' ,
    "job":'Doctor'
}
new_member2={
    "name":'Iyer',
    "age":'39' ,
    "job":'scientist'
}
new_member3={
    "name":'roshan sodhi',
    "age":'32' ,
    "job":'mechanic'
}

df = pd.DataFrame(mydata)
df.loc[len(df.index)] = new_member
df.loc[len(df.index)] = new_member2
df.loc[len(df.index)] = new_member3
data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

filepath = os.path.join(data_dir, "sample_data.csv")

df.to_csv(filepath, index=False)

print(f"CSV saved to {filepath}")