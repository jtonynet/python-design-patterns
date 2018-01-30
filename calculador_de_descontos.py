# -*- coding: UTF-8 -*-
""" Chain of Responsability """

from descontos import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhentos_reais, Sem_desconto

class Calculador_de_descontos(object):

    def calcula(self, orcamento):
        
        desconto = Desconto_por_cinco_itens(
            Desconto_por_mais_de_quinhentos_reais(
                Sem_desconto()
            )
        ).calcula(orcamento)


        return desconto

if __name__ == '__main__':

    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM - 1', 100))
    orcamento.adiciona_item(Item('ITEM - 2', 50))
    orcamento.adiciona_item(Item('ITEM - 3', 100))
    #orcamento.adiciona_item(Item('ITEM - 4', 50))
    #orcamento.adiciona_item(Item('ITEM - 5', 50))
    #orcamento.adiciona_item(Item('ITEM - 6', 50))

    print orcamento.valor

    calculador = Calculador_de_descontos()
    desconto = calculador.calcula(orcamento)

    print 'Desconto calculado %s' % (desconto)