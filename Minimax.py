import random
import copy

bile = []  # vectorul de bile
sequence = []  # secventa aleasa

lista_cul = ["red", "green", "blue", "white", "yellow", "orange", "violet", "pink"]  # lista de culori disponibile


# subounctul 1
# functia de initializare care primeste ca parametrii n culori diferite,  m bile de fiecare culoare si (A alege) k bile
def init(n, m, k):
    j = 0
    k2 = 0
    global bile
    global sequence
    bile = [None] * m * n
    for i in range(0, n * m):
        bile[i] = lista_cul[j]
        k2 += 1
        if k2 == m:
            k2 = 0
            j += 1
    sequence = select(m, n, k)


# functia care verifica daca cei doi vectori sunt egali
# (o stare primită ca parametru este finală)
def check(vec1, vec2):
    return vec1 == vec2


# subpunctul 2
# functia care  alege aleator k bile din cele m*n disponibile
def select(m, n, k):
    temp_vector = [None] * k
    x = m * n
    alegere = random.sample(range(0, x - 1), k)
    # print(alegere)
    for i in range(0, k):
        temp_vector[i] = bile[alegere[i]]
    return temp_vector


# subounctul 3
# compară o secvență de k culori cu secvența generată de funcția anterioară și întoarce o valoare între 0 și k
# corespunzătoare numărului de potriviri între cele două șiruri.
def compare(vec1, vec2):
    count = 0
    for i in range(0, len(vec1)):
        if vec1[i] == vec2[i]:
            count = count + 1
    return count


# subounctul 4
# o interfata in terminal pentru jucatorul b care acesta da o secventa de culorii
# afișarea numărului de potriviri și afișarea câștigătorului jocului.
def interface(n):
    i = 0
    while i < 2 * n:
        x = input("Introdu secventa de culori: ")
        culori = x.split()
        for j in culori:
            if j not in lista_cul or len(culori) != len(sequence):
                print("Nu este o culoare din lista sau nu ai dat lungimea corecta")
                i -= 1
                break
        if check(culori, sequence):
            return print("A castigat jucatorul B")
        else:
            print(compare(culori, sequence))
            i += 1
    return print("Ai pierdut! A castigat jucatorul A!")

# zice daca inputul este valid
def valid(culori):
    for j in culori:
        if j not in lista_cul or len(culori) != len(sequence):
            # print("Nu este o culoare din lista sau nu ai dat lungimea corecta")
            return False
    return True


def minimax(state, depth, alpha, beta, player):
    if check(state, sequence) is True or depth == 0:            #daca starea e finala sau adancimea e 0 returneaza starea si nr de matchuri
        return compare(state, sequence), state
    if player == 0:                                 #daca e juctaorul B
        temp = -1
        max_state = None
        for neighbour in get_neighbours(state):             # iteram prin vecinii starii
            if neighbour != sequence:                       # daca vecinul nu e stare finala atunci reapelam functia minimax
                score, new_state = minimax(neighbour, depth - 1, alpha, beta, abs(player-1))
                # print(get_neighbours(new_state))
                if score > temp:
                    temp = score
                    max_state = new_state
                alpha = max(alpha, score)
                if score >= beta:
                    break
            else:                                                       #daca vecinul e stare finala, o alege si returneaza
                return compare(neighbour, sequence), neighbour
        return temp, max_state
    else:
        temp = 1024
        min_state = None
        for neighbour in get_neighbours(state):  # iteram prin vecinii starii
            if neighbour != sequence:  # daca vecinul nu e stare finala atunci reapelam functia minimax
                # print("here")
                score, new_state = minimax(neighbour, depth - 1, alpha, beta, abs(player - 1))
                # print(get_neighbours(new_state))
                if score < temp:
                    temp = score
                    min_state = new_state
                beta = min(beta,score)
                if score <= alpha:
                    break
                if score > alpha:
                    alpha = score
            else:  # daca vecinul e stare finala, o alege si returneaza
                return compare(neighbour, sequence), neighbour
        return temp, min_state

#functia ce returneaza toti vecinii unei stari
def get_neighbours(state):
    neighbours = list()
    for i in range(len(state)):
        for color in lista_cul:             #verifica pentru fiecare culoare din cele disponibile, daca e diferita o inlocuieste
            if state[i] != color:           # si daca e valida acea schimbare, o adauga la lista de vecini
                neighbour = copy.deepcopy(state)
                neighbour[i] = color
                if valid(neighbour):
                    neighbours.append(neighbour)
    return neighbours


def interface_minimax(n, m, k):
    state = select(m, n, k)
    print("Miscarea ta initiala este: ")
    print(state)
    print("Ai ghicit : ")
    print(compare(state, sequence))
    score, state = minimax(state, 2*n, -100, 100, 1)
    print("Starea la iesire din Minimax: ")
    print(state)
    print("Solutia era: ")
    print(sequence)
    if check(state, sequence) is True:
        print("A castigat jucatorul B")
    else:
        print("A castigat jucatorul A")


# apelurile fct
init(4, 2, 4)
# print(bile)
print("Secventa jucatorului A este: ")
print(sequence)
interface_minimax(4, 2, 4)
