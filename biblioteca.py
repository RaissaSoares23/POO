class Pessoa():
    def __init__(self,peso, nome,idade):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.comendo=False
        self.falando=False
        self.dormindo=False
    def comer(self,comida):
        if self.comendo==True:
            print (f"{self.nome}  já está comendo")
        elif self.falando==True:
            print(f"{self.nome} não pode comer pq está falando.")
        else:
            print (f"{self.nome} foi comer {comida}")
            self.comendo=True
    def PararComer(self):
        if self.comendo==True:
            print("Parar de Comer")
            self.comendo=False
    def falar(self):
        print (f"{self.nome} foi conversar")
    def dormir(self):
        print (f"{self.nome} foi dormir")
