import pandas as pd

df = pd.DataFrame({"id":["000","001","002","003","004","005","006","007","008","009","010","011","012","013","014","015","016","017","018","019"],
                   "team":["a","a","a","b","b","b","b","c","c","d","d","d","d","d","d","e","e","f","f","f"],
                   "score":[30,26,31,40,39,23,17,50,45,34,11,42,32,27,10,39,20,14,43,15]})

print(df.head(20))

input()

group = df.groupby("team")
group = group.sum()
group = group.sort_values(["score"],ascending=False)

print(group)
