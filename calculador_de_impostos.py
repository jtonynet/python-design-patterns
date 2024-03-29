# -*- coding: UTF-8 -*-
""" Strategy Duck Type AND Template Method """

from impostos import ISS, ICMS, ICPP, IKCV

class Calculador_de_impostos(object):

        def realiza_calculo(self, orcamento, imposto):

            imposto_calculado = imposto.calcula(orcamento)

            print imposto_calculado


if __name__ == '__main__':

    from orcamento import Orcamento, Item

    calculador = Calculador_de_impostos()

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM - 1', 50))
    orcamento.adiciona_item(Item('ITEM - 2', 200))
    orcamento.adiciona_item(Item('ITEM - 3', 250))

    print 'ISS and ICMS'
    #STRATEGY
    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())

    print 'ISS + ICMS  with Decorator'
    #STRATEGY AND DECORATOR
    calculador.realiza_calculo(orcamento, ISS(ICMS()))

    print 'ICPP and IKCV'
    #STRATEGY AND TEMPLATE METHOD
    calculador.realiza_calculo(orcamento, ICPP())
    calculador.realiza_calculo(orcamento, IKCV())

    print 'ICPP + IKCV with Decorator'
    #STRATEGY AND TEMPLATE METHOD AND DECORATOR
    calculador.realiza_calculo(orcamento, ICPP(IKCV()))