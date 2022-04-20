'''
rappels
P * V = n * R * T
Ph          = Patm + MasseVo * g * profondeur
profondeur  = (Ph/MasseVo * g) - (Patm/MasseVo * g)
LE PROGRAMME RETOURNE LA PROFONDEUR MAXIMALE A LAQUELLE LE PLONGEUR PEUT ALLER
'''
# VARIABLES
maxFound = False

#  DONNEES DE INVARIABLES
masseVolumiqueEau = float(1030)  # Kilogrammes paer metres cube
g = 9.81

# RECUPERER LA PRESSION ATMOSPHERIQUE
userInput = float(input("Quelle pression fait-il au niveau de la mer ?"))
if (userInput == 0.0) :
    Patm = 101325   # valeur en Pa
else :
        Patm = userInput

# Récupérer la pression maximale
pressionMaxSupportable = float(input("Quelle pression maximale ?"))

#                               ______________ PHASE DEUX ___________________
print("Essayez de deviner la profondeur max!")
res = Patm/(masseVolumiqueEau*g)
resultat1 = pressionMaxSupportable/(masseVolumiqueEau*g) - res
profMax = round(abs(resultat1))
# Récupérer la profondeur
while maxFound == False:
    userInput = input("Quelle profondeur ne doit pas dépasser notre plongeur?")
    profEstime = round(float(userInput))
    diffProf = abs(profEstime - profMax)
    if profEstime == profMax:
        print("Oui c'est bien ça")
        maxFound = True
    elif (profEstime < profMax) :
        print("Le plongeur peut aller plus loin!")
    else:
        print("Le plongeur est allé trop loin")
print(profMax)
