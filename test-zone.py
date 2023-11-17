import os


arquivo = open('disciplinas-sexta.txt', 'r')
for linha in arquivo:
    print(linha, end='')
arquivo.close()
