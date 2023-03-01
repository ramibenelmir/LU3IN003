from traceFunc import *

print("Instances_genome\Inst_0000010_44.adn")
_, _, x, y = readFile("Instances_genome\Inst_0000010_44.adn")
print("distance d'édition : ", DIST_NAIF(x, y))

print("Instances_genome\Inst_0000010_7.adn")
_, _, x, y = readFile("Instances_genome\Inst_0000010_7.adn")
print("distance d'édition : ", DIST_NAIF(x, y))

print("Instances_genome\Inst_0000010_8.adn")
_, _, x, y = readFile("Instances_genome\Inst_0000010_8.adn")
print("distance d'édition : ", DIST_NAIF(x, y))

trace_courbe_tacheA("Instances_genome\\")
trace_courbe_tacheB("Instances_genome\\")

# Comparaison entre les résultats de DIST_1 et ceux de DIST_2
tailleB, tempsB = trace_courbe_DIST_1("Instances_genome\\")
tailleC, tempsC = trace_courbe_DIST_2("Instances_genome\\") # Dist2
fig = plt.figure()
fig.suptitle("Comparaison entre DIST_1 et DIST_2")
plt.plot(tailleB, tempsB)
plt.plot(tailleC, tempsC)
plt.legend(['DIST_1', 'DIST_2'])
plt.show()


trace_courbe_tacheD("Instances_genome\\")


# Question 30
_, _, x, y = readFile("Question30\\Instance_0010000_5.adn")
print(DIST_2(x,y))
_, _, x, y = readFile("Question30\\Instance_0015000_9.adn")
print(DIST_2(x,y))
_, _, x, y = readFile("Question30\\Instance_0020000_12.adn")
print(DIST_2(x,y))