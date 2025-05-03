# Estrutura do Projeto

```bash
Root/
├── .env/                           => Ambiente do python
├── db/                             => Volume do docker para o banco
├── docs/                           => Documentação do projeto
├── src/                            => Pasta de código fonte do projeto
│   ├── config/                     => Configurações de ambiente
│   ├── exceptions/                 => Exceções customizadas
│   ├── models/                     => DataModels do banco de dados
│   ├── repositories/               => Comunicações com o banco através dos DataModels
│   ├── resources/                  => Registros das rotas
│   │   └── api/                    => Registros das rotas - Para o endpoint /api
│   │       └── \<resource\>/       => Registros das rotas - Para o endpoint /\<resource\>
│   │           └── __init__.py     => Declaração da rota
│   │           └── routes.py       => Classe de implementação da rota
│   ├── tests/                      => Testes
│   ├── app_singleton.py            => Variaveis globais em runtime
│   ├── app.py                      => Arquivo principal (main)
│   ├── error_handler.py            => Tratamento de erros do flask
│   ├── migrate.py                  => Inicialização do banco - Cuidado pois recria o banco quando executado
│   ├── utils.py                    => Funções genericas e helpers
│   └── wsgi.py                     => Gateway para servidor de produção
├── feed_img/                       => Pasta onde ficam as imagens das postagens
├── docker-compose.yml              => Configuração do Docker-compose
├── Dockerfile                      => Criação do ambiente Docker
├── requirements.txt                => Dependencias do projeto
└── site.conf                       => Configurações do apache
```


    