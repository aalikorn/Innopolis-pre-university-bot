import sqlite3 as sq

db = sq.connect('person.db')
cur = db.cursor()


async def db_start():
    global db, cur
    cur.execute("CREATE TABLE IF NOT EXISTS person(user_id TEXT PRIMARY KEY, name TEXT, surname TEXT, phone TEXT, mail TEXT, birth_date TEXT, grade INT, interests INT, conf TEXT, adds TEXT)")
    db.commit()


async def create_profile(user_id):
    user = cur.execute(f"SELECT 1 FROM person where user_id == {user_id}").fetchone()
    if not user:
        cur.execute("INSERT INTO person VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (user_id, '', '', '', '', '', 0, 0, '', ''))
        db.commit()


async def edit_profile(data, user_id):
    await create_profile(user_id)
    print(data)
    cur.execute(f"UPDATE person SET name = ?, surname = ?, phone = ?, mail = ?, birth_date = ?, grade = ?, interests = ?, conf = ?, adds = ? WHERE user_id == ?", (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], user_id))
    db.commit()


async def is_exists(user_id) -> bool:
    user = cur.execute(f"SELECT 1 FROM person where user_id == {user_id}").fetchone()
    if not user: return False
    return True