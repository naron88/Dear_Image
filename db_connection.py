import os
import mysql.connector
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

def connect_to_database():
    try:
        # MySQL 연결 설정
        mydb = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
        )
        return mydb
    except mysql.connector.Error as err:
        print("MySQL 연결 오류:", err)
        return None
