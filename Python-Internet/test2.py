import pandas as pd

learn = pd.read_excel("learn.xlsx", sheet_name='Sales', sep=r'\s*,\s*', header=0, encoding='ascii')

print(learn.head(100))

learn['TestColumn'] = [True if x > 1000 else False for x in learn['COP_VALUE']]

print(learn['TestColumn'])
print(learn)

print(learn.dtypes)

learn['COP_VALUE'] = learn['COP_VALUE'].astype('int')
print(learn.dtypes)
print(learn.columns.tolist())

pvt = pd.pivot_table(data=learn, index='METRIC_NM', values='COP_VALUE', aggfunc='sum')
print(pvt)

#sep=r'\s*,\s*'

dir()