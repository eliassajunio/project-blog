# Projeto Blog - Aprendizado com Django e CBVs

Este é um mini projeto de blog desenvolvido com o objetivo de aprender **Django** e **Class-Based Views (CBVs)**. A aplicação exibe posts de blog obtidos de um arquivo JSON, o qual foi importado para o projeto através de um arquivo Python chamado `data.py`. Os dados são armazenados como uma lista de dicionários, tornando o processo de manipulação mais simples e eficiente.

## Tecnologias Utilizadas:

- **Back-End**: Django (Framework Python).
- **Fron-End**: HTML e CSS (para um layout simples e funcional).
- **API**: Consumo de dados de uma API externa para preencher os posts do blog (armazenados localmente em um arquivo JSON).

## Como Funciona?

O projeto foi estruturado para exibir posts de blog a partir de um arquivo JSON. Quando os dados são importados no `data.py`, eles são convertidos em uma lista de dicionários, o que facilita a manipulação e exibição na aplicação. Inicialmente, não foi utilizado um modelo do Django, o que simplifica o processo de visualização dos dados.

O uso de **Class-Based Views (CBVs)** permite gerenciar a exibição e a navegação do blog de maneira eficiente.

### Link da API Utilizada:

Os dados dos posts são obtidos de uma API externa e armazenados localmente em um arquivo JSON. Abaixo está o link para a API:

- [Link da API](https://jsonplaceholder.typicode.com/posts)

## Instalação:

- Clone este repositório:

   ```bash
   git clone https://github.com/eliassajunio/project-blog.git
