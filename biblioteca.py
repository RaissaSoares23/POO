class Pessoa():
    def __init__(self,peso, nome,idade):
        self.nome=nome
        self.idade=idade
        self.peso=peso
    def comer(self,comida):
        print(f"{self.nome} foi comer{comida}")
    def falar(self):
        print (f"{self.nome} foi conversar")
    def dormir(self):
        print (f"{self.nome} foi dormir")