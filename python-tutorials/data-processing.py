import csv
from collections import namedtuple
import re
import json
from urllib.request import urlopen
from xml.etree.ElementTree import parse, Element, tostring
import sqlite3
import binascii
import base64
from struct import Struct

# CSV Data 
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    try:
        header = next(f_csv)
        Row = namedtuple('Row', header)
    except ValueError:
        header = (re.sub('[^a-zA-Z_]', '_', n) for n in next(f_csv))
        Row = namedtuple('Row', header)
    for r in f_csv:
        row = Row(*r)
        print(f'Symbol: {row.Symbol}, Volume: {row.Volume}')

print("----------------")
# Json Data
data = {
    'name' : 'xxx',
    'shares' : 22,
    'price' : 33.3
}

s = json.dumps(data)
print(json.loads(s))
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)
with open('data.json', 'r') as f:
    print(json.load(f))
print("----------------")

# XML Data
u = urlopen("https://planetpython.org/rss20.xml")
doc = parse(u)

for item in doc.iterfind("channel/item"):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')

root = doc.getroot()
e = Element('spam')
e.text = 'This is a test'
root.insert(2, e)

doc.write('newpred.xml', xml_declaration=True)

doc = parse('newpred.xml')

print("----------------")
# From a dic to XML

def dic_to_xml(parent, d):
    elem = Element(parent)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem

dic = { 'name' : 'erdem', 'role': 'engineer' }
e = dic_to_xml('employee', dic)
e.set('id', '0')
print(tostring(e))

print("----------------")
# Implementing sqlite3
stocks = [
    ('GOOG', 100, 490.1),
    ('AAPL', 50, 545.75),
    ('FB', 150, 7.45),
    ('HPQ', 75, 33.2),
]
db = sqlite3.connect('database.db')
c = db.cursor()
try:
    c.execute('create table data (symbol text, shares integer, price real)')
    db.commit()
    c.executemany('insert into data values (?,?,?)', stocks)
    db.commit()
except:
    pass

min_price = 100
for row in db.execute('select * from data where price >= ?', (min_price,)):
    print(row)

print("----------------")
# Encoding hex, base64
s = b'hello'
h = binascii.b2a_hex(s)
print(h)
print(binascii.a2b_hex(h))
h = base64.b16encode(s)
print(base64.b16decode(h))

print("----------------")
# Binary Data
def write_records(records, format, f):
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))

def read_records(format, f):
    record_struct = Struct(format)
    chunks = iter(lambda: f.read(record_struct.size), b'')
    return (record_struct.unpack(chunk) for chunk in chunks)

if __name__ == '__main__':
    records = [ (1, 2.3, 4.5),
                (6, 7.8, 9.0),
                (12, 13.4, 56.7) ]

    with open('data.b', 'wb') as f:
        write_records(records, '<idd', f)
    
    with open('data.b', 'rb') as f:
        for rec in read_records('<idd', f):
            print(rec)





