import uvicorn
from data import scrape
from database import app

if __name__ == "__main__":
    scrape()
    uvicorn.run(app, host="127.0.0.1", port=5049)