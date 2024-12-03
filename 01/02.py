from sqlite_utils import Database
db = Database(memory=True)

def readData(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            splitted = line.split()
            xInt = int(splitted[0])
            yInt = int(splitted[1])
            data.append({"x": xInt, "y":yInt})
    db['t'].insert_all(data)


sql = f"""
SELECT SUM(t.x * t2.aantal) as result
FROM t
JOIN (
    SELECT y, COUNT(1) as aantal
    FROM t t2
    GROUP BY y
) t2 ON t2.y = t.x

"""

readData('2024-01-input.txt')

for row in db.query(sql):
    print(row)

