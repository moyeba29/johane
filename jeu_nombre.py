nombre_secret = 10
print("=== jeu de nombre mystere ===")
vies = 0
choix = int(input("Devinez le nombre (entre 1 et 20) : "))
while choix > 1 and choix < 20 and vies < 3:
    if choix < nombre_secret:
     choix = int(input("Le nombre est plus grand.")) 
     vies = vies + 1
    elif choix > nombre_secret:
     choix = int(input("Le nombre est plus grand.")) 
     vies = vies + 1
    elif choix ==nombre_secret :
      print("vous avez trouvé le mot juste")

print("nombre de tentative atteint")