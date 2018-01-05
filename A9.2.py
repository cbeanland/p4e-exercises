#9.4 Write a program to read through the mbox-short.txt
#and figure out who has the sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a
#count of the number of times they appear in the file. After the dictionary is produced,
#the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname = input("Enter file name: ")
fh = open (fname)
count = 0
email_count = dict()
emails = []
most_common = None
highest_count = None

for line in fh:
    if line.startswith("From:"):
        continue
    elif line.startswith("From"):
        words = line.split()
        emails.append(words[1])

for email in emails:
    email_count[email] = email_count.get(email,0) + 1


for k,v in email_count.items():
    if highest_count is None or v > highest_count:
        most_common = k
        highest_count = v

print(most_common, highest_count)

    
