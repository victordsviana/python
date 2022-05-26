f = open("demofile.txt", "r")
#printa a primeira linha
arquivo = f.readline()
#entra no loop até que uma linha vazia seja detectada
while arquivo != "":
    print("Linha original")
    #printa o arquivo
    print(arquivo)
    #lê a nova linha do arquivo
    arquivo = f.readline()
f.close()
