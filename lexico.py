# -*- coding: UTF-8 -*-
reservadas = ['program', 'var', 'procedure', 'if', 'then', 'while', 'do', 'write', 'read', 'else', 'begin', 'end',
              'integer', 'real']
simbolosSimples = ['(', ')', '*', '+', '-', '<', '>', '=', '$', ':', ';', ',', '.']
# simbolosDuplos = ['<>','>=','<=',':=']
digitos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
import string
import os
import Sintatico as sint
from token import *
#CLASSES

#=================================================================================================================
#VARIAVEIS GLOBAIS
global valor
lista_tokens = []  #variavel que estao meus tokens
global linha_do_arquivo
#=================================================================================================================
# FUNÇÕES

def proxcaracter(chars):
    return (chars.pop(0))


def loopletra(chars, var):
    global valor
    if not chars:
        pass
    else:
        var = var.lower()
        valor = proxcaracter(chars)
        while (valor.upper() in letras or valor.isdigit()):
            var = var + valor.lower()
            if not chars:
            #                print "Não tem mais lista, mas adicionou"

                if var in reservadas:
             #       print "viu que é reservada"
                    obj = Token(var, linha_do_arquivo, "Reservada")
                    lista_tokens.append(obj)
                    print "Adicionou na lista a palavra reservada : %s" % obj.identificador
                else:
              #      print "viu que não é reservada"
                    obj = Token(var, linha_do_arquivo, "Identificador")
                    lista_tokens.append(obj)
                    print "Adicionou na lista o identificador : %s" % obj.identificador

                break  # só para sair do while
            # como faço para fechar o while
            else:
                valor = proxcaracter(chars)
               # print valor
        #print var
    if var in reservadas:
       # print "viu que é reservada"
        obj = Token(var, linha_do_arquivo, "Reservada")
        lista_tokens.append(obj)
        print "Adicionou na lista a palavra reservada : %s " %obj.identificador
        print "Adicionou na lista a palavra reservada : %s"  % obj.linha
        # vira palavra reservada, nao esta entrando aqui tbm
        print "O valor que saiu foi:"
        print valor
        return valor

    else:
        #print "viu que não é reservada"
        obj = Token(var, linha_do_arquivo, "Identificador")
        lista_tokens.append(obj)
        print "Adicionou na lista o identificador : %s" % obj.identificador
        print "O valor que saiu foi:"
        print valor
        # vira um identificador
        return valor


def loopdigito(linha, var):
    global valor
    valor = proxcaracter(chars)
    real = False
    while valor.isdigit():
        var = var + valor
        # print valor
        # print var
        if not chars:
          break
        else:
            valor = proxcaracter(chars)
            if valor == '.':
                print "encontrou dps do numero um . - loopdigito"
                real = True
                var = loopreal(linha, var)
    if valor == '.':
        print "encontrou dps do numero um . - loopdigito"
        real = True
        var = loopreal(linha, var)
    if not real:
        print "nao encontrou dps do numero um . - loopdigito"
        obj = Token(var, linha_do_arquivo, "Inteiro")
        lista_tokens.append(obj)
        print "Adicionou na lista o valor inteiro : %s " % obj.identificador
        print "a linha é: %d" %obj.linha
        # print "retorna o valor:"
        # print var
        print "O valor que saiu foi:"
        print valor
    return var

def loopreal(linha, var):
    global valor
    var = var + '.'
    valor = proxcaracter(chars)
    while valor.isdigit():
        var = var + valor
   #     print valor
    #    print var
        if not chars:
            obj = Token(var, linha_do_arquivo, "Real")
            lista_tokens.append(obj)
            print "O valor que saiu foi:"
            print var

            return var
        else:
            valor = proxcaracter(chars)
    obj = Token(var, linha_do_arquivo, "Real")
    lista_tokens.append(obj)
    print "Adicionou na lista o valor real : %s" % obj.identificador
    print "O valor que saiu foi:"
    print var

    return var


