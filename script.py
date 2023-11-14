from pyrogram import Client,filters
import time


api_id =  ""
api_hash = "" 


app = Client("account",api_hash=api_hash,api_id=api_id)



@app.on_message(filters.command("otvet", prefixes=".") & filters.me)
def type(_, msg):
    sp_p=[]
    orig_text = msg.text.split(".otvet ", maxsplit=1)[1]
    text = orig_text
    msg.delete()  
    @app.on_message(filters.private)
    def avtootvet(client,message):
        if message.from_user.id not in sp_p:
            if message.chat.type:
                try:
                    app.send_message(chat_id=message.from_user.id,text=text)
                except:
                    pass
                time.sleep(0.25)
                sp_p.append(message.from_user.id)
        else:
            pass




app.run()