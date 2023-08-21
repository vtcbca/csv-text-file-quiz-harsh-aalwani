# Question Solution 4
import csv
header=['sid','name','salary']
rows=[[1,'krishna',4600],[2,'om',4000],[2,'ram',4000],[3,'radha',4600],[5,'sai',4200]]
temp=0     #counter

# Writing file
with open("C:\sqlite3\salary.csv","w",newline="") as write_obj:
    csv_writer=csv.writer(write_obj)
    csv_writer.writerow(header)
    csv_writer.writerows(rows)
	
# Reading file while checking condition
with open("C:\sqlite3\salary.csv","r") as read_obj:
    csv_reader=csv.reader(read_obj)
    for row in csv_reader:
        if row[1][0]=='s':      #if employee name starts with 's',it will pass
            print("{},{},{}".format(row[0],row[1],row[2]))
            temp=temp+1        #number of times condition was satisfied
    maxlen=list(csv_reader)
    print("Number of 'S' names are {}/{}".format(temp,len(rows)))
