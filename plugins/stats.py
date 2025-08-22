import ba

PLAYER_STATS = {}

def on_player_join(player):
    PLAYER_STATS[player.getname()] = {"kills": 0, "deaths": 0}
    ba.screenmessage(f"📊 Stats tracking started for {player.getname()}")

def on_player_kill(killer, victim):
    if killer and killer.getname() in PLAYER_STATS:
        PLAYER_STATS[killer.getname()]["kills"] += 1
    if victim and victim.getname() in PLAYER_STATS:
        PLAYER_STATS[victim.getname()]["deaths"] += 1
