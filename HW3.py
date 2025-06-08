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
list2 = [10, 25, "orange", 45, "banana", 100, "kiwi", 5, 0, "melon"]
print(df[(df["data"]% x == 0) & (df["data"] % y != 0)])


flatten_list = [[1, 2], [3, 4, 5], [6], [7, 8, 9]]
print([a for b in flatten_list for a in b])



print([a for a in list1 if isinstance(a,int)and a<8]+ [a for a in list2 if isinstance(a,int) and a>4])
dicts = [
    {'a': 10, 'b': 5},
    {'a': 7, 'b': 3, 'c': 8},
    {'a': 2, 'c': 4}
]
sum = 0
key = "a"
for a in dicts:
    if key in a:
            sum += a[key]
print(sum)

print(["kse" if isinstance(a,str) and a.lower().startswith(("c","v","o")) else a for a in list1])

cou = 0
for a in list1:
        if isinstance(a,str) and len(a) > x:
                cou+=1
print(cou)

conc = []



for i in range(len(list2)):
        conc.append(str(list2[i])+str(list1[i]))
print(conc)

print([a*y if isinstance(a,(int,float)) and a>x else a for a in list1])
