# Question 4 Solution
import csv
header=['sid','name','salary']
rows=[]; L=[]
temp=1     #counter
# Taking user records
print("Insert Staff Details:- \n")
while temp!=0:
    sid=int(input("Enter Staff ID: "))
    name=input("Enter Staff Name: ")
    salary=int(input("Enter Staff Salary: "))
    L=[sid,name,salary]
    rows.append(L)
    temp=int(input("\nEnter '0' to stop inserting records[Enter any other number to continue]: "))
# Writing file
with open("C:\sqlite3\salary.csv","w",newline="") as write_obj:
    csv_writer=csv.writer(write_obj)
    csv_writer.writerow(header)
    csv_writer.writerows(rows)
	
# Reading file while checking condition
with open("C:\sqlite3\salary.csv","r") as read_obj:
    csv_reader=csv.reader(read_obj)
    for row in csv_reader:
        if row[1][0]=='s' or row[1][0]=='S':      #if employee name starts with 's',it will pass
            print("{},{},{}".format(row[0],row[1],row[2]))
            temp=temp+1        #number of times condition was satisfied
    print("Number of 'S' names are {}/{}".format(temp,len(rows)))
