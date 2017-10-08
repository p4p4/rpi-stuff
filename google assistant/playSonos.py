import soco

for zone in soco.discover():
  print("name: " + zone.player_name + ", IP: " + zone.ip_address)

player = soco.SoCo("192.168.0.94")
player.play_uri('http://patrick-thinkpad-x230.local:8080/out.wav')

