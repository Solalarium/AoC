from util import Day

def make_orbit_dict(data):
    orbit = {}
    for i in range(len(data)):
        orbitet,orbiter = data[i].split(')')
        orbit.update({orbiter:orbitet})
    return orbit

def keyfinder(orbit,keys,nr_of_each_orbits,instances):
    instances += 1
    for k in orbit:
        if orbit[k] == keys:
            nr_of_each_orbits.update({k:instances})
            keyfinder(orbit,k,nr_of_each_orbits,instances)
    return nr_of_each_orbits

def way_to_center(orbit,keys,planets):
    for k in orbit:
        if k == keys:
            planets.append(orbit[k])
            way_to_center(orbit,orbit[k],planets)
    return planets

def find_new_center(you,san):
    for i in range(len(you)):
        for j in range(len(san)):
            if you[i] == san[j]:
                return you[i]

def distance_to_center(orbit,keys,halt,distance=-1):
    distance += 1
    if keys == halt:
        return distance
    for k in orbit:
        if orbit[k] == keys:
            answer = distance_to_center(orbit,k,halt,distance)
            if answer != None:
                return answer

def count_orbits(nr_of_each_orbits):
    nr_of_all_orbits = 0
    for k in nr_of_each_orbits:
        nr_of_all_orbits += nr_of_each_orbits[k]
    return nr_of_all_orbits

if __name__ == '__main__':

    # --Part 1-- 139597
    test1 = ['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L']
    part1 = Day(6,1)
    part1.load()

    orbit = make_orbit_dict(part1.data)

    nr_of_each_orbits = keyfinder(orbit,'COM',{},0)

    print(part1.answer(count_orbits(nr_of_each_orbits)))

    # --Part 2-- 286
    test2 = ['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L','K)YOU','I)SAN']
    part2 = Day(6,2)
    part2.load()

    orbit = make_orbit_dict(part2.data)

    you = way_to_center(orbit,'YOU',[])
    san = way_to_center(orbit,'SAN',[])
    new_center = find_new_center(you,san)

    result = distance_to_center(orbit,new_center,'YOU')+distance_to_center(orbit,new_center,'SAN')-2
    print(part2.answer(result))