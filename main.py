import random

linhas = 3
colunas = 3
vetor = [0] * colunas
vetor_mapa = ["#"] * colunas
matriz = []
mapa = []
cont = 0


def imprime_mapa (mat, l):
   cont = 0
   while cont < l:
     print(mat[cont])
     cont += 1

def imprime_matriz (mat, l):
   cont = 0
   while cont < l:
     print(mat[cont])
     cont += 1

while cont < linhas:
  matriz.append(vetor.copy())
  mapa.append(vetor_mapa.copy())
  cont += 1

def sorteio():
  for x in range(3):
   lin = random.randint(0, linhas-1 )
   col = random.randint(0, colunas-1)
   while matriz[lin][col] == 1:
      lin = random.randint(0, linhas-1 )
      col = random.randint(0, colunas-1)
   matriz[lin][col] = 1


def jogo (linha, coluna):
  if matriz[linha-1][coluna-1] == 0:
    print("*"*30)
    print("Você não achou Nada!")
    print("*"*30)
    mapa[lin_jogo -1][col_jogo-1] = "X"
  elif matriz[linha-1][coluna-1] == 1:
    print("*"*30)
    print("Parabéns você encontrou algo!")
    print("*"*30)
    mapa[lin_jogo -1][col_jogo-1] = "$"

sorteio()
jogador1 = 0
jogador2 = 0
imprime_matriz(matriz, linhas)

while True:
  print("")
  print("Bora Jogar!")
  print("")
  print("Jogador 1 sua vez!")
  print("-"*30)
  imprime_mapa(mapa,linhas)
  print("")
  col_jogo = int(input("Sinalize a coluna:"))
  lin_jogo = int(input("Sinalize a linha:"))
  print("-"*30)
  jogo(lin_jogo,col_jogo)
  if matriz[lin_jogo -1][col_jogo-1] == 1:
    jogador1 += 1
  print(f'Você esta com: {jogador1} pontos')
  if jogador1 == 2:
   print("Jogador 1 Venceu. Parabéns!")
   break

  print("")
  print("Bora Jogar!")
  print("")
  print("Jogador 2 sua vez")
  print("-"*30)
  imprime_mapa(mapa,linhas)
  print("")
  col_jogo = int(input("Sinalize a coluna:"))
  lin_jogo = int(input("Sinalize a linha:"))
  print("-"*30)
  jogo(lin_jogo,col_jogo)
  if matriz[lin_jogo -1][col_jogo-1] == 1:
    jogador2 += 1
  print(f'Você esta com: {jogador2} pontos')
  if jogador2 == 2:
   print("Jogador 2 Venceu. Parabéns!")
   break
 
