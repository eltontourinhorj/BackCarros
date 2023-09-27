from pydantic import BaseModel
from typing import Optional, List
from model.carro import Carro

from schemas import ComentarioSchema


class CarroSchema(BaseModel):
    """Define como um novo carro a ser inserido deve ser representado"""

    modelo: str = "Focus"
    ano: int = 2000
    marca: str = "Ford"
    quantidade: Optional[int] = 1
    valor: float = 32000.00


class CarroUpdateSchema(BaseModel):
    """Define como um novo carro a ser inserido deve ser representado"""

    ano: int = 2000
    marca: str = "Ford"
    quantidade: Optional[int] = 1
    valor: float = 32000.00


class CarroBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca. Que será
    feita apenas com base no nome do carro.
    """

    modelo: str = "Focus"


class ListagemCarrosSchema(BaseModel):
    """Define como uma listagem de carros será retornada."""

    carros: List[CarroSchema]


def apresenta_carros(carros: List[Carro]):
    """Retorna uma representação do carro seguindo o schema definido em
    CarroViewSchema.
    """
    result = []
    for carro in carros:
        result.append(
            {
                "modelo": carro.modelo,
                "ano": carro.ano,
                "marca": carro.marca,
                "quantidade": carro.quantidade,
                "valor": carro.valor,
            }
        )

    return {"carros": result}


class CarroViewSchema(BaseModel):
    """Define como um carro será retornado: carro + comentários."""

    id: int = 3
    modelo: str = "Fusca"
    ano: int = 2000
    marca: str = "Volks"
    quantidade: Optional[int] = 1
    valor: float = 15000
    total_cometarios: int = 1
    comentarios: List[ComentarioSchema]


class CarroDelSchema(BaseModel):
    """Define como deve ser a estrutura do dado retornado após uma requisição
    de remoção.
    """

    mesage: str
    modelo: str


def apresenta_carro(carro: Carro):
    """Retorna uma representação do carro seguindo o schema definido em
    CarroViewSchema.
    """
    return {
        "id": carro.id,
        "modelo": carro.modelo,
        "ano": carro.ano,
        "marca": carro.marca,
        "quantidade": carro.quantidade,
        "valor": carro.valor,
        "total_comentarios": len(carro.comentarios),
        "comentarios": [{"texto": c.texto} for c in carro.comentarios],
    }
