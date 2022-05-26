f = open("textousuario.txt","a")
conta = 1

while conta <= 5:
    texto = input("Digite texto: ")
    f.write(texto)
    texto = ""
    conta += 1
f.close()

f = open("textousuario.txt", "r")
print(f.read())
f.close()
