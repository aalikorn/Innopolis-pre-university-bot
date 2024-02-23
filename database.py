import sqlite3 as sq

db = sq.connect('person.db')
cur = db.cursor()


async def db_start():
    global db, cur
    cur.execute("CREATE TABLE IF NOT EXISTS person(user_id TEXT PRIMARY KEY, name TEXT, surname TEXT, mail TEXT)")
    db.commit()


async def create_profile(user_id):
    user = cur.execute(f"SELECT 1 FROM person where user_id == {user_id}").fetchone()
    if not user:
        cur.execute("INSERT INTO person VALUES(?, ?, ?, ?)", (user_id, '', '', ''))
        db.commit()


async def edit_profile(data, user_id):
    cur.execute(f"UPDATE person SET name = ?, surname = ?, mail = ? WHERE user_id == ?", (data[0], data[1], data[2], user_id))
    db.commit()

