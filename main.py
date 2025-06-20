# main.py

import asyncio
from scraper import scrape_chapter

if __name__ == "__main__":
    # Run the asynchronous scraper function
    asyncio.run(scrape_chapter())
