from os import getenv
import load_dotenv
import psycopg2
from sqlalchemy import create_engine

load_dotenv.load_dotenv("/home/izzat/PycharmProjects/Modul_6/.env")

engine = create_engine("postgresql://postgres:0@localhost:5433/postgres")


class BotConfig:
    TOKEN = getenv("TOKEN")


class DBConfig:
    NAME = getenv("DBNAME")
    DB_USER = getenv("DB_USER")
    PASSWORD = getenv("PASSWORD")
    HOST = getenv("HOST")
    PORT = getenv("PORT")

    connection = psycopg2.connect(
        dbname=NAME,
        user=DB_USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )
    cursor = connection.cursor()
