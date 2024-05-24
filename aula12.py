#1
# import os
# with os.scandir("G:/Python/aulas/aula12_teste") as entrada:
#       for arquivo in entrada:
#                 print(f"Diretório encontrado: {arquivo.name}")

#2



#3
# import os
# os.rename("pasta_teste2", "aula12_teste")

#4
# import shutil
# shutil.rmtree("G:/Python/aulas/pasta_teste")

#5
import os
with os.scandir("aula12_teste") as entrada:
    for arquivo in entrada:
        if arquivo.is_file():
            print(f"arquivo encontrado: {arquivo.name}")


#6
# shutil.copytree("G:/Python/aulas/aula12_teste", "copia")









with open ("text.txt","r")as arquivo:
          conteudo = arquivo.read()
          print(conteudo)


