# from config.config import DBConfig
#
# conn = DBConfig.connection
# cursor = DBConfig.cursor
#
#
# async def save_user_data(teleg_user_id, first_name, last_name) -> None:
#     query = """insert into users (id, first_name, last_name)
#     values (%s, %s, %s);"""
#
#     cursor.execute(query, (teleg_user_id, first_name, last_name))
#     conn.commit()
#
#
# async def save_to_waiting_users(teleg_user_id) -> None:
#     query = """insert into waitingusers (tg_id) values (%s);"""
#
#     cursor.execute(query, [teleg_user_id])
#     conn.commit()
#
#
# async def load_waiting_users() -> list[tuple]:
#     query = """select tg_id from waitingusers;"""
#
#     cursor.execute(query)
#
#     return cursor.fetchall()
