# Minha API

Este projeto foi desenvolvido a partr faz do material didático da Disciplina **Desenvolvimento Full Stack Básico**

O objetivo deste projeto é implementar uma API que execute a interface entre um Servidor de Dados Back-end, um Banco de dados (Camada 2) e um Servidor de aplicação Front-end(Camada 1). Esta API deve executar os métodos GET, POST, PUT e DELETE de itens no Banco de Dados.

O Banco de Dados em SQLite corresponde a um cadastro de diferentes modelos de carros que representam o estoque disponível em loja de uma concessionária de carros novos e seminovos. Através dessa aplicação é possível listar, buscar, adicionar, deletar e fazer alteraçoes nos carros do Banco de Dados.

As características dos carros no Banco de Dados correspondem ao seu modelo, ano, marca, quantidade e valor. Outras características podem ser acrescentadas, mas como exemplo prático optou-se por definir um número limitado de colunas. A aplicação tem como objetivo demonstrar como seria um sistema de gestão dos automóveis em uma plataforma de visualização de veículos à venda em uma determinada concessionária.


---
## Como executar 


Para executar esta aplicação é necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
