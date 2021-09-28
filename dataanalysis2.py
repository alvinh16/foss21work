#!/usr/bin/python3.9 # This program computes square root of x # import os import pandas as pd
import pandas as pd
import plotly.express as px
import seaborn as sns

# pd.set_option("mode.chained_assignment",None)
df = pd.read_csv("https://drive.google.com/uc?id=1VwKENxmc_AWmP1Rpyl0t1pgfH5GIlLFM")
df_sg = df.query("location == 'Singapore'").reset_index()
df_sg['average_sevendays'] = df_sg['new_cases'].rolling(7, min_periods = 1).mean()
df_sg
# df_sg.plot.bar(
#     x = ,
#     y =
# )

# df = pd.read_csv("https://drive.google.com/uc?id=1VwKENxmc_AWmP1Rpyl0t1pgfH5GIlLFM")
# df.head()
# df.info()

# df_world = df.query("location=='World'")
# df_sg = df.query("location=='Singapore'")
# df_mal = df.query("location=='Malaysia'")
