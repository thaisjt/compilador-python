
# -*- coding: UTF-8 -*-

from token import *
from Simbolo import *
import sys
tabeladesimbolos = {};
escopo = "global"
categoria = ""
dic = {}
lista_simb = []
def teste():
    print "Teste Sintatico"

def programa(chars):
    conf = chars.pop(0)
    print "entrou no programa"
    print conf.identificador
    if conf.identificador=="program":
        conf = chars.pop(0)
        print "tirou o PROGRAM"
        if conf.classe == "Identificador":
            print "tirou o IDENTIFICADOR"
            corpo(chars)
            print "aqui"
            if chars[0].identificador == '.':
                conf = chars.pop(0)
                print "TIROU O %s" % conf.identificador
                valor = dic.get("procedure_divisao_h")
                print valor.token.linha
                print dic
                print "FIM DO PROGRAMA"
            else:
                print "DEVERIA EXISTIR UM PONTO FINAL PARA FINALIZAR O PROGRAMA"
        else:
            print conf.identificador
            print conf.classe
            print "Deveria existir um identificador na linha "
            print "%d" %conf.linha
            exit()
    else:
        print "Deveria existir um elemento programa para comecar o programa na linha"
        print "%d" % conf.linha
        exit()

def corpo(chars):
    # VEM DE PROGRAMA

    print "entrou no corpo"
    dc(chars)
    print "_____________corpo______________"
    conf = chars.pop(0)
    if conf.identificador== "begin":
        print "TIROU O %s" % conf.identificador
        comandos(chars)
        conf = chars.pop(0)
        if conf.identificador == "end":
            print "TIROU O %s" % conf.identificador
            print "LISTAAAAAAA COMANDO"
            pass
        else:
            print "Deveria existir um end na linha "
            print "%d" %conf.linha
            exit()

    else:
        print "Deveria existir um begin na linha "
        print "%d" % conf.linha
        exit()


def dc(chars):
    #VEM DO CORPO
    #ESSE UTILIZO O FIRST

    print "entrou no dc"
    if chars:
        print chars[0].identificador
        if chars[0].identificador== 'var':
            dc_v(chars)
            mais_dc(chars)
        elif chars[0].identificador == 'procedure':
            print "ENCONTROU O PROCEDURE"
            dc_p(chars)
            mais_dc(chars)

def dc_v(chars):
    #VEM DO DC
    global categoria
    print "entrou no dc_v"
    if chars:
        conf = chars.pop(0)
        if conf.identificador=="var":
            print "tirou o VAR"
            categoria = "variavel"
            variaveis(chars)
            print "-----------dc_v-------------- "
            conf = chars.pop(0)
            if conf.identificador == ":":
                print "TIROU O %s" % conf.identificador
                tipo_var(chars)
            else:
                print "erro no :"
                print conf.identificador
                print "Deveria existir um identificador : na linha "
                print "%d" %conf.linha
                exit()
        else:
            print "Deveria existir um identificador var na linha "
            print "%d" % conf.linha
            exit()
    else:
        print "ERRO DEVERIA EXISTIR UMA VARIAVEL"
        exit()

def mais_dc(chars):

    print "entrou no mais_dc"
    #VEM DO DC
    if chars:
        if chars[0].identificador == ";":
            print "TIROU O %s" % chars[0].identificador
            chars.pop(0)
            dc(chars)
        else:
            pass


def tipo_var(chars):
    # VEM DO DC_V
    print "entrou no tipo_var"
    if chars:
        conf = chars.pop(0)
        print conf.identificador
        if conf.identificador == "real":
            tam = len(lista_simb)
            for a in range(tam):
                simb = lista_simb.pop()
                simb.tipo = "real";
                adicionanatabela(simb,escopo);

            print "TIROU O %s" % conf.identificador
        else:
            if conf.identificador == 'integer' or conf.identificador == 'inteiro':
                tam = len(lista_simb)
                print "TIROU O INTEIRO"
                for a in range(tam):
                    simb = lista_simb.pop()
                    simb.tipo = "integer";
                    adicionanatabela(simb,escopo);

            else:
                print "Deveria existir um numero real ou inteiro na linha "
                print "%d:" % conf.linha
                exit()
    else:
        print "ERRO ERA ESPERADO UM REAL OU INTEGER, MAS NAO HÁ CARACTER"
        exit()


