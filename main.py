import emoji
from time import sleep
from random import randint
print('''suas opções:
[1] PEDRA
[2] PAPEL
[3] TESOURA''')
pc = randint(1, 3)
opcao = int(input('faça sua jogada: '))
sleep(1)
print('JO' + emoji.emojize(' 🖐️'))
sleep(1)
print('KEN' + emoji.emojize(' 👊'))
sleep(1)
print('PO' + emoji.emojize(' ✌️'))
sleep(2)
print('='*20, 'PROCESSANDO', '='*20)
sleep(2)
# opção do jogador
if opcao == 1:
    print(emoji.emojize('voce escolheu PEDRA 👊'))
elif opcao == 2:
    print(emoji.emojize('voce escolheu PAPEL  🖐️'))
elif opcao == 3:
    print(emoji.emojize('voce escolheu TESOURA ✌'))
else:
    print('\033[7;31;40m opção invalida \033[m')
sleep(2)
# escolha ramdomica
if pc == 1:
    print(emoji.emojize('O computador escolheu PEDRA 👊'))
elif pc == 2:
    print(emoji.emojize('O computador escolheu PAPEL  🖐️'))
elif pc == 3:
    print(emoji.emojize('O computador escolheu TESOURA ✌'))
sleep(2)
# Resultado do jogo
if opcao == 1 and pc == 1:
    print('o jogo \033[0;30;43m EMPATOU \033[m')
elif opcao == 1 and pc == 2:
        print('voce \033[7;31;40m VOCE PERDEU \033[m')
elif opcao == 1 and pc == 3:
    print('voce \033[0;30;42m GANHOU \033[m')
elif opcao == 2 and pc == 2:
    print('o jogo \033[0;30;43m EMPATOU \033[m')
elif opcao == 2 and pc == 1:
    print('voce \033[0;30;42m GANHOU \033[m')
elif opcao == 2 and pc == 3:
    print('voce \033[7;31;40m VOCE PERDEU \033[m')
elif opcao == 3 and pc == 3:
    print('o jogo \033[0;30;43m EMPATOU \033[m')
elif opcao == 3 and pc == 2:
    print('voce \033[0;30;42m GANHOU \033[m')
elif opcao == 3 and pc == 1:
    print('voce \033[7;31;40m VOCE PERDEU \033[m')
