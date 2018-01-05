#10.2 Write a program to read through the mbox-short.txt and
#figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time
#and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour,
#print out the counts, sorted by hour as shown below.

fname = input("Enter name of the file: ")
handle = open(fname)

times = dict()
position = 0
hrs = []
hours = dict()
listofhours = []

for line in handle:
    if line.startswith("From:"):
        continue
    elif line.startswith("From"):
        position = line.find(":")
        start = int(position) - 2
        time_string = line[start:start+8]
        time_list = time_string.split(":")
        hrs.append(time_list[0])
        
for hr in hrs:
    hours[hr] = hours.get(hr,0) + 1

for k,v in sorted(hours.items()):
    print(k,v)




