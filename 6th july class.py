#pandas

import pandas as pd
data={'Name':['Tom', 'jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df=pd.DataFrame(data)
print(df)

import pandas as pd
data={'Name':['Tom', 'jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df=pd.DataFrame(data,index={'rank1','rank2','rank3','rank4'})
print(df.head(2))
print(df.tail(2))

d={'Name': pd.Series(['Tom', 'jack', 'Steve', 'Ricky']),
'Age': pd.Series([28,34,29,42]),
'Rating ':pd.Series ([4,23,3,24])}
df=pd.DataFrame(d)
print(df)
print(df.axes)
print(df.dtypes)
print(df.shape)
print(df.values)

df=pd.read_csv("sample1.csv")
print(df)
print(df['name'])

import pandas as pd
import numpy as np
data=np.array(['a','b','c','d'])
s=pd.Series(data)
print(s)

import pandas as pd
import numpy as np
data={'a','b','c','d'}
a=pd.Series(data)








