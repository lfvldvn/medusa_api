# medusa_api
API for customers, products and orders.

# Medusa API
Uma API RESTful desenvolvida em Python usando Flask para gerenciar a integração de clientes, pedidos, produtos e inscrições em newsletter. Este projeto é um exemplo de como construir uma aplicação web completa com validação de entrada, autenticação, documentação e testes automatizados.

## Funcionalidades
- **Gerenciamento de Clientes**: Adicione, atualize, visualize e exclua clientes.
- **Gerenciamento de Pedidos**: Adicione, atualize, visualize e exclua pedidos.
- **Gerenciamento de Produtos**: Adicione e visualize produtos.
- **Inscrição na Newsletter**: Permita que os usuários se inscrevam em uma newsletter.
- **Validação de Entrada**: Validação de dados de entrada para garantir que estejam no formato correto (e-mail, telefone, etc.).
- **Tratamento de Erros**: Respostas de erro mais informativas e personalizadas.
- **Autenticação**: Proteção de endpoints com autenticação básica.
- **Documentação da API**: Documentação da API gerada automaticamente usando Swagger.
- **Testes Automatizados**: Testes para garantir a funcionalidade correta das rotas e funcionalidades.

## Tecnologias Utilizadas
- Python
- Flask
- SQLite
- Flask-Swagger para documentação
- Flask-HTTPAuth para autenticação
- email-validator para validação de e-mails

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/medusa.git
   cd medusa

2. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux ou macOS
    venv\Scripts\activate  # Para Windows

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt

## Uso
1. Execute a aplicação
    ```bash
    python medusa.py

2. A API estará disponível em http://127.0.0.1:5000.

## Endpoints
1. Clientes
    - Adicionar Cliente: POST /add_customer
    - Visualizar Clientes: GET /customers
    - Atualizar Cliente: PUT /update_customer/<int:id>
    - Deletar Cliente: DELETE /delete_customer/<int:id>

2. Pedidos
    - Adicionar Pedido: POST /add_order
    - Visualizar Pedidos: GET /orders
    - Atualizar Pedido: PUT /update_order/<int:id>
    - Deletar Pedido: DELETE /delete_order/<int:id>

3. Produtos
    - Adicionar Produto: POST /add_product
    - Visualizar Produtos: GET /products

4. Newsletter
    - Inscrever na Newsletter: POST /subscribe_newsletter
    - Visualizar Inscrições: GET /newsletter_subscribers

## Autenticação
Endpoints de atualização e exclusão requerem autenticação básica. Você pode usar ferramentas como Postman para testar a autenticação.

## Documentação
A documentação da API está disponível em http://127.0.0.1:5000/apidocs.

## Testes
Para executar os testes automatizados, utilize o seguinte comando:
    ```bash
    python -m unittest discover -s tests

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para detalhes.


### Personalizações:
- **Substitua `seu_usuario` pelo seu nome de usuário do GitHub**.
- **Adicione informações sobre como realizar os testes, caso tenha implementado algum**.
- **Inclua qualquer outra informação específica ou instruções que você ache relevante**. 

Sinta-se à vontade para ajustar qualquer seção para refletir melhor o seu projeto!
