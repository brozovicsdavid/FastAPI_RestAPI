from databases import Database
from fastapi import FastAPI
from data import scrape

#create the app
app = FastAPI()

@app.get("/")
async def fetch_data():
    #create the project database
    database = Database('sqlite+aiosqlite:///database.db')
    await database.connect()

    #create the new table
    query1 = "CREATE TABLE imdb (id INTEGER PRIMARY KEY, movie_title VARCHAR(100), ratings FLOAT, year INTEGER, cast VARCHAR(100))"
    await database.execute(query=query1)

    #load the data into the database
    list = []
    query2 = "INSERT INTO imdb(id, movie_title, ratings, year, cast) VALUES (:id, :movie_title, :ratings, :year, :cast)"
    await database.execute_many(query=query2, values=scrape(list))
    
    #get the data from the database and return it with the API call
    query3 = "SELECT * FROM imdb"
    rows = await database.fetch_all(query=query3)
    await database.disconnect()
    return rows