def variaveis(chars):
    global categoria
    print "entrou em variaveis"
    # VEM DO DC
    if chars:
        conf = chars.pop(0)
        print conf.classe
        print conf.identificador
        if conf.classe == "Identificador":
            simb = Simbolo(conf, categoria, "", None, None);
            lista_simb.append(simb);
            print "____________________________________________________"
            print simb.token.identificador;
            print "TIROU O %s" %conf.identificador
            if chars:
                mais_var(chars)
        else:
            print "Deveria existir um identificador na linha - variaveis "
            print "na linha: %d" % conf.linha
            print "é o identificador: %s" % conf.identificador
            print escopo
            exit()
    else:
        print "ERRO POIS NÃO HÁ MAIS CARACTERES"
        exit()

def mais_var(chars):

    print "entrou em mais_var"
    # VEM DAS VARIAVEIS
    if chars:
        conf = chars[0].identificador
        if conf == ",":
            conf = chars.pop(0)
            print "TIROU O %s" % conf.identificador
            variaveis(chars)

def dc_p(chars):
    # VEM DO DC
    global escopo
    if chars:
        conf = chars.pop(0)
        print conf.identificador
        if conf.identificador == "procedure":
            conf = chars.pop(0)
            print conf.classe
            print conf.identificador
            if conf.classe == "Identificador":
                escopo = "procedure" + "_" + conf.identificador
                print escopo
                print "entrou"
                parametros(chars)
                corpo_p(chars)
            else:
                print "Deveria existir um identificador na linha "
                print "%d:" % conf.linha
                exit()
        else:
            print "Deveria existir um PROCEDURE na linha "
            print "%d:" % conf.linha
            exit()
    else:
        print "ERRO POIS NÃO HÁ MAIS CARACTERES"
        exit()


def parametros(chars):
    # VEM DO DC_P
    if chars:
        print "entrou em paramentros"
        abre = chars.pop(0)
        print abre.identificador
        if abre.identificador == '(':
            print "vai entrar em lista_par"
            lista_par(chars)
            fecha = chars.pop(0)
            print "volta para parametros"
            print abre.identificador
            if fecha.identificador == ')':
                print "fechou"
            else:
                print "Não fechou no paramentro"
                exit()
        else:
            print "Não abriu no paramentro"
            exit()

def lista_par(chars):
    # VEM DO PARAMETRO
    global categoria
    if chars:
        print "entrou em paramentros"
        categoria = "parametro" + "_" + escopo
        variaveis(chars)
        if chars:
            conf = chars.pop(0)
            if conf.identificador == ":":
                tipo_var(chars)
                mais_par(chars)
            else:
                print "Deveria existir um : na linha "
                print "%d:" % conf.linha
                exit()
        else:
            print "ERRO POIS NÃO HÁ MAIS CARACTERES"
            exit()
    else:
        print "ERRO POIS NÃO HÁ MAIS CARACTERES"
        exit()


def mais_par(chars):
    #VEM DA LISTA_PAR
    if chars:
        print "ENTROU EM MAIS_PAR"
        print chars[0].identificador
        if chars[0].identificador == ";":
            chars.pop(0)
            lista_par(chars)


def corpo_p(chars):
    #VEM DE DC_P
    if chars:
        dc_loc(chars)
        conf = chars.pop(0)
        print conf.identificador
        if conf.identificador== "begin":
            comandos(chars)
            conf = chars.pop(0)
            if conf.identificador == "end":
                pass
            else:
                print "Deveria existir um end na linha "
                print "%d" %conf.linha
                exit()
        else:
            print "Deveria existir um begin na linha "
            print "%d" % conf.linha
            exit()
    else:
        print "ERRO POIS NÃO HÁ MAIS CARACTERES"
        exit()



