import ba

ADMIN_PASS = "12345"
ADMINS = set()

def on_chat_message(msg, client_id):
    player = ba.getsession().getplayer(client_id)
    name = player.getname()

    if msg.startswith("!login "):
        password = msg.split(" ")[1]
        if password == ADMIN_PASS:
            ADMINS.add(client_id)
            ba.screenmessage(f"✅ {name} is now an admin!", color=(0,1,0))
        else:
            ba.screenmessage(f"❌ Wrong password, {name}", color=(1,0,0))

    if msg.startswith("!kick "):
        if client_id in ADMINS:
            target = msg.split(" ",1)[1]
            for p in ba.getsession().players:
                if target.lower() in p.getname().lower():
                    ba.disconnect_client(p.inputdevice.client_id)
                    ba.screenmessage(f"🔨 {p.getname()} was kicked by {name}", color=(1,0,0))
        else:
            ba.screenmessage("❌ You are not an admin!", color=(1,0,0))
