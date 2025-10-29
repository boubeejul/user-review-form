
# Formulário de Avaliação

Este projeto consiste em um formulário para o envio de avaliações feito em Python + Flask com uso de DynamoDB e API Gateway na AWS com objetivo de praticar a criação de infraestrutura via IaC e integrá-la a uma aplicação.

## Screenshot
![Screenshot da aplicação](https://github.com/user-attachments/assets/d4c187cd-fcd5-4751-ac3c-0110010f4ec3)

## Tecnologias utilizadas

- AWS (Lambda, DynamoDB, API Gateway)
- Python
- Flask + HTML + CSS
- Terraform
- Boto3

## Arquitetura
![Screenshot da arquitetura](https://github.com/user-attachments/assets/51b5a827-2c3e-407e-b04e-d3690495eb8b)

## Estrutura do repositório

- `/api`: funções utilizadas pelas Lambdas
- `/app`: aplicação com o formulário
- `/terraform`: arquivos .tf necessários para a criação da infraestrutura na nuvem

## API

- Rotas:
    - `GET /reviews`
    - `POST /reviews`
- Body da requisição POST:
    ```json
    {
        "username": "string",
        "title": "string",
        "message": "string"
    }
    ```
- Body retornado pelo GET:
    ```json
    {
        "reviews": [
            {
                "username": "string",
                "title": "string",
                "message": "string",
                "date": "string"
            }
        ]
    }
    ```

## Rodando o projeto

### Variáveis de ambiente

Utilizadas pela aplicação:

- `FLASK_SECRET_KEY`: utilizada pelo Flask para criptografar a session
- `AWS_API_URL`: URL fornecida pela AWS ao criar uma API Gateway

Utilizadas pelo Terraform e Boto3 (se for rodar as funções localmente):

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION`

### Aplicação e infraestrutura

    # Criar ambiente virtual (em Linux)
    python3 -m venv .venv

    # Ativar ambiente (em Linux)
    source .venv/bin/activate

    # Atualizar pip
    python3 -m pip install --upgrade pip

    # Instalar dependências
    pip install -r requirements.txt

    # Subir infraestrutura pelo Terraform
    cd terraform/ && terraform apply

    # Rodar a aplicação
    cd .. && python3 app/app.py
