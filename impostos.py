# -*- coding: UTF-8 -*-
""" Strategy Duck Type AND Template Method AND Decorator """

from abc import ABCMeta, abstractmethod

class Imposto(object):
    #DECORATOR
    def __init__(self, outro_imposto = None):
        self.__outro_imposto = outro_imposto

    def calculo_do_outro_imposto(self, orcamento):
        if self.__outro_imposto is None:
            retorno = 0
        else:
            retorno = self.__outro_imposto.calcula(orcamento)

        return retorno

    @abstractmethod
    def calcula(self, orcamento):
        pass

class Template_de_imposto_condicional(Imposto):
    """Don't call us, we'll call you!"""
    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            taxacao = self.maxima_taxacao(orcamento)
        else:
            taxacao = self.minima_taxacao(orcamento)

        return taxacao + self.calculo_do_outro_imposto(orcamento)

    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def minima_taxacao(self, orcamento):
        pass

def IPVX(metodo_ou_funcao):
    def wrapper(self, orcamento):
        return metodo_ou_funcao(self, orcamento) + 50
    return wrapper
    # chama o cálculo do imposto ISS, pega o resultado e soma com R$ 50,00

class ISS(Imposto):
    #STRATEGY AND DECORATOR
    @IPVX
    def calcula(self, orcamento):
        return orcamento.valor * 0.1 + self.calculo_do_outro_imposto(orcamento)

class ICMS(Imposto):
    #STRATEGY
    def calcula(self, orcamento):
        return orcamento.valor * 0.06 + self.calculo_do_outro_imposto(orcamento)

class ICPP(Template_de_imposto_condicional):
    #STRATEGY AND TEMPLATE METHOD
    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.07

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.05

class IKCV(Template_de_imposto_condicional):
    #STRATEGY AND TEMPLATE METHOD
    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500 and __tem_item_maior_que_cem_reais(orcamento)

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.1

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.06


    def __tem_item_maior_que_cem_reais(self, orcamneto):

        retorno = False
        for item in orcamneto.obter_itens():
            if item.valor > 100:
                retorno = True
        return retorno