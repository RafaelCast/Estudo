**Teste Adaptativo - Nível Iniciante (50 Questoes)**

**Instruções:**

* Este teste tem 50 questões adaptadas ao seu nível atual com base no desempenho anterior.
* Você tem até 4 horas para completar o teste.
* Inclui exercícios teóricos e práticos inspirados em problemas reais, como no Case Técnico enviado.
* Inclui questões sobre o gerenciador de dependências **Poetry**.

---

### PARTE 1 - QUESTÕES TEÓRICAS (25 pontos)

1. O que é uma função em Python? Dê um exemplo simples.

    Função é um bloco de codigo que executa uma tarefa especifica

    ```python
    def soma(a: int, b: int) -> int:
        return a+b
    ```
2. O que são listas e como se declara uma?

    Lista é um objeto que armazena um coleção ordenada de elementos. Esse objeto é mutavel e pode ser de qualquer tipo

    ```python
    lista = []
    ```
3. Explique a diferença entre `if`, `elif` e `else`.

    O `if` é a primeira condição a ser testada, já o `elif` é uma condição adicional que só é testada se o `if` ou qualquer outro `elif` anterior falhe. Ja o `else` se nao atender nenhum requisito vai parar nele

4. O que faz a função `range()`?

    Ela cria um interador que vai de 0 até n-1
5. Qual a diferença entre `==` e `is`?

    `==` verifica o valor
    `is` verifica a identidade do objeto
6. O que significa `None` em Python?

    Significa ausencia de valor ou nenhum resultado
7. O que é o `print()` e para que serve?

    Serve para imprimir uma mensagem no terminal, serve para mostra algo ou passar uma mensagem
8. Como tratar erros com `try` e `except`?

    Utiliza o `try` para fazer um bloco de codigo e caso de algum erro ele vai direto para o `except` que pode ser tratado
9.  O que são argumentos de uma função?

    São os parametros que são passados para uma função para que ela possa utiliza-los
10. Para que serve o `return`?

    Serve para retornar algo da função para quem o chamou
11. O que são dicionários em Python? Dê um exemplo.

    Dicionario é uma estrutura de dados que armazena pares chave -> valor

    ```python
    data = {nome: 'Rafael', idade: 22}
    ```

12. O que é PEP8?

    A PEP8 é um guia de estilos para escrever codigos em Python de forma legível, organizada e consistente
13. O que são ambientes virtuais e por que são usados?


    Um ambiente virtual eé um isolamento do interpretador e das bibliotecas para uma aplicação especifica. Ele são usados para isolar aplicaçoes, reprodutibilidade e organização
14. Como instalar pacotes com pip?

    Só dar um `pip install pacote`
15. O que faz `pip freeze > requirements.txt`?

    Coloca todos os pacotes instalados em um txt
16. O que é o Poetry e para que serve?

    O Poetry é uma ferramenta que ajuda a gerenciar pacotes e dependencias no Python. Ele serve para criar ambiente virtuais, garantir reprodutibilidade, publicar bibliotecas no PyPl, gerenciar dependencias.

18. Como instalar uma dependência com o Poetry?

    Basta dar o comando
    ```bash
    poetry add nome_do_pacote
    ```
19. Como ativar o ambiente do Poetry?

    Basta dar o comando
    ```bash
    poetry shell
    ```
    Logo apos o comando
    ```bash
    poetry run python main.py
    ```
20. O que é uma API?

    Uma API(*Application Programming Interface*) 
    é um conjunto de regras e padrões para que diferentes sistemas, aplicações ou compontentes possam se comunicar entre si.
21. Qual a diferença entre GET e POST?

    `GET` é uma requisição que obtem dados do servidor.

    `POST` é uma requisição que envia dados ao servidor.
22. O que é JSON?

    Json é um formato leve de troca de dados, facil de ler e escrever utilizado majoritariamente em API's
23. O que significa 404 em uma resposta HTTP?

    Rota nao encontrada
24. O que são rotas/endpoints?

    Rotas/endpoints são caminhos de acessos a recursos ou funcionalidades de uma aplicação web ou API.
25. O que é um token de autenticação?

    Um token de autenticação é um valor único (geralmente uma string) que representa a identidade e permissões de um usuário durante um período de sessão.
---

### PARTE 2 - QUESTÕES PRÁTICAS (25 pontos)

**Python Básico**
26\. Crie uma função `soma(a, b)` que retorna a soma de dois números.

27\. Crie uma função que verifica se um número é par.

28\. Crie uma lista com os números de 1 a 10.

29\. Escreva uma função que retorne a quantidade de vogais em uma string.

30\. Crie um dicionário com nome, idade e cidade. Imprima os valores.

**APIs e Lógica Simples**
31\. Crie um arquivo `main.py` com uma API FastAPI com rota GET `/` que retorna `"API online"`.

32\. Crie uma rota GET `/soma` que receba `a` e `b` como query params e retorne a soma.

33\. Crie uma rota POST `/echo` que receba um JSON com `{"mensagem": "texto"}` e retorne o mesmo JSON.

34\. Crie um pydantic model `Usuario` com nome e idade.

35\. Crie uma rota POST `/usuario` que receba um `Usuario` e retorne a mensagem `"Usuario recebido"`.

**Docker / Poetry / Projeto**
36\. Escreva um `pyproject.toml` com FastAPI como dependência.

37\. Escreva um comando para instalar o `uvicorn` com Poetry.

38\. Escreva um Dockerfile básico para rodar a API.

39\. Crie um `docker-compose.yml` com FastAPI e PostgreSQL.

40\. Como expor a porta 8000 no Docker Compose?

**Extra - Simulação de Case GitHub Simples**
41\. Escreva uma função `contar_commits(usuario, repo)` que use `requests` para acessar a API do GitHub e retorne a quantidade de commits.

42\. Crie uma rota GET `/commits` que receba `usuario` e `repo` como query params e use a função acima.

43\. Adicione tratamento de erro caso o repositório não exista.

44\. Crie uma rota GET `/commits/mensagem` que mostre a mensagem do commit mais recente.

45\. Como evitar que o repositório seja clonado mais de uma vez?

**Testes / Qualidade / Execução**
46\. Escreva um teste com `pytest` que testa a rota `/`.

47\. Crie um script `start.sh` que roda o servidor com uvicorn.

48\. Como rodar a API usando `poetry run`?

49\. Crie uma função que valida se a idade é maior que 18.

50\. O que deve ser retornado se uma requisição é feita com dados inválidos?

---

**Pontuação Final: 50 pontos**

* 0-20: Iniciante
* 21-30: Júnior inicial
* 31-40: Júnior completo
* 41-49: Quase pleno
* 50: Pronto para subir de nível

**Dica:** organize as respostas em um arquivo `.py`, `.md`, `.pdf` ou `.zip` e envie aqui para correção.
