# Projeto para uma Vaga de Programador Python - B2Bit

O projeto irei fazer utilizando o framework Flask, por ter mais familiaridade com ele do que com o DJango

---

### Descrição
O projeto se trata de uma API RESTFUL para um sistema de midia social, onde os usuários poderão:
- [ ] Registrar e Autenticar
- [ ] Criar, Editar e Deletar Postagem
- [ ] Curtir Postagens
- [ ] Seguir e Deixar de Seguir Outros Usuários
- [ ] Visualizar o Feed
- [ ] Mostrar apenas postagens dos usuários seguidos

As Views e Models foram separados em vários arquivos nas suas respectivas pastas para garantir um código mais limpo.

---

### Banco de Dados
Estou avaliando se utilizo o Postgres ou MySQL

---

### Documentações
- [Documentação Tecnica](./docs/README.md)
- [Estrutura do Projeto](./docs/estrutura_projeto.md)

---

### Execução
#### Python
Para executar diretamente no python é necessário ter um banco de dados Postgres ou MySQL rodando na maquina

1. Acessar a pasta raiz do projeto (onde está localizado o [requirements.txt](./requirements.txt))
2. Abrir o terminal e digitar (a parte do ambiente é opcional)
##### Windows
```shell
python -m venv .env
.env\scripts\activate
python -m pip install -U pip
pip install -r requirements.txt
```
##### Linux ou Mac
```shell
python -m venv .env
source .env/scripts/activate
python -m pip install -U pip
pip install -r requirements.txt
```
3. Acessar a pasta [src](./src/) (onde fica o codigo fonte do projeto) e executar o seguinte comando no terminal
```shell
python app.py
```