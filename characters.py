class Personagem:
    def __init__(self, nome, vida, dano):
        self.nome = nome
        self.vida = vida
        self.dano = dano
    
    @property
    def vida(self):
        return self._vida
    
    @vida.setter
    def vida(self, valor):
        if valor < 0:
            self._vida = 0
        elif valor > 100:
            self._vida = 100
        else:
            self._vida = valor

    
    def __str__(self):
        return f'Classe: {self.nome} / Nível: {self.nivel} / Vida: {self._vida} / Dano: {self.dano}' 

    def receber_dano(self, quantidade):
        nova_vida = self.vida - quantidade
        self.vida = nova_vida
        print(f'{self.nome} agora possui {self.vida} de vida!')

    def atacar(self, alvo):
        if not isinstance(alvo, Personagem):
            print('O alvo deve ser um personagem válido!')
            return
        print(f'{self.nome} atacou {alvo.nome} e causou {self.dano} de dano!')
        alvo.receber_dano(self.dano)
        return True

class Paladino(Personagem):
    def __init__(self, nome, vida, dano, fe):
        self.fe = fe

        super().__init__(nome, vida, dano)

    def cura_sagrada(self):
        if self.fe >= 10:
            self.vida += 25
            print(f'{self.nome} é banhado por uma luz divina e recupera 25 de vida!')
            self.fe -= 10
            return True
        else: 
            print('Você não tem fé suficiente!')
            return False
        
class Assassino(Personagem):
    ...

class Arqueiro(Personagem):
    ...

class Mago(Personagem):
    def __init__(self, nome, vida, dano, mana):
        super().__init__(nome, vida, dano)
        self.mana = mana

    def lancar_bola_de_fogo(self, alvo):
        if self.mana >= 50:
            print(f'{self.nome} lançou BOLA DE FOGO em {alvo.nome}')
            self.mana -= 50
            alvo.receber_dano(20)
            return True
        else:
            print('Você não tem mana suficiente!')
            return False
        
    def meditar(self):
        self.mana += 30
        print(f'{self.nome} medita e recupera 30 de mana.')
        return True
    
class Kamikaze(Personagem):
    ...

    

