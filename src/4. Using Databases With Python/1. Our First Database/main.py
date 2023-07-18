import sqlite3

con = sqlite3.connect("tutorial.db")
cur = con.cursor()

query = """\
CREATE TABLE Ages (
  name VARCHAR(128),
  age INTEGER
)\
"""
cur.execute(query)


queries = [
    """\
DELETE FROM Ages;\
""",
    """\
INSERT INTO Ages (name, age) VALUES ('Murdo', 33);\
""",
    """
INSERT INTO Ages (name, age) VALUES ('Gus', 15);\
""",
    """
INSERT INTO Ages (name, age) VALUES ('Rhianna', 22);\
""",
    """
INSERT INTO Ages (name, age) VALUES ('Kinsey', 21);\
""",
]
for query in queries:
    cur.execute(query)

con.commit()

query = """\
SELECT hex(name || age) AS X FROM Ages ORDER BY X;\
"""
res = cur.execute(query)
print(res.fetchall())
