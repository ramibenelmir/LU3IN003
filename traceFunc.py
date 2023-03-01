from tacheA import *
from tacheB import *
from tacheC import *
from tacheD import *

def readFile(path):
    adn = open(path)
    i = adn.readline()
    j = adn.readline()
    x = adn.readline().split()
    y = adn.readline().split()
    return i, j, x, y

def trace_courbe_tacheA(dossier):
    path = ""
    taille = []
    temps = []
    for filename in os.scandir(dossier):
        if filename.is_file():
            path = filename.path
            print(path)
            i, _, x, y = readFile(path)

            start = time.time()
            DIST_NAIF(x, y)
            end = time.time()
            temps_total = end - start
            print("le temps est : ", temps_total)


            if temps_total > 60:
                print("l'exécution de ", path, " a pris ", temps_total, " seconds qui est plus d'une minute")
                break
            taille.append(i)
            temps.append(temps_total)
            
    plt.plot(taille, temps)
    plt.legend(['Tâche A'])
    plt.xlabel("|x|")
    plt.ylabel("Temps (s)")
    plt.show()
    return taille, temps

def trace_courbe_tacheB(dossier):
    taille = []
    temps = []

    for filename in os.scandir(dossier):
        if filename.is_file():

            path = filename.path
            print(path)
            i, _, x, y = readFile(path)

            start = time.time()
            PROG_DYN(x, y)
            end = time.time()
            temps_total = end - start
            print("le temps est : ", temps_total)
            if temps_total > 600:
                print("l'exécution de ", path, " a pris ", temps_total, " seconds qui est plus de dix minutes")
                break
            taille.append(i)
            temps.append(temps_total)
    fig = plt.figure()
    fig.suptitle("Consommation du temps CPU pour Tâche B")
    plt.plot(taille, temps)
    plt.legend(['Tâche B'])
    plt.xlabel("|x|")
    plt.ylabel("Temps (s)")
    plt.show()
    return taille, temps

def trace_courbe_DIST_1(dossier):
    taille = []
    temps = []

    for filename in os.scandir(dossier):
        if filename.is_file():
            
            path = filename.path
            print(path)
            i, j, x, y = readFile(path)
            T = np.zeros((len(x)+1,len(y)+1),dtype=int)

            start = time.time()
            DIST_1(x, y, T)
            end = time.time()
            temps_total = end - start
            print("le temps est : ", temps_total)
            if temps_total > 600:
                print("l'exécution de ", path, " a pris ", temps_total, " seconds qui est plus de deix minutes")
                break
            taille.append(i)
            temps.append(temps_total)
    fig = plt.figure()
    fig.suptitle("Consommation du temps CPU pour DIST_1")
    plt.plot(taille, temps)
    plt.legend(['DIST_1'])
    plt.xlabel("|x|")
    plt.ylabel("Temps (s)")
    plt.show()
    return taille, temps

def trace_courbe_DIST_2(dossier):
    taille = []
    temps = []

    for filename in os.scandir(dossier):
        if filename.is_file():

            path = filename.path
            print(path)
            i, _, x, y = readFile(path)

            start = time.time()
            DIST_2(x, y)
            end = time.time()
            temps_total = end - start
            print("le temps est : ", temps_total)
            if temps_total > 600:
                print("l'exécution de ", path, " a pris ", temps_total, " seconds qui est plus de dix minutes")
                break
            taille.append(i)
            temps.append(temps_total)
    fig = plt.figure()
    plt.plot(taille, temps)
    plt.legend(['DIST_2'])
    fig.suptitle("Consommation du temps CPU pour DIST_2")
    plt.xlabel("|x|")
    plt.ylabel("Temps (s)")
    plt.show()
    return taille, temps

def trace_courbe_tacheD(dossier):
    taille = []
    temps = []

    for filename in os.scandir(dossier):
        if filename.is_file():

            path = filename.path
            print(path)
            i, _, x, y = readFile(path)

            start = time.time()
            coupure(x, y)
            end = time.time()
            temps_total = end - start
            print("le temps est : ", temps_total)
            if temps_total > 600:
                print("l'exécution de ", path, " a pris ", temps_total, " seconds qui est plus de dix minutes")
                break
            taille.append(i)
            temps.append(temps_total)
    fig = plt.figure()
    fig.suptitle("Consommation du temps CPU pour Tâche D")
    plt.plot(taille, temps)
    plt.legend(['Tâche D'])
    plt.xlabel("|x|")
    plt.ylabel("Temps (s)")
    plt.show()
    return taille, temps