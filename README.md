# Problema 1

Para a primeira questão, coloque as strings num arquivo de input.txt e ao executar o código no prompt de comando, execute:

    $ python (ou python3) q1.py < input.txt

O output será no formato de uma única string que representará a resposta.

# Problema 2
A segunda questão, apesar de não receber input, é possível alterar a lista de adjacência do grafo no código.

O output será no formato de uma lista onde a ordem de carregamento dos módulos se dará pelos números da esquerda para a direita da lista.

    [1º, 2º, 3º, ... , último]

# Problema 3
A pasta "trydjango" é o ambiente virtual (virtual environment) que contem o projeto.

Versões utilizadas:

- Virtualenv: 15.1.0 (Ferramenta Python)
- Python: 3.6.X
- Django: 2.0.7
- Psycopg2: 2.8.4 (Biblioteca Python)

Para executar, siga os seguintes passos:
- Vá até a pasta inicial e execute:
```
$ source bin/activate
```
- Vá até a pasta /src. Essa é a pasta da aplicação web.
```
$ cd src
```
- Execute:
```
$ python (ou python3) manage.py runserver
```
  Você deverá ver no prompt de comando uma mensagem como a seguinte:
  ```
    January 23, 2020 - 15:49:49
    Django version 2.0.7, using settings 'trydjango.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
```
- Agora basta acessar o link e uma página de login deverá ser carregada.
- Se já não tiver uma conta no banco de dados, é possível se cadastrar apertando no botão "Fazer cadastro".
- Ao fazer login, a próxima tela que deverá ser carregada é a tela de buscas. Para realizar uma busca, digite o nome da doença sem
aspas, ou, se a busca for por múltiplas doenças, digite conforme a seguinte formatação:

    "nome da doença", "nome de outra doença", "nome de outra"

  E após clicar no botão "Submit", a próxima tela será uma com os genes cadastrados a essa doença no banco de dados, ou a seguinte mensagem caso a doença não esteja cadastrada:
  
  Doença não encontrada. Tente outra vez.
- O banco de dados já estará criado com as doenças. Para atualizá-lo é possível rodar:
```
$ python (ou python3) manage.py update_local
```