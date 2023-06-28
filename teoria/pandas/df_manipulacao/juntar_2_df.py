import pandas as pd

df = pd.DataFrame

df1 = df(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
)


df2 = df(
    {
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
    },
)

df_final = pd.concat([df1, df2], ignore_index=True)
# ignore_index=False: 0123 0123 # ignore_index=True: 0123 4567

print(df_final)
