# -*- coding: UTF-8 -*-

import token;

class Simbolo:
    def __init__(self, token, categoria, tipo, arraydeparametros, endereco):
        self.token = token
        self.categoria = categoria
        # procedimento ou variavel ou param
        self.tipo = tipo
        # real ou inteiro
        self.arraydeparametros= arraydeparametros
        #quando é procedimento
        self.endereco= endereco
