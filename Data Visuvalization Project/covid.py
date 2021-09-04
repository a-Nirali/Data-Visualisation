import pandas as pd
import plotly.express as px

df=pd.read_csv("Copy+of+data+-+data.csv")
corona=px.scatter(df,x="date",y="cases",color="country",title="Covid-19 Cases")
corona.show()

