from characters import Personagem
from database import p3, p2, p3, p3, p5

turno = 1
while p3.vida > 0 and p2.vida > 0:
    print(f'TURNO: {turno}')
    p3.atacar(p2)
    if p2.vida <= 0:
        print(f"\n{p2.nome} foi derrotado! {p3.nome} é o vencedor!")
        break
    p2.atacar(p3)
    if p3.vida <= 0:
        print(f"\n{p3.nome} foi derrotado! {p2.nome} é o vencedor!")
        break
    turno += 1