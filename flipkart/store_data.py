import sqlite3

def store_data(data):
    connection = sqlite3.connect("flipkart.db")
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS datum
                     (feature REAL, label REAL)''')

    cursor.executemany('INSERT INTO datum VALUES (?, ?)', data)
    
    connection.commit()
    connection.close()


x =  ['axe deo', 'best-seller books', 'calvin klein', 'camcorder', 'camera', 'chemistry', 'chromebook', \
     'c programming', 'data structures algorithms', 'dell laptops', 'dslr canon', 'mathematics', \
     'nike-deodrant', 'physics', 'sony cybershot', 'spoken english', 'timex watch', 'titan watch', \
     'tommy watch', 'written english']

_train=[]
train_label=[]
f = open('training.txt')
for i in range(int(f.readline())):
    s=f.readline().rstrip()
    idx=s.find("\t")
    _train.append(s[:idx])
    train_label.append(x.index(s[idx+1:]))
f.close()

datum = [(a,b) for a,b in zip(_train, train_label)]
store_data(datum)