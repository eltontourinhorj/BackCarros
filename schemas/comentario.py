from pydantic import BaseModel


class ComentarioSchema(BaseModel):
    """ Define como um novo comentário a ser inserido deve ser representado
    """
    carro_modelo: str = "Focus"
    texto: str = "Só comprar se o carro for realmente bom!"
