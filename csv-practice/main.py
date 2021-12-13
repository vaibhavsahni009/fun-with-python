import pandas

data=pandas.read_csv("squirrel.csv")

gray_squirrels_count=len(data[data["Primary Fur Color"]=="Gray"])
cinnamon_squirrels_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrels_count=len(data[data["Primary Fur Color"]=="Black"])


print(gray_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)


data_dict={
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[gray_squirrels_count,cinnamon_squirrels_count,black_squirrels_count]
}

print(data_dict)

df=pandas.DataFrame.from_dict(data_dict)

print(df)
df.to_csv("squirrel_count.csv")