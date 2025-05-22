a = "Hello, Python World!"
print(a)

try:
    n1 = float(input("Введіть число: "))
    n2 = float(input("Введіть число: "))
    print(n1+n2, n1-n2, n1*n2, n1/n2)
except ValueError:
    print("тут мав бути код який вимикає комп'ютер, але його написала гптшка")
except ZeroDivisionError:
    print(" іді полєчісь, іді голову полєчі дурак")

a = "Маніпуляція"
b = "рядком"
print(a+" "+ b, len(a+b))

a = int(input("Введіть ціле число: "))
if a%2 ==0:
    print("парне")
else:
    print("непарне")

a = 0
while a<10:
    a += 1
    print(a)

num = float(input("Введіть число: "))
if num >0 :
    print("додатнє")
elif num <0:
    print("від'ємне")
else:
    print("0")

s = 0
n = int(input("введіть останнє число послідовності: "))
for i in range(1,n+1):
    s += i
print(f"Ваша сума = {s}")

a = 11
while a>1:
    a += -1
    print(a)

for a in range(1,11):
    if a ==5 :
        continue
    if a == 7:
        break
    print(a)