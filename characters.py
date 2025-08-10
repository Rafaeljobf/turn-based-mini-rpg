class Personagem:
    def __init__(self, nome, vida, dano):
        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.nivel = 1
    
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
        print(f'{self.nome} agora possui {self.vida} de vida')

    def atacar(self, alvo):
        if not isinstance(alvo, Personagem):
            print('O alvo deve ser um personagem válido!')
            return
        print(f'{self.nome} atacou {alvo.nome} e causou {self.dano} de dano!')
        alvo.receber_dano(self.dano)

     


    

