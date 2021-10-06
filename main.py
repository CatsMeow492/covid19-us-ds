import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Import dataset from https://covidtracking.com/data/download

data = pd.read_csv(r'national-history.csv')

# Fill in missing data with set mean rounded to .1

data = data.fillna(data.mean().round(1))

print(data.head())
print(data.describe())

# Create and Save ScatterPlot of Death Increases vs Date

sns.relplot(x="date", y="deathIncrease", data=data)
plt.savefig('DateVsDeathIncrease.png')

# Deaths by State

#sns.set_theme(style="whitegrid")
#g = sns.catplot(
#    data=data, kind="bar",
#    x="death", y="states",
#    ci="sd", palette="dark", alpha=.6, height=6
#)
#g.despine(left=True)
#g.set_axis_labels("State", "Total Deaths")
#g.savefig('DeathsbyState.png')

# Create and Save ScatterPlot of Death Increases vs Positive Tests

sns.relplot(x="positive", y="death", data=data)
plt.savefig('positivevsdeath.png')

# Create and Save ScatterPlot of current hospitalizations vs current hospitalizations in ICU

sns.relplot(x="hospitalizedCurrently", y="inIcuCurrently", data=data)
plt.savefig('hospitalizedCurrentlyvsInIceCurrently.png')

# A more ambitious set

status = data.hospitalizedCurrently, data.inIcuCurrently, data.onVentilatorCurrently
print(status)

sns.set_theme(style="whitegrid")

rs = np.random.RandomState(365)
values = rs.randn(365, 4).cumsum(axis=0)
dates = pd.date_range("1 1 2016", periods=365, freq="D")
data = pd.DataFrame(values, dates, columns=["A", "B", "C", "D"])
data = data.rolling(7).mean()

sns.lineplot(data=data, palette="tab10", linewidth=2.5)
