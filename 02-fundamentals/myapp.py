import mymodule as phy

EARTH_GRAVITY = 9.807 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62 #? měsíční gravitace

print("Světlo urazí vzdálenost 300 000 km za " + str(phy.time_by_light_speed(300000)) + "s")

print("Zvuk urazí vzdálenost 3 000 km za " + str(round(phy.time_by_sound_speed(3000))) + "s")

print("Hydrostaticky tlak v hloubce 10m ve vodě o hustotě 1000kg/m3 na naší planetě je " +
      str(phy.hydrTlak(10, 1000, EARTH_GRAVITY)) + " Pa")

print("Hmotnost 1000kg na Zemi je na Měsíci " +
      str(round(phy.hmotnostNaMesici(1000, EARTH_GRAVITY, MOON_GRAVITY))) + " kg")