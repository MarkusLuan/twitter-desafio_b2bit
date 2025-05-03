# Documentação Tecnica

### Requisitos
- [x] Python 3
- [x] Com algum framework Web (Preferencia Django) - Irei utilizar o Flask
- [x] Autenticação com JWT
- [x] Banco de Dados de preferencia PostgreSQL
- [x] Sistema de cache para sistema de likes e seguidores
- [x] Paginação
- [x] Testes unitários
- [ ] Documentação com Swagger ou Postman
- [x] Docker com o Docker-compose

### Casos de uso
- Caso 1: Cadastro
    - [x] Os usuários deverão ser capazes de se registrar usando email, nome e senha
    - [x] A autenticação para login e gerenciamento de sessão deverá ser com JWT
- Caso 2: Postagens
    - [x] Os usuários logados podem postar com texto
    - [x] Os usuários logados podem postar com uma imagem
    - [x] As postagens podem ser curtidas por outros usuários
- Caso 3: Seguidores
    - [x] Os usuários logados podem Seguir ou Deixar de Seguir outros usuários
    - [x] O Feed deve mostrar apenas postagens dos usuários que a pessoa segue
- Caso 4: Feed
    - [x] O usuário pode visualizar uma lista de postagens dos usuários que segue de forma paginada
    - [x] As postagens devem ser ordernadas pela data de criação, do mais recente ao mais antigo

### Bonus - Provavelmente não consiga concluir a tempo
- [x] Criar o Front-end em React.js - Link no [github](https://github.com/MarkusLuan/twitter-desafio_b2bit-front)
- [ ] Limitador de banda nos endpoints para evitar abuso
- [ ] Recursos de segurança para evitar SQL Injection e para garantir a Validação dos Dados
- [ ] Tarefas async com Celery ou outra ferramenta
- [x] Sistema de busca
- [x] Continuos Integration (Github Actions para testes)