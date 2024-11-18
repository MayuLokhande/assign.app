import pandas as pd


df = pd.DataFrame({"sepal_length": [5.1, 4.9, None, 5.0, None]})


df["sepal_length"].fillna(df["sepal_length"].mean(), inplace=True)

print(df)
