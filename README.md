Avaliação de Filmes API
Bem-vindo à Avaliação de Filmes API! Esta API permite que os usuários avaliem filmes e obtenham informações sobre filmes populares, melhores avaliados, em exibição nos cinemas e muito mais. A API utiliza uma integração com uma API externa para buscar informações detalhadas sobre os filmes.

Tecnologias Utilizadas:
Django: Framework web de alto nível para desenvolvimento rápido de aplicações seguras e escaláveis em Python.
Django REST Framework: Biblioteca poderosa para construir APIs web em Django.
Requests: Biblioteca HTTP para Python, usada para fazer requisições HTTP para a API externa de filmes.
Token Authentication: Autenticação baseada em token para garantir a segurança das rotas da API.
Funcionalidades Principais:
Listar Filmes Populares: Endpoint para obter uma lista de filmes populares atualmente.
Listar Melhores Avaliados: Endpoint para obter uma lista dos filmes mais bem avaliados.
Listar Filmes em Exibição nos Cinemas: Endpoint para obter uma lista de filmes atualmente em exibição nos cinemas.
Buscar Filmes por Nome: Endpoint para buscar filmes por nome.
Detalhes do Filme: Endpoint para obter informações detalhadas sobre um filme específico.
Créditos do Filme: Endpoint para obter os créditos de elenco e equipe de um filme.
Provedores de Streaming do Filme: Endpoint para obter informações sobre provedores de streaming disponíveis para um filme.
Listar Gêneros de Filmes: Endpoint para obter uma lista de gêneros de filmes disponíveis.
Descobrir Filmes: Endpoint para descobrir novos filmes com base em vários critérios.
Implementação:
As funcionalidades são implementadas como views do Django REST Framework.
A API utiliza a autenticação baseada em token para proteger as rotas e garantir que apenas usuários autenticados possam acessar as funcionalidades.
Integração com uma API externa de filmes para buscar informações detalhadas sobre os filmes.
