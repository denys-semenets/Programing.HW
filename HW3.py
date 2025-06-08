list =[2,3,5,38,7,23,8,9,1,-3,-7,-16]
a = sorted(list, reverse=True)
b = []
for i in list:
    if i%2 ==0:
        b.append(i)

print(sum(list),min(list),f"\n {a}")
print(b)
list = [i*3 for i in list]
print(list)

'''
Easy level
перепрошую за pandas і один рядок
так просто цікавіше
'''
x = 4
y = 3
import pandas as pd
list1 =[2,3,5,12,16,15,28,30,39,38,7,23,8,9,1,-3,-7,-16,20,67,-248,848,-1939,39,49,2345,"Car",
        "zsjv","rkd","fvmnv","vmvprenf","apple","pen","python","stop_it","POWER","Roshen","Empty space","abba"]
df = pd.DataFrame(list1)
df.columns = ["data"]
df["data"] = df[df["data"].apply(lambda x: isinstance(x,(int,float)))]
df1 = pd.DataFrame(list1)
df1.columns = ["data"]

print(df[df["data"]>4])
print((df[df["data"]>0]).mean())
print((df[df["data"]<4]).max())
print((df[df["data"]%y==0]).sum())
print([i*i for i in df["data"]])
print((df[df["data"]>0]))
print(df1[df1["data"].str.lower().str.startswith(("c","k","d"),na=False)])
print(df["data"][:(int(input("Введіть кількість чисел : ")))].sum())
print(df1[df1["data"].apply(lambda x: isinstance(x,str) and x.lower() == x.lower()[::-1])])
print(df["data"]%x == 0 )
'''
Medium level
'''
