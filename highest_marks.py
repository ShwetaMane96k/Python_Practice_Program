def find_highesst_marks(students):
    highest=max(students.values())
    toppers=[name for name,marks in students.items()if marks == highest]
    return toppers,highest
students={
    "Shweta" : 95,
    "Dhanu" : 80,
    "Sita" : 82,
    "Gita" : 90
    }
toppers,marks=find_highesst_marks(students)
print("Topper(s) :",toppers)
print("Highest Marks :",marks)