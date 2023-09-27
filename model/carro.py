from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base, Comentario


class Carro(Base):
    __tablename__ = 'carro'

    id = Column("pk_carro", Integer, primary_key=True)
    modelo = Column(String(140), unique=True)
    ano = Column(Integer)
    marca = Column(String(10))
    quantidade = Column(Integer)
    valor = Column(Float)
    data_insercao = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o carro e o comentário.
    # Essa relação é implicita, não está salva na tabela 'carro',
    # mas aqui estou deixando para SQLAlchemy a responsabilidade
    # de reconstruir esse relacionamento.
    comentarios = relationship("Comentario")

    def __init__(self, modelo:str, ano:int, marca:str, quantidade:int, valor:float,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Carro

        Arguments:
            modelo: modelo do carro.
            ano: ano de fabricação do modelo
            marca: montadora do carro
            quantidade: quantidade que se espera comprar daquele carro
            valor: valor esperado para o carro
            data_insercao: data de quando o carro foi inserido à base
        """
        self.modelo = modelo
        self.ano = ano
        self.marca = marca
        self.quantidade = quantidade
        self.valor = valor

        # se não for informada, será a data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

    def adiciona_comentario(self, comentario:Comentario):
        """ Adiciona um novo comentário ao carro
        """
        self.comentarios.append(comentario)

