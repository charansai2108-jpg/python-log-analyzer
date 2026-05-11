#Read log files and Count
# ERROR
#WARNING
#INFO

with open(r"C:\Users\ADMIN\Documents\Python_WorkSpace\Test.txt", "r") as file:
    count=0
    for line in file:
        if "ERROR" in line:
            count=count+1
    print(count)