def loopcomentario(chars, fora):
    global valor
    comentariobarra = False
    comentarioconchete = False
    if fora is '*':
        comentariobarra = True
    else:
        comentarioconchete = True
    fora = proxcaracter(chars)
    cont= 1
    while True:
        while (comentariobarra and fora is not '*') or (comentarioconchete and fora is not '}'):
            if not chars:
                print "ERRO LEXICO, ESPERADO FECHAR O COMENTÁRIO JÁ INICIADO"
                exit()
            else:
                fora = proxcaracter(chars)
                print fora
        if not chars:
            pass
        else:
            fora = proxcaracter(chars)
        if fora is '/' or comentarioconchete:
            if not chars:
                pass
            else:
                fora = proxcaracter(chars)
            break
    return fora


def loopsimbolos(chars, simb):
    global valor
    var = simb
    if not chars:
        obj = Token(var, linha_do_arquivo, "Simbolo Simples")
        print obj.classe
        lista_tokens.append(obj)
    else:
        simb = proxcaracter(chars)
    if ((var == '<' or var == '>' or var == ':') and simb == '=') or (var == '<' and simb == '>'):
        var = var + simb
        simb = proxcaracter(chars)
        print var
        print "TEM SIMBOLO DUPLO"
        obj = Token(var, linha_do_arquivo, "Simbolo Duplo")
        print "Adicionou na lista o símbolo duplo : %s" % obj.identificador
        lista_tokens.append(obj)
        return simb
        # eh um simbolo duplo
    else:
        obj = Token(var, linha_do_arquivo, "Simbolo Simples")
        print "Adicionou na lista um símbolo simples : %s" % obj.identificador
        print simb
        lista_tokens.append(obj)
        # nao é um simbolo duplo
        return simb



def filetolist(teste):

    fd = open(teste, "r")
    lista = fd.readlines()
    fd.close()
    chars = []
    for line in lista:
        for c in line:
            chars.append(c)
    return chars

#=================================================================================================================
#MEU MENU COMEÇA AQUI:
chars = filetolist("teste1")  # Peguei todas as linhas do arquivo
i = 0
carac= ""
lista_tokens=[]
print lista_tokens
print "aqui printou a lista tokens"
linha_do_arquivo = 1  # para colocar no objeto
while chars:  # enqnt nao chego no fim da lista entra nesse while
    if i==0:
        carac= proxcaracter(chars)
        i=1;
    if carac in simbolosSimples:
       # print "entrou no simb "
        carac = loopsimbolos(chars, carac)
      #  print carac
    if carac.isdigit():
        #print "entrou no digito"
        var = carac
        var = loopdigito(chars, carac)
        carac = valor  # Como confiro o ultimo caracter na funcao eu preciso retomar ele para continuar a verificacao
        if not chars:
            exit()
    if carac is '/':
        # print carac
       # print "entrou no / "
        fora = proxcaracter(chars)  # tudo que tiver dps desse caracter nao será um token.
        fora = proxcaracter(chars)  # tudo que tiver dps desse caracter nao será um token.
        if fora is '*':
           carac= loopcomentario(chars, fora)
    if carac is '{':
        #print "entrou no { "
        carac = loopcomentario(chars, carac)
    if carac.upper() in letras:
        print chars
        carac = loopletra(chars, carac)
        print chars
        print carac
    if carac is '.':
        obj = Token('.', linha_do_arquivo, "Simbolo simples")
        print "Adicionou na lista o símbolo simples : %s" % obj.identificador
        lista_tokens.append(obj)
    if carac == ('\r'):
        carac= proxcaracter(chars)
    if (carac == " "):
        carac = proxcaracter(chars)
    if (carac == '\n'):
         #   print "entrou no \n "
        carac= proxcaracter(chars)
        linha_do_arquivo = linha_do_arquivo + 1
    if (carac == "#" or carac == "!" or carac == "%" or carac == "&" or carac== "@"):
        print "CARACTER INVALIDO NA LINGUAGEM %s:" %carac
        carac = proxcaracter(chars)


for token in range(len(lista_tokens)):
    print lista_tokens[token].identificador, lista_tokens[token].classe
print "                                         "

sint.menuPrincipalSintatico(lista_tokens)

