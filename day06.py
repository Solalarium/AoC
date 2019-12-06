from util import Day

# --Part 1--
test = ['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L']
part1 = Day(6,1)
part1.load()


def placeholder():
    orbit = {}
    nr_of_orbits = {}
    orbits = 0

    for i in range(len(part1.data)):
        orbitet,orbiter = part1.data[i].split(')')
        orbit.update({orbiter:orbitet})

    nr_of_orbits = keyfinder(orbit,'COM',nr_of_orbits,0)

    for k in nr_of_orbits:
        orbits += nr_of_orbits[k]


    return part1.answer(orbits)

def keyfinder(orbit,keys,nr_of_orbits,instances):
    instances += 1
    for k in orbit:
        if orbit[k] == keys:
            nr_of_orbits.update({k:instances})
            keyfinder(orbit,k,nr_of_orbits,instances)
    return nr_of_orbits

print(placeholder())
