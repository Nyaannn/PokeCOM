if __name__ == "":
 from JsMacrosAC import *
import math
import requests
webhook=''
#get baritone classes
BaritoneAPI = Reflection.getClass("baritone.api.BaritoneAPI")
bapi = BaritoneAPI.getProvider().getPrimaryBaritone()
baritone = bapi.getCommandManager()
ents = World.getEntities()
#get all loaded players and players in tab

players = World.getLoadedPlayers()
player_name = Player.getPlayer().getName().getString()
for l in players:
   #event set to player on join 
   #when the player join it gets uuid and the uuid of loaded players
   #if its true it goes
   uuid = l.getUUID()
   plr = event.UUID
   if uuid == plr:
     x = math.floor(l.getX())
     y = math.floor(l.getY())
     z = math.floor(l.getZ())
     nbt = l.getNBT()
     if x != -0:
      if y != 0:
       if z != -0:
            serverip=World.getCurrentServerAddress()
              #api request to get plr name because jsmacros broke playernames
            e = requests.get(f"https://api.mojang.com/user/profile/{plr}").json()
            name = e['name']
            Chat.log(f'[\u00A7cPiss\u00A7fBox]-\u00A7e - Name:{name}, UUID: {plr}, X:{x}, Y:{y}, Z:{z}')
            #asscheeks wp system
            def waypoint():
                import math
                h3d = Hud.createDraw3D()
                line = h3d.addLine(x, 1, z, x+1, 128, z+1, 0xff0000)
                h3d.register()
            waypoint()

            coordlog = f' IP:{serverip}, Name:{name}, UUID: {plr}, X:{x}, Y:{y}, Z:{z}' 
            baritone.execute(f'wp save user {name} {x} {y} {z}')
            #send to discord webhook

            payload = {"payload_json": '{"username": "PissBox", "avatar_url": "", "content": "'+ coordlog +'","embeds": [], "components": []}'}
            requests.post(webhook,data=payload)
