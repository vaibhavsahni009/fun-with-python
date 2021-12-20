import pandas
df=pandas.DataFrame([[1,2,3],[2,3,4],[3,50,5]])
print(df)

print(df.std().mean())

print([df.std()>df.std().mean()])

print(df.drop(columns=df.std()>df.std().mean()))
