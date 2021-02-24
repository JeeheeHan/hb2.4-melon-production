log_file = open("um-server-01.txt")
#opening file in directory into a variable log_file 

def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)

#make function to remove trailing white spaces from the lines
#changed from tues to mon on line 8
#
sales_reports(log_file)
