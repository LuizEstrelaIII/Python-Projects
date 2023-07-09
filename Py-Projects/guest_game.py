from random import randint

seu_nome = input("Olá, qual o seu nome?")
print(f'okay! {seu_nome}, eu estou escolhendo um número de 1 até 10. Você consegue adivinhar? ')

numero_adivinhado = randint(1,10) 
numero_tentativas = 3

for tentativa in range(1, numero_tentativas + 1):
    numero_escolhido = int(input('Escolha um número: '))
    if numero_escolhido == numero_adivinhado:
        print(f'VOCÊ ACERTEU EM {tentativa} TENTATIVAS!! PARABÉÉÉÉNSSS!!')
        break #"break" para cortar o loop do "if"
    elif numero_escolhido > numero_adivinhado:
        print(f'Escolha um número menor!')
    else:
        print('Escolha um número maior!')
    print('Obrigada por jogar!')