def dc_loc(chars):
    #VEM DE CORPO_P
    if chars:
        print chars[0].identificador
        if chars[0].identificador == "var":
            dc_v(chars)
            if chars:
                mais_dcloc(chars)
            else:
                exit()



def lista_arg(chars):
    # VEM DE restoIdent
    if chars:
      conf= chars.pop(0)
      print conf.identificador
      if conf.identificador == '(':
        argumentos(chars)
        conf = chars.pop(0)
        print "esta no lista_arg"
        if conf.identificador == ')':
            pass
def argumentos(chars):
    #Vem de LISTA_ARG
    if chars:
        print "entrou em argumentos %s" %chars[0].identificador
        conf = chars.pop(0)
        print conf.identificador
        if conf.classe== "Identificador":
                mais_ident(chars)
        else:
            print "O ELEMENTO EM ARGUMENTOS ERRADO É: "
            print conf.identificador
            print "Deveria existir um identificador na linha - argumentos"
            print "%d" % conf.linha
            exit()
    else:
        print "ERRO POIS NÃO HÁ MAIS CARACTERES"
        exit()

def mais_ident(chars):
    # Vem de ARGUMENTOS
    if chars:
        print "Entrou em Mais_Ident"
        print chars[0].identificador
        if chars[0].identificador== ";":
            chars.pop(0)
            print "1"
            argumentos(chars)
        else:
            print "entrou no else"
            pass

def pfalsa(chars):
    # Vem de COMANDO
    if chars:
        conf = chars.pop(0)
        if conf.identificador == "else":
            comandos(chars)
        else:
            print "Deveria existir um ; na linha "
            print "%d:" % conf.linha


def comandos(chars):
    print "entrou em comandos"
    #VEM DO CORPO, CORPO_P, PFALSA, COMANDO
    if chars:
        comando(chars)
        if chars:
            print "entrou pelo comando"
            mais_comandos(chars)
        else:
            print "ERRO POIS NÃO HÁ MAIS CARACTERES - comandos"
            exit()
    else:
        print "ERRO POIS NÃO HÁ MAIS CARACTERES - comandos"
        exit()

def comando(chars):
    # VEM DO COMANDOS
    print "entrou em comando"
    global categoria
    if chars:
        categoria = "variavel"
        print 'o identificador é '
        print chars[0].identificador
        if chars[0].identificador == 'read':
            print "TIROU O %s" %chars[0].identificador
            chars.pop(0) # já sei que é um read
            conf = chars.pop(0)
            if conf.identificador== '(':
                print "TIROU O %s" % conf.identificador
                variaveis(chars)
                conf= chars.pop(0)
                if conf.identificador == ')':
                 print "TIROU O %s" % conf.identificador
                else:
                    print "Não há um parenteses para fechar o read"
        else:
            print "entrou no else"
            print chars[0].classe, chars[0].identificador
            if chars[0].classe == "Identificador":
                    conf = chars.pop(0) # já sei que é um ident
                    restoIdent(chars, conf)
            elif chars[0].identificador == 'if':
                chars.pop(0)
                verificatipo = None
                condicao(chars, verificatipo)
                conf = chars.pop(0)
                if conf.identificador == "then":
                    print "TIROU O THEN"
                    comandos(chars)
                    pfalsa(chars)
                    conf = chars.pop(0)
                    if conf.identificador == "$":
                        pass
                    else:
                        print "Deveria existir um $ na linha "
                        print "%d" % conf.linha
                        exit()
                else:
                    print "Deveria existir um then na linha "
                    print "%d" % conf.linha
                    exit()
            elif chars[0].identificador == 'write':
                print " entrou no write "
                chars.pop(0)
                conf = chars.pop(0)
                if conf.identificador == '(':
                    print "TIROU O ("
                    variaveis(chars)
                    conf = chars.pop(0)
                    if conf.identificador== ')':
                        print "TIROU O )"
                    else:
                        print "Deveria existir um ) na linha "
                        print "%d" % conf.linha
                        exit()
                else:
                    print "Deveria existir um ( na linha "
                    print "%d" % conf.linha
                    exit()
            elif chars[0].identificador == 'while':
                if chars:
                    print "entrou no while"
                    chars.pop(0)
                    verificatipo = None
                    condicao(chars, verificatipo)
                    conf = chars.pop(0)
                    print conf
                    print conf.identificador
                    if conf.identificador == "do":
                        comandos(chars)
                        conf = chars.pop(0)
                        if conf.identificador == "$":
                            pass
                        else:
                            print "Deveria existir um $ na linha "
                            print "%d" % conf.linha
                            exit()
                    else:
                        print "Deveria existir um do na linha "
                        print "%d" % conf.linha
                        exit()
