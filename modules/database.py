from aiosqlite import connect
from os import mkdir
from sqlite3 import IntegrityError
from aiogram.types.user import User

# async def create_database():
#     try:
#         mkdir('database')
#     except FileExistsError:
#         pass
#     async with connect('database/sdr_e-mails.sql') as conn:
#         cur = await conn.cursor()
#         await cur.execute("CREATE TABLE IF NOT EXISTS emails (user_id INTEGER PRIMARY KEY, username char[50], name char[50], email char[254])")
#         await conn.commit()