import random
graph = {}
f = open('Graph.txt', 'r')
for row in f:
    row = row.split(' ')
    k = 0
    graph[row[k]] = list()
    for i in range(len(row)):
        if row[k] != row[i]:
            graph[row[k]].append(row[i].strip())
    k += 1

colors = {}
#Exemplul 2
colors['WA'] = ['red']
colors['SA'] = ['red', 'green', 'blue']
colors['NT'] = ['green', 'red', 'blue']
colors['Q'] = ['green']
colors['NSW'] = ['red', 'green', 'blue']
colors['V'] = ['green', 'red', 'blue']
colors['T'] = ['green', 'red', 'blue']
#Exemplul 1
# colors['WA'] = ['red', 'green', 'blue']
# colors['SA'] = ['red', 'green']
# colors['NT'] = ['green']
colors2 = {}
for i in colors:
    colors2[i] = colors[i]
def FC(region):
    result = {}
    i = 1
    global colors
    while len(graph) >= i > 0:
        x_i = select_value(region)      #selecteaza o culoare din domeniu consistenta
        if x_i is None:
            i = i - 1
        else:                       #daca culoarea a fost selectata, coloram regiunea
            i = i + 1
            result[region] = x_i
            print(result)
        for k in graph.keys():      #scoatem regiunea colorata din vecinii celoralte regiuni
            if k != region:
                if region in graph[k]:
                    graph[k].remove(region)
        for r in graph[region]:             #lua urmatoarea regiune
            region = r
        if len(colors[region]) == 0 and region not in result:        #daca domeniul este vid -> problema este inconsistenta
            print(region + " Domeniul de culori este vid")
            print("Problema inconsistenta")
            return "Problema inconsistenta"

    if i == 0:
        print("Problema inconsistenta")
        return "Problema inconsistenta"
    else:
        print(result)
        return result


def select_value(region):

    while len(colors2[region]) != 0:
        value = random.choice(colors2[region])      #luam o culoare random din domeniu
        #print(region)
        vizitat = {}
        #print(value)
        colors2[region].remove(value)       #scoatem culoarea din domeniu
        vid = False
        for k in graph[region]:
            for b in colors2[k]:
                if not asignare(region, value, k, b):       #verificam daca asignarea cu culoarea selectata este valida
                    colors2[k].remove(b)        #daca nu e valida, scoatem culoarea din domenii
                    #print("Aici este colors2")
                    #print(colors2)
                    vizitat[k] = b
            if len(colors2[k]) == 0 and len(colors2[region]) > 0:
                print("Lungimea e 0")
                vid = True
            elif len(colors2[k]) == 0 and len(colors2[region]) == 0:
                print(region)
                return None
        #print(vizitat)
        if vid:
            for key in colors2.keys():
                if key in vizitat.keys():
                    #print(colors2[key])
                    #print(vizitat)
                    colors2[key].append(vizitat[key])
            #print("Aici tot este colors")
            #print(colors2)
        elif not vid:
            return value
    return None

def asignare(region, color, region2, color2):
    if region2 in graph[region]:
        if color == color2:
            return False
    return True

result = {}
def mrv():
    if len(result) == len(graph):
        return result
    var = minim()
    for key in result.keys():       #verifica daca nu se respecta constrangerile
        if key in graph[var]:
            for color in colors[var]:
                list_1 = color.split()
                #print(list_1)
                #print(result[key])
                if color == result[key]:
                    colors[var].remove(color)
    if len(colors[var]) == 0:       #daca domeniul este vid -> problema este inconsistenta
        print(var + " Problema inconsistenta, domeniul este 0")
        return None
    value = random.choice(colors[var])
    result[var] = value
    print(result)
    rez = mrv()
    if rez != None:
        return rez



cities = {}
for key in graph.keys():
    cities[key] = None

def minim():        #functia ce selecteaza regiunea cu nr minim de culori
    cities_without_color = []
    allowed_colors = {}
    for key in graph.keys():
        if cities[key] is None:
            cities_without_color.append(key)
    #print(cities_without_color)
    for city in cities_without_color:
        allowed_colors[city] = len(colors[city])
    minimum = 100
    for allowed in allowed_colors.keys():
        if minimum > allowed_colors[allowed]:
            minimum = allowed_colors[allowed]
    for city, length in allowed_colors.items():
        if length == minimum:
            cities[city] = 1
            return city

FC("WA")
#mrv()
