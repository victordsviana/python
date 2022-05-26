f = open("demofile.txt", "r")
arquivo = f.read()
print("Arquivo original")
print(arquivo)
print()
print("Divisão de arquivo por linhas")
lista = arquivo.split("\n")
print(lista)
print()

print("Divisão de cada linha por espaço em branco")
for linha in lista:
    print(linha.split(" "))
