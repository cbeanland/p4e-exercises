from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import re
import ssl

#Ignore SSL errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#collect data from fulltime webste
url = 'http://full-time.thefa.com/ListPublicResult.do?divisionseason=331725007&league=9031785'
content = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(content, 'html.parser')

#Create an empty dictionary to store the results
results = {}

#Return only the table tags
table_rows = soup('tr')
table_datas = soup('td')
i=0

for table_data in table_datas:
    #print(table_row.get_text())
    i = i+1
    results [i] = table_data.get_text()
 #   for table_data in table_datas:
#        results.append(i, table_data)
        
print(results)




#results = dict()

#Data = soup.get_text()
#Data = soup.find_all('tr')

#Open a file and put all of the text from the weage into it and then close it
#file = open("testfile.txt", "w")
#file.write(Data)
#file.close()










#League-results_table is the div calss in the soup

#for table_row in soup.select("table.League-Results_Table tr"):
	# Each tr (table row) has three td HTML elements (most people 
	# call these table cels) in it (first name, last name, and age)
#	cells = table_row.findAll('td')
#print(Soup)




#def get_results():
#    i=0
#    for tr in Soup.find_all('tr'):
#        tds = tr.find_all('td')
#        print("league: %s, Date: %s, Home team: %s, Score: %s, Away team %s, leagueagain %s" % \ (tds[0].text, tds[1].text, tds[2].text, tds[3].text, tds[4].text, tds[5].text))

     ##   print
#        print("game", i)
#        i = i + 1
#        for td in tr.find_all('td'):
#            print(td.get_text())
#    return
        
#for line in get_results():
#    line.rstrip()


#print(get_results())

#with get_results() as f, open("outfile.txt","w") as outfile:
 #for i in f.readlines():
#       if not i.strip():
#           continue
#       if i:
#           outfile.write(i)   

#Data = Soup.prettify()


#print(Soup.get_text())

#print(Soup.find_all('tr'))

    

#for tr in soup.find_all('tr')[2:]:
#    tds = tr.find_all('td')
#    print("Nome: %s, Cognome: %s, Email: %s")
#          (tds[0].text, tds[1].text, tds[2].text)
    
#for line in Data:
#    if line.startswith("<"):
#        continue
#    else:
#        print(line)


#my_table = tp.get_tables()[0]
#filename = 'table_as_csv.csv'
#f = open(filename, 'wb')
#with f:
#    writer = csv.writer(f)
#    for row in table:
#        writer.writerow(row)
