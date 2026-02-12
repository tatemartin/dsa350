import pandas as pd

df = pd.read_csv('planet_data.csv', index_col='eName')
print(df.head())
data = df[['isPlanet', 'meanRadius', 'orbit_type', 'orbits']]
print(data.head())

planet_d = dict()
moon_d = dict()

class planet():
    def __init__(self,name, color = "blue", radius = 1, moon_list = []):
        self.color = color
        self.radius = radius
        self.name = name
        self.moon_list = []
class moon():
    def __init__(self,name, color = "white", radius = 1,
                     tidally_locked=False, planet_companion=None):
        self.name = name
        self.color = color
        self.radius = radius
        self.tidally_locked = tidally_locked
        self.planet_companion = planet_companion
    def update_planet(self):
        self.planet_companion.moon_list.append(self)

def print_largest(pl):  
    largest = None
    for moon in pl.moon_list:
        if largest is None:
            largest = moon
        else:
            if largest.radius < moon.radius: largest = moon      
    if largest is not None:
        print(f"The largest moon of {pl.name} is {largest.name}")

planet_d = dict() 
moon_d = dict()
for index, row in df.iterrows():
    if row['isPlanet'] is True:
        planet_d[index] = planet( name = index, radius = row['meanRadius'])

for index, row in df.iterrows():
    if row['isPlanet'] is False:
        moon_d[index] = moon( name = index, radius = row['meanRadius'], planet_companion = planet_d[row['orbits']])

for key, val in planet_d.items():
    print(key, val.radius)

for key, val in moon_d.items():
    print(key, val.radius, val.planet_companion)

for key, val in moon_d.items():
    val.update_planet()
    print(key, val.radius, val.planet_companion.name)

for key, val in planet_d.items():
    print_largest(val)
    print(key, [moon.name for moon in val.moon_list])
