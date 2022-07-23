from mailbox import NotEmptyError
from tokenize import PseudoExtras


class Animal:
    def __init__(self, nome, peso) -> None:
        self.nome = nome
        self.peso= peso


class Mamifero(Animal):
    def __init__(self, nome, peso, peso_gestacao) -> None:
        super().__init__(nome, peso)
        self.peso_gestacao = peso_gestacao

    def __str__(self):
        return 

from IPython import embed; embed()