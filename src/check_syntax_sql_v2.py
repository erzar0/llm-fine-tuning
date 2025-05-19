import sqlite3

def is_valid_sql(sql: str, schema: str = "") -> bool:
    try:
        conn = sqlite3.connect(":memory:")
        cur = conn.cursor()
        if schema:
            cur.executescript(schema)
        cur.execute("EXPLAIN " + sql)
        return True
    except sqlite3.Error as e:
        print(f"Błąd SQL: {e}")
        return False
    finally:
        conn.close()


schema = """
CREATE TABLE users (id INTEGER, name TEXT);
CREATE TABLE x (a INTEGER, b INTEGER);
"""

queries = [
    "SELECT * FROM users",
    "SELEC * FRM users",               
    "INSERT INTO x VALUES (1, 2)",
    "SELECT id name FROM users",        
    "DELETE FROM y"                   
]

for q in queries:
    print(f"{'VALID' if is_valid_sql(q, schema) else 'ERROR'} :   {q}")