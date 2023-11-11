from pyrogram import Client, filters
import time
import sqlite3

api_id = "---------"
api_hash = "-----------"

app = Client("account", api_hash=api_hash, api_id=api_id)

def create_connection():
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    return conn, cursor

prepared_message = """Hello, i am egor. please wait me for my free time,i call you at the moment""" 

@app.on_message(filters.command("otvet", prefixes=".") & filters.me)
def type(_, msg):
    msg.delete()
5
@app.on_message(filters.private)
def avtootvet(client, message):
    user_id = message.from_user.id

    conn, cursor = create_connection()

    try:
        cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
        user_exists = cursor.fetchone()

        if not user_exists:
            if message.chat.type:
                try:
                    app.send_message(chat_id=user_id, text=prepared_message)
                except:
                    pass
                time.sleep(0.25)
                cursor.execute('INSERT INTO users (user_id) VALUES (?)', (user_id,))
                conn.commit()

    finally:
        conn.close()

app.run()
