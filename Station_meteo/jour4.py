fd = open("monfichier.txt","a")
fd.write("Bonjour \n")
fd.write("Ceci est un fichier text\n")
fd.close()

fd = open("monfichier.txt","r")
print("DEBUT DE LECTURE")
for line in fd:
	print(line)
print("FIN DE LECTURE")
fd.close()
