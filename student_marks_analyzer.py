n=int(input("Enter numbers of subject :"))
marks=[float(input("Enters marks for subjects {i+1} :"))for i in range(n)]
total=sum(marks)
average=total/n
if average>=90:
    grade = "A+"
elif average>=80:
    grade = "A"
elif average>=70:
    grade = "B"
elif average>=60:
    grade =  "C"
elif average>=50:
    grade = "D"
else:
    grade = "Fail"
print("\n------Students Marks Analysis ----")
print(f"Marks :{marks}")
print(f"Total Marks :{total}")
print(f"Average Marks : {average :.2f}")
print(f"Grade :{grade}")
print("\n Subject with marks grater than  average : ")
for i in range(n):
    if marks[i]>average :
        print(f"Subject {i+1}:{marks[i]}")
failed_sujects =[f"Subject{i+1}"for i in range(n) if marks[i]<40]
print("\n Failed Subjects :",failed_sujects if failed_sujects else "None")