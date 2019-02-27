from random import randit
computador = randit(0, 5)
print('-=-'*25)
print('Vou pensar em um número entre 0 e 5. Tente Advinhar...')
print('-=-'*25)
jogador = int(input('Em que número pensei? '))
if jogador == computador:
	print('Parabéns! você me venceu!')
else:
	print('Ganhei! eu pensei {} e não em {}!'.format(computador, jogador))
	
 