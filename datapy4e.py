import sqlite3 
import urllib.request
from bs4 import BeautifulSoup

conn = sqlite3.connect("assndatabase.sqlite")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS Counts")
cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")
obj1 = urllib.request.urlopen("https://www.py4e.com/code3/mbox.txt?PHPSESSID=82d936abd83203b8fe1ff003beb15c4c").read()
obj2 = BeautifulSoup(obj1, "lxml")
for i in obj2:
    
    if (i.startswith("From")):
        i.split
        var = i[1]
        cur.execute('SELECT count FROM Counts WHERE org = ? ', (var,))
        row = cur.fetchone()
        if row is None:
            cur.execute('''INSERT INTO Counts (org, count)
                    VALUES (?, 1)''', (var,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE count = ?',
                        (var,))
conn.commit()
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()    
        
        