import csv
with open("salary.csv",'w',newline='')as f:
     data=csv.writer(f)
     header=['sid','sname','salary']
     record=[[1,'om',4000],
            [2,'sai',5700],
            [3,'ram',4200],
            [4,'ronak',7700],
            [5,'rekha',7800]]
     data.writerow(header)
     data.writerows(record)
     data=csv.reader(f)
     for i in data :
         print(i)
