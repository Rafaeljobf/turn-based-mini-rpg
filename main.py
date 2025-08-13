from characters import Personagem
from database import p1, p2, p3, p4, p5

while p1.vida > 0 and p4.vida > 0:
    while True:
        print()
        print(f'\n--- TURNO DE {p4.nome.upper()} ---')
        print(f'Vida: {p4.vida} | Mana: {p4.mana}')
        escolha = input('Escolha sua ação: \n1 - Ataque Normal \n2 - Bola de Fogo (-50 Mana)\n3 - Meditar (+30 Mana) \n\nSua ação: ')

        acao_bem_sucedida = False 

        if escolha == '1':
            acao_bem_sucedida = p4.atacar(p1)
        elif escolha == '2':
            acao_bem_sucedida = p4.lancar_bola_de_fogo(p1)
        elif escolha == '3':
            acao_bem_sucedida = p4.meditar()
        else:
            print("\n!!! Opção inválida! Tente novamente. !!!\n")
            continue

        if acao_bem_sucedida:
            p4.mana += 5
            break 
        else:
            print("\n!!! Ação falhou! Tente outra coisa. !!!\n")

    if p1.vida <= 0:
        print(f'{p1.nome} foi DERROTADO! {p4.nome} É O VENCEDOR!')
        break
    
    while True:
        print(f'\n--- TURNO DE {p1.nome.upper()} ---')
        print(f'Vida: {p1.vida} | Fé: {p1.fe}')
        escolha = input('Escolha sua ação: \n1 - Ataque Normal \n2 - Cura Sagrada (10 Fé) \n\nSua ação: ')

        acao_bem_sucedida = False

        if escolha == '1':
            acao_bem_sucedida = p1.atacar(p4)
        elif escolha == '2':
            acao_bem_sucedida = p1.cura_sagrada()
        else:
            print("\n!!! Opção inválida! Tente novamente. !!!\n")
            continue

        if acao_bem_sucedida:
            p1.fe += 2
            break 
        else:
            print("\n!!! Ação falhou! Tente outra coisa. !!!\n")

    if p4.vida <= 0:
        print(f'{p4.nome} foi DERROTADO! {p1.nome} É O VENCEDOR!')