def restoIdent(chars, conf):
    #VEM DE COMANDO
    if chars:
        print "entrou em restoident"
        print chars[0].identificador
        if chars[0].identificador == ':=':
            verificatipo = procuranatabela(conf.identificador, escopo)
            print 'verificando tipo, o tipo da variavel que veio do procura na tabela é:'
            print verificatipo.tipo
            conf2= chars.pop(0)
            print "TIROU O %s" % conf2.identificador
            expressao(chars,verificatipo)
        elif chars[0].identificador == '(':
            lista_arg(chars)
        else:
            print "erro em restoIdent"
def condicao(chars, verificatipo):
    if chars:
        print "entrou em condicao"
        expressao(chars, verificatipo)
        relacao(chars)
        expressao(chars, verificatipo)
    else:
        print "ERRO POIS NÃO HÁ MAIS CARACTERES"
        exit()


def relacao(chars):
    #VEM DE CONDICAO
    print dic
    conf=  chars[0].identificador
    print conf
    if conf == ">":
        print "Tirou >"
        chars.pop(0)
        pass
    else:
        print "não há uma relação na linha "
        exit()

def expressao(chars, verificatipo):
    #VEM DE RESTOIDENT, CONDICAO, FATOR
    if chars:
        print "ENTROU EM EXPRESSAO"
        termo(chars, verificatipo)
        if chars:
            print "ENTROU EM EXPRESSAO APOS ACABAR O TERMO"
            outros_termos(chars, verificatipo)
        else:
            print "ERRO POIS NÃO HÁ MAIS CARACTERES"
            exit()
    else:
        print "ERRO POIS NÃO HÁ MAIS CARACTERES"
        exit()

def op_un(chars):
    # VEM DE TERMO
    if chars:
        print "ENTROU EM OP_UN"
        if chars[0].identificador == "+" or chars[0].identificador == "-":
            print "TIROU O %s" % chars[0].identificador
            chars.pop(0)
            pass

def op_ad(chars):
    # VEM DE OUTROSTERMOS
    if chars:
        print "ENTROU EM OP_AD"
        conf = chars.pop(0)
        print conf.identificador
        if conf.identificador == "+" or conf.identificador == "-":
            print "TIROU O %s" %conf.identificador
            pass
        else:
            print "não há um operador na linha "
            print "%d" % conf.linha
            exit()
    else:
        print "ERRO POIS NÃO HÁ MAIS CARACTERES"
        exit()

def op_mul(chars):
    # VEM DE MAIS FATORES
    if chars:
        if chars[0].identificador == "*" or chars[0].identificador == "/":
            chars(0).pop

def termo(chars, verificatipo):
    #VEM DE COMANDO
    if chars:
        print "ENTROU EM TERMO"
        op_un(chars)
        fator(chars, verificatipo)
        mais_fatores(chars)
    else:
        print "ERRO POIS NÃO HÁ MAIS CARACTERES"
        exit()

def outros_termos(chars, verificatipo):
    #VEM DE EXPRESSAO
    if chars:
        print "ENTROU EM OUTROS_TERMOS"
        if chars[0].identificador == "+" or chars[0].identificador == "-":
            op_ad(chars)
            termo(chars, verificatipo)

            outros_termos(chars, verificatipo)

