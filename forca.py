import random
import os

#definição das variáveis principais
er = 0
letras = []
escolhe = ''
espacos = 0
pal = []
palavras = ("casa","garrafa","pinto", "batata", "monitor", "impressora", "passarinho", "vaca")

#função inicia o jogo.
def es():
	os.system('cls')
	global escolhe
	global pal
	global espacos
	global letras
	pal = []
	letras = []
	escolhe = ''
	escolhe = random.choice(palavras)
	espacos = len(escolhe)

	for i in escolhe:
		pal.append("-")

	print('Jogo da Forca!\n')
	print("-------\n       |\n\n\n\n\n")
	print('A palavra tem ',espacos, ' letras\n\n')
	for i in pal:
		print(i, end='')

#função que atualiza e resesenha a forca a cada jogada
def desenhaForca(err):
	print('Jogo da Forca!\n')
	forca = "-------\n       |\n"
	if err != 0:
		for i in range(err + 1):
			if i == 1:
				forca += "       O\n"
			if i == 2:
				forca += "      /"
			if i == 3:
				forca += "|"
			if i == 4:
				forca += "\ \n"
			if i == 5:
				forca += "      /"
			if i == 6:
				forca += " \ \n\n"
	print(forca)

#função que atualiza e reescreve a palavra substituindo os traços pelas letras correspondentes
def reescrevePalavra():
	global espacos
	global pal
	print('\n\nA palavra tem ',espacos, ' letras\n\n\n')
	 
	ind = 0
	for i in range(espacos):
		for j in letras:
			if j == escolhe[i]:
				pal[ind] = j
				break
			else:
				pal[ind] = "-"
		ind += 1
	for i in pal:
		print(i, end='')

#chama a função inicial
es()

#laço principal
while True:
	resp = input('\n\ndigite uma letra.\n')
	letras.append(resp)
	if resp not in escolhe:
		er += 1
	
	
	os.system('cls')
	desenhaForca(er)
	reescrevePalavra()
	print('\n\n\nletras escolhidas:\n\n', letras)
	ppe = ''
	for i in pal:
		ppe += str(i)
 
	if ppe == escolhe:
		print("Você Ganhou!!!\nParabéns\n\n")
		rr = input('Deseja jogar novamente?\nPressione S para sim, ou pressione qualquer tecla para encerrar. ')
		if rr.lower() == 's':
			er = 0
			es()
			
			
		else:
			break
	if er > 6:
		print('Você Perdeu!\n\n')
		rr = input('Deseja jogar novamente?\nPressione S para sim, ou pressione qualquer tecla para encerrar. ')
		if rr.lower() == 's':
			er = 0
			es()
			
		else:
			break



	



	
