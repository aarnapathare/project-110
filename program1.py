import statistics as st
import pandas as pd 
import random
import plotly.figure_factory as ff
import statistics as st
df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

meansamplinglist = []
for i in range(100):
    readinglist = []
    for j in range(30):
        readinglist.append(random.choice(data))
    meansamplinglist.append(st.mean(readinglist))

fig = ff.create_distplot([meansamplinglist], ["reading_time"], show_hist=False)
fig.show()

datamean = st.mean(data)
meansampling = st.mean(meansamplinglist)

print(meansampling)
print(datamean)