# -*- coding: UTF-8 -*-
""" Strategy Duck Type AND Template Method """

from abc import ABCMeta, abstractmethod

class Template_de_imposto_condicional(object):
    """Don't call us, we'll call you!"""
    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento)
        else:
            return self.minima_taxacao(orcamento)

    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def minima_taxacao(self, orcamento):
        pass

class ISS(object):
    #STRATEGY
    def calcula(self, orcamento):
        return orcamento.valor * 0.1

class ICMS(object):
    #STRATEGY
    def calcula(self, orcamento):
        return orcamento.valor * 0.06

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

        for item in orcamneto.obter_itens():
            if item.valor > 100:
                return True
        return False