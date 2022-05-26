#R = read; A = append; W = write

f = open("demofile2.txt", "a")
f.write("pq na casa nao tinha chao\n")
f.write("\nappend adiciona conteúdo, sem excluir o que havia antes")
f.close

f = open("demofile2.txt", "r")
print(f.read())


f = open("demofile2.txt", "w")
f.write("write apaga tudo, e só deixa o que você escrever")
f.close

f = open("demofile2.txt", "r")
print(f.read())
