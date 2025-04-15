import sqlite3

def viewData():
    try:
        conn = sqlite3.connect('Quotes.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Quotes")
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}")
            print(f"Theme: {row[1]}")
            print(f"Author: {row[2]}")
            print(f"lines: {row[3]}")
            print("-" * 50)
        
        conn.close()
    except sqlite3.Error as e:
        print("Database Error:", e)

viewData()