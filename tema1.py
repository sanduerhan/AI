def init(nrcouples):
    pozitii = [0 for i in range(2 * nrcouples+1)]
    return pozitii


#verifica daca o stare este finala
def check(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            return False
    return True

#functia de miscare a persoanelor de pe un mal pe altul
def move(arr, positions):
        if arr[-1] == 0:
            for i in positions:
                arr[i] = 1
            arr[-1] = 1
            return arr
        elif arr[-1] == 1:
            for i in positions:
                arr[i] = 0
            arr[-1] = 0
            return arr

#functia ce ne arata daca exista gelozie pe un mal dupa o tranzitie
def jealousy(arr):
    for i in range(0, nrCouples):  # parcurgem sotiile
        if arr[i] != arr[i + nrCouples]:  # daca cuplul este pe maluri diferite
            for j in range(nrCouples, nrCouples * 2):   #parcurgem sotii si verificam daca este vreounul pe acelasi mal cu sotia
                if arr[i] == arr[j]:
                    return True
    return False

#c)
#functia de validare a tranzitiei
def validmove(arr, positions):
    arr2 = list(arr)
    if len(positions) > 2 or len(positions) == 0:       #minim o persoana in barca si maxim doua
        return False
    else:
        for i in positions:
            if arr[-1] != arr[i]:         #daca persoanele nu sunt pe acelasi mal cu barca, returneaza false
                return False
    if jealousy(move(arr2, positions)):      #daca miscarea este valida, o executa si returneaza true
        #print("before: ", arr, "After: ", arr2)
        return False
    else:
        move(arr, positions)
        return True

#functia ce gaseste toate miscarile posibile pornind de la o stare din coada
def possiblemoves(arr, queue, visited):
    allpositions = []       #salvam pozitiile persoanelor pentru a vedea daca le putem muta cu barca
    #parents = []
    for i in range(0, nrCouples*2):     #luam pe rand fiecare persoana in parte
        arrcopy = list(arr)
        allpositions.append(i)
        if validmove(arrcopy, allpositions):      #daca miscarea e valida si daca starea nu e vizitata
            if not(arrcopy in visited):
                queue.append(arrcopy)                   #adaugam starea in coada si o marca vizitata si verificam daca e stare finala
                visited.append(arrcopy)
                #parents.append(visited.index(arr))      #vectorul unde salvam tranzitiile corecte spre solutie
                #if check(queue[-1]):
                    #temp = parents[-1]
                    ##while(temp!=0):
                     #   print(arr[temp])
                     #   temp = parents[arr.index(arr[temp])]
                    #print("solutia: ", queue[-1])
                    #return True
        allpositions.remove(i)

    for i in range(0, nrCouples * 2):           #luam combinatii a cate 2 persoane si se repeta aceiasi pasi
        allpositions.append(i)
        for j in range(i + 1, nrCouples * 2):
            arrcopy2 = list(arr)
            allpositions.append(j)
            if validmove(arrcopy2, allpositions):
                if not(arrcopy2 in visited):
                    queue.append(arrcopy2)
                    visited.append(arrcopy2)
                    #if check(queue[-1]):
                      #  print("solutia: ", queue[-1])
                      #  return True
            allpositions.remove(j)
        allpositions.remove(i)


#e)
def BFS(arr):
    queue = [arr]           #initializam coada cu starea initiala
    vizitat = [arr]         #vectorul unde punem starile vizitate
    while len(queue) != 0:      #cat timp coada nu-i goala, cautam toate posibilele miscari incepand cu starea state
        state = queue[0]
        queue.pop(0)
        possiblemoves(state, queue, vizitat)

#d)
def Backtracking(arr,visited):
    allpositions = []
    if check(arr):
        print("Valid:", arr)
        return True
    for i in range(0,nrCouples*2):      #luam pe rand fiecare persoana
        arr2 = list(arr)
        print(arr2)
        allpositions.append(i)
        if validmove(arr2, allpositions):     #daca miscarea e valida si starea nu e vizitata se executa apelu recursiv
            if not (arr2 in visited):
                visited.append(arr2)
                found = Backtracking(arr2,visited)      #cu starea de dupa tranzitie
                del visited[visited.index(arr2)]
                if found:
                    return True
    for i in range(0,nrCouples*2):      #aceiasi pasi pentru perechi de cate 2 persoane
        allpositions.append(i)
        for j in range(i+1, nrCouples):
            arr2 = list(arr)
            print(arr2)
            allpositions.append(j)
            if validmove(arr2, allpositions):
                if not (arr2 in visited):
                    visited.append(arr2)
                    found = Backtracking(arr2,visited)
                    del visited[visited.index(arr2)]
                    if found:
                        return True

def h(state):       #functia euristica- calculeaza pentru o stare numarul de persoane pe malul stang
    result = 0
    for i in range(len(state)-1):
        if state[i] == 0:
            result += 1
    return result


def HC():           # Hill Climbing
    currentNode = initial
    vizitat = [currentNode]
    queue = []
    while True:
        queue.clear()
        possiblemoves(currentNode,queue,vizitat)        #calculam toti vecinii starii currentNode
        print(queue)
        nextEval = 1024
        nextNode = []
        for i in queue:         #iteram prin vecinii lui CurrentNode salvati in queue
            if h(i) < nextEval:     #daca euristica starii curente e mai mica decat euristica unei stari vecine, actualizam si nodul si valoarea
                nextNode = i
                print("Nodul cu euristica mai buna: "+ str(nextNode))
                nextEval = h(i)
                print("Euristica este: "+ str(nextEval))
        if nextEval >= h(currentNode):          #daca euristica cea mai buna a unei stari vecine lui currentnode e >= euristica lui currentnode, o returnam
            print(currentNode)
            return currentNode
        currentNode = nextNode      #actualizam nodul curent


def AStar(initial , goal , h ):
    openSet = [initial]
    gscore = {tuple(initial): 0}
    fscore = {tuple(initial): h(initial)}
    vizitat = [initial]
    queue = []
    result = 0
    while len(openSet) != 0:
        temp = 1024
        for i in openSet:
            if fscore[tuple(i)] < temp:
                temp = fscore[tuple(i)]
                current = i
          #nodul din dictionar cu cel mai mic fscore
        print(current)
        if current == goal:     #daca am ajuns la starea finala, returnam
            print("Solutia gasita: " + str(current))
            return current
        openSet.remove(current)
        queue.clear()
        possiblemoves(current, queue, vizitat)
        for i in queue:     #iteram prin vecinii starii
            for j in range(len(current)):       #calculam distanta
                #print(len(current))
                #print(j)
                result += abs(current[j]-goal[j])
            tentative_gscore = gscore[tuple(current)] + result
            #print(tentative_gscore)
            if gscore.get(tuple(i)) is None:
                gscore[tuple(i)] = 1024
            if tentative_gscore < gscore[tuple(i)]:
                gscore[tuple(i)] = tentative_gscore
                fscore[tuple(i)] = gscore[tuple(i)] + h(i)
                #print("aici")
                if i not in openSet:
                    openSet.append(i)
                    print(openSet)
    return False



while True:


    print("\nsearch strategies:")
    print("\t(1) BFS")
    print("\t(2) Backtracking")
    print("\t(3) Hill Climbing")
    print("\t(4) A*")
    selection = int(input("Select the search strategy : "))
    nrCouples = int(input("Introduceti numarul de cupluri: "))
    initial = init(nrCouples)
    visited = []
    queue = []
    goal = [1 for i in range(nrCouples*2+1)]
    if selection == 1:
        BFS(initial)
    if selection == 2:
        Backtracking(initial, visited)
    if selection == 3:
        HC()
    if selection == 4:
        AStar(initial, goal, h)

#possiblemoves(initial,queue,visited)
#print(queue)
# changes = [0, 2]
# result = move(initial, changes, boat)
# print(result)
# check(pozitii2)
