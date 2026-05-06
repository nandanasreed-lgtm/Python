print("Enter your marks out of 100 : ")
m=int(input("Maths : "))
e=int(input("English : "))
s=int(input("Science : "))

t=m+e+s
p=(t/300)*100
print("Percentage: ",p)

if p>90:
    print("A1 Grade")
elif p>80:
    print("A2 Grade")
elif p>70:
    print("B1 Grade")
elif p>60:
    print("B2 Grade")
elif p>50:
    print("C Grade")
elif p>40:
    print("D Grade")
else:
    print("You Failed the exam.")