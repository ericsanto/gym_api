# gym_api

## Descrição

O `gym_api` é uma API RESTful desenvolvida em Django com Django Rest Framework (DRF) para gerenciar informações relacionadas a um sistema de academia. A API permite realizar operações como criar, ler, atualizar e excluir informações sobre exercícios, músculos, configurações de autenticação e permissões.

## Funcionalidades

- **Gerenciamento de Exercícios**: Crie, leia, atualize e exclua exercícios.
- **Gerenciamento de Músculos**: Acompanhe quais músculos são trabalhados em cada exercício.
- **Autenticação e Permissões**: Controle de acesso para diferentes usuários.
- **Documentação da API**: Gere documentação para facilitar o uso da API.

## Instalação

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seu_usuario/gym_api.git
   cd gym_api

## Criando e Ativando um Ambiente Virtual

Para gerenciar as dependências do projeto de forma isolada, é recomendado usar um ambiente virtual. Siga os passos abaixo para criar e ativar um ambiente virtual:

1. **Crie um ambiente virtual**:

   ```bash
   python -m venv venv

2. **Ative o ambiente virtual:**:

Para Linux/Mac:
    ```bash
   source venv/bin/activate

Para Windows:
     ```bash
   source venv/bin/activate


**Estrutura da API**

A API possui os seguintes endpoints:

    Exercícios
        GET /api/exercises/: Lista todos os exercícios.
        POST /api/exercises/: Cria um novo exercício.
        GET /api/exercises/{id}/: Obtém detalhes de um exercício específico.
        PUT /api/exercises/{id}/: Atualiza um exercício específico.
        DELETE /api/exercises/{id}/: Remove um exercício específico.

    Músculos
        GET /api/muscles/: Lista todos os músculos.
        POST /api/muscles/: Cria um novo músculo.
        GET /api/muscles/{id}/: Obtém detalhes de um músculo específico.
        PUT /api/muscles/{id}/: Atualiza um músculo específico.
        DELETE /api/muscles/{id}/: Remove um músculo específico.

    Autenticação e Permissões
        Use o sistema de autenticação do Django Rest Framework para proteger os endpoints.


**Gerando Documentação**

Para gerar a documentação da API, você pode usar o django-pydoc ou Sphinx. Aqui estão os passos para cada método:
Usando django-pydoc

    1- Coloque o arquivo django_pydoc.py na raiz do seu projeto (ao lado do manage.py).

    2- Execute o seguinte comando: python django_pydoc.py -p 1234

    3- Acesse a documentação no navegador em http://localhost:1234.