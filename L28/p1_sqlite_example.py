import sqlite3

connection = sqlite3.connect('dbs/orders.db', isolation_level=None)

cursor = connection.cursor()

#data = cursor.execute('select * from Vendors;')
#print(data)
#print(data.fetchall())

# import pprint
# pprint.pprint(data.fetchall())


# print(data.fetchone())
# print(data.fetchone())
# print(data.fetchmany(2))
# print(dir(data))

# for line in data:
#     print(line)

# cursor.execute("INSERT INTO Vendors(name, item, deal, price) VALUES ('Oksana', 'Car-Train', 3, 50);")
# data = cursor.execute('select * from Vendors;')
# print(data.fetchall())
# connection.commit()

# cursor.execute("INSERT INTO Vendors(name, item, deal, price) VALUES ('Olga', 'Helicopter', 43, 5000);")
# data = cursor.execute('select * from Vendors;')
# print(data.fetchall())


#data = cursor.execute('select * from Vendors where deal=3 and price > 10;')
# deal_id = 3
# price = 10
# data = cursor.execute(f'select * from Vendors where deal={deal_id} and price > {price};')
# data = cursor.execute(f'select * from Vendors where deal=(?) and price > (?);', (3, 10))
# data = cursor.execute(f'select * from Vendors where deal=(?);', (3,))
# data = cursor.execute(f'select * from Vendors where deal=:deal_id and price > :price;', {'deal_id': 3, 'price': 10})
# print(data.fetchall())

# cursor.executemany("INSERT INTO Vendors(name, item, deal, price) VALUES ((?), (?), (?), (?));",
#                    [('Olga1', 'Helicopter1', 431, 50001), ('Olga2', 'Helicopter2', 432, 50002)])


with open('test.sql', 'r') as f:
    cursor.executescript(f.read())


cursor.close()
connection.close()
