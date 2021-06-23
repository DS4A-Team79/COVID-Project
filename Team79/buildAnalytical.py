import pandas as pd
import re
import os
import us

directory="../Datasets/Refined_Datasets"
state_files=[]
refined_state_files=[]
for filename in os.listdir(directory):
    state_files.append(pd.read_csv(f"{directory}/{filename}"))

for filename in state_files:
    filename = filename.rename(columns={"NAME":"State"})
    filename["Abbr"] = [us.states.lookup(state).abbr for state in filename["State"]]
    refined_state_files.append(filename)

df_x = pd.merge(refined_state_files[0], refined_state_files[1], on="Abbr", how="outer")
df_z = pd.merge(df_x, refined_state_files[2], on="Abbr", how="outer")


df_z = df_z.drop(["State_x", "State_y","State"], axis=1)
df_z.to_csv(f"{directory}/Analytical.csv")


# for y in test: 
#     if "State" in y.columns or "NAME" in y.columns:
#         if "State" in y.columns:
#             for i in y["State"]:
#                 y["StateAbbr"] = us.states.lookup(i).abbr
#         if "NAME" in y.columns:
#             for i in y["NAME"]:
#                 y["StateAbbr"] = us.states.lookup(i).abbr