def mais_fatores(chars):
    if chars:
        print "ENTROU EM MAIS_FATORES"
        if chars[0].identificador == "/" or chars[0].identificador == "*":
            op_mul(chars)
            fator(chars)
            mais_fatores(chars)
    else:
        print "ERRO POIS NÃO HÁ MAIS CARACTERES"
        exit()

def fator(chars, antigo):
    if chars:
        print "ENTROU EM FATOR"
        conf = chars.pop(0)
        print conf.classe
        print conf.identificador
        if conf.classe == 'Identificador':
            print "TIROU O %s" %conf.identificador
            print 'tirou da lista'
            print chars[0].identificador
            if antigo != None:
                conf = procuranatabela(conf.identificador, escopo)
                print 'teste 1'
                print conf.tipo
                print antigo
                if conf.tipo == antigo.tipo:
                    print "SAO DOS TIPOS IGUAIS"
                    pass
                else:
                    print "tipos de variaveis incompativeis, no escopo %s entre as variáveis:" %escopo
                    print conf.token.identificador
                    print antigo.token.identificador
                    print conf.tipo
                    print antigo.tipo
                    sys.exit()

            else:
                antigo = conf
        elif conf.classe == 'Inteiro' or conf.classe == 'Real':
            print "TIROU O %s" % conf.identificador
            print 'tirou da lista'
            print chars[0].identificador
            print 'teste 1'
            print conf.classe
            print antigo
            if conf.classe == antigo.tipo:
                pass
        elif conf.identificador == '(':
            print "Tirou o ("
            expressao(chars, antigo)
            conf= chars.pop(0)
            if conf.identificador == ')':
                print "Tirou o )"
            else:
                print conf.classe
                print conf.identificador
                print "erro é esperado fecha parenteses - fator"
                print dic
                exit()
        else:
            print "Erro sintatico - fator"

def mais_dcloc(chars):
    print "ENTROU EM +DCLOC"
    if chars:
        if chars[0].identificador== ";":
            chars.pop(0)
            dc_loc(chars)
        else:
            pass


def mais_comandos(chars):
    #VEM DE COMANDOS
    print "ENTROU EM +COMANDOS"
    if chars:
        print  chars[0].identificador
        if chars[0].identificador== ";":
            conf = chars.pop(0)
            print "TIROU O %s" % conf.identificador
            comandos(chars)

def adicionanatabela(simbolo,escopo):
    nome = escopo + "_" + simbolo.token.identificador;
    print dic
    print simbolo.token.identificador;
    print nome
    verifica = dic.get(nome)
    print verifica
    if verifica == None :
        dic.update({nome: simbolo})
        print simbolo.tipo
        valor = dic.get(nome)
        print 'confereeeeeee'
        print valor
    else:
        print "Impossivel criar outra variavel com o mesmo nome no %s com a variavel;" %escopo
        print "o elemento de erro é a variavel: %s. Por favor, declare variaveis apenas inexistentes." %simbolo.token.identificador
        print "na linha %s" %simbolo.token.linha
        exit()
    print "DICIONARIO______________________________________"
    print dic

def procuranatabela(nome, escopo):
    print 'PROCURA NA TABELAAAAAA'
    nome_global = 'global' + "_" + nome;
    nome_procedure = escopo + "_" + nome;
    print nome
    print nome_global
    print nome_procedure
    print dic
    valor = dic.get(nome_procedure)
    print 'o valor e %s, no procedimento' %valor
    print "ELE É VAZIO?"
    if valor == None:
        print 'é, então irá procurar no escopo global'
        print nome_procedure
        valor = dic.get(nome_global)
        print 'o valor e %s, no escopo global' % valor
        print dic
        return valor
    if valor != None:
        return valor
def menuPrincipalSintatico(lista):
    print "COMEÇA A ANALISE SINTATICA"
    programa(lista)

