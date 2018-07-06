#question1

import pandas as pd
data={'name':{'tom','jack','steve','ricky'},'age':{28,34,42},'mail id':['tom@gmail.com','jack@gmail.com','steve@gmail.com','ricky@gmail.com'],
        'phone no':([5872789379,7689036091,9879797764,6869810878])}
df=pd.DataFrame(data)
print(df)


#question2
df =pd.read_csv("p.csv")
#a
print(df.head(5))
#b
print(df.head(10))
#c
print(df['Min Temp'].describe())
print(df['Min Temp'].max())
print(df['Min Temp'].var())
print(df['Min Temp'].secribe())
print(df['Risk_MM'].mean())
#d
print(df.tail(5))
print(df['Location'])
print(df['Locatio'].describe)