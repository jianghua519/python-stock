import sys
import os

# 获取上上级目录（shared 的父目录）
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
sys.path.append(BASE_DIR)

from fastapi import FastAPI
from shared.logger.logger import get_logger
from shared.database.database import get_db_connection

app = FastAPI()
logger = get_logger("data-ingestor")

@app.get("/")
async def root():
    logger.info("Root API called.")
    return {"message": "Hello from data-ingestor!"}

@app.get("/stocks")
async def get_stocks():
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM stock_prices LIMIT 10")
            result = cursor.fetchall()
        return result
    finally:
        conn.close()
