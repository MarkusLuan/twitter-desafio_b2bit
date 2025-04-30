# Estrutura do Projeto

```bash
Root/
├── .env/                 => Ambiente do python
├── db/                   => Volume do docker para o banco
├── docs/                 => Documentação do projeto
├── src/                  => Pasta de código fonte do projeto
│   ├── config/           => Configurações de ambiente
│   ├── models/           => DataModels do banco de dados
│   ├── resources/        => Registros das rotas
│   ├── tests/            => Testes
│   ├── app_singleton.py  => Variaveis globais em runtime
│   ├── app.py            => Arquivo principal (main)
│   ├── error_handler.py  => Tratamento de erros do flask
│   ├── utils.py          => Funções genericas e helpers
│   └── wsgi.py           => Gateway para servidor de produção
├── feed_img/             => Pasta onde ficam as imagens das postagens
├── docker-compose.yml    => Configuração do Docker-compose
├── Dockerfile            => Criação do ambiente Docker
├── requirements.txt      => Dependencias do projeto
└── site.conf             => Configurações do apache
```


    