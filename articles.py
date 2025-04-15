import sqlite3
import requests
from bs4 import BeautifulSoup

def connectDb():
    try:
        conn=sqlite3.connect('Quotes.db')
        cursor=conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Quotes(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       theme TEXT,
                       author TEXT,
                       lines TEXT)''')
        conn.commit()
    except sqlite3.Error as e:
        print("Database Connection Error",e)
    # finally:
    #     conn.close()

def fetchData(url):
    try:
        headers={"User-Agent":"Mozilla/5.0"}
        responses=requests.get(url,headers=headers)
        if(responses):
            soup=BeautifulSoup(responses.text,"html.parser")
            articles=soup.find("div",attrs={'id':'all_quotes'})
            data=[]
            for article in articles.find_all('div',attrs={'class': 'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
                theme = article.h5.text
                lines = article.img['alt'].split(" #")[0]
                author = article.img['alt'].split(" #")[1]
    
                data.append((theme,lines,author))
            return data

    except requests.exceptions.RequestException as err:
        print("Request Error",err)

def storeData(data):
    try:
        conn=sqlite3.connect('Quotes.db')
        cursor=conn.cursor()
        for theme,lines,author in data:
            # try:
                cursor.execute("INSERT INTO Quotes(theme,lines,author) VALUES(?,?,?)",(theme,lines,author))
            # except sqlite3.IntegrityError as e:
            #     print("Duplicate Entry skipped",e)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("Database Error",e)

def main():
    connectDb()
    url="http://www.values.com/inspirational-quotes"
    content=fetchData(url)
    if(content):
        storeData(content)
        print("Stored Data into Database")
    else:
        print("Data Fetching Cancelled")

if __name__=="__main__":
    main()
