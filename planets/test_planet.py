from planet import *

earth = planet("Earth", "blue", 4.26e-5)
luna = moon("Luna", "white", 1.16e-5, True, earth)
jupiter = planet("Jupiter", "red", 12345)
europa = moon("Europa", "white", 1560, True, jupiter)
saturn = planet("Saturn", "yellow", 0.00389)
hyperion = moon("Hyperion", "white", 1561, True, saturn)

def test_planet():
    luna.update_planet()
    moon = earth.moon_list[0]
    assert luna.name == "Luna"
    europa.update_planet()
    moon2 = jupiter.moon_list[0]
    assert europa.name == "Europa"
    hyperion.update_planet()
    moon3 = saturn.moon_list[0]
    assert hyperion.name == "Hyperion"
