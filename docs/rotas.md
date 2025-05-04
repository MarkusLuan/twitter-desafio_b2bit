# Desafio Twitter B2Bit

Creditos ao repositorio no git que adiantou uma parte da documentação https://github.com/ntandoyenkosi1/postman-to-markdown

[Auth](#auth) - Rotas de Autenticação

[Users](#users) - Rotas de Usuario

[Feed](#feed) - Rotas do Feed (Postagens)

[Likes](#likes) - Rotas dos Likes

[Followers](#followers) - Rotas dos Seguidores

<div id="auth">

# 📁 Auth
##### 🟦 **POST** Gerar Token

`/auth/token`

**Headers**
```json
{
    "Content-Type": "application/json",
    "Authorization": "Basic Auth" // Consultar variaveis de ambiente em config
}
```

**Body - JSON**
```json
{
"username": "jisasas@dandsjnsad",
"senha": "dajdna"
}
````


##### 🟦 **GET** Obter informações do Usuario Logado

`/auth/info`

**Headers**
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer Auth" // Gerado no /auth/toke
}
```

**Body - JSON**
```json
{
"username": "jisasas@dandsjnsad",
"senha": "dajdna"
}
````
##### 🟦 **POST** Renovar Token

`/auth/refresh`


**Headers**
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer Auth" // Gerado no /auth/toke
}
```


##### 🟦 **GET** Obter informações do Usuario Logado

`/auth/info`

**Body - JSON**
```json
{
"username": "jisasas@dandsjnsad",
"senha": "dajdna"
}
```
</div>

<div id="users" >

# 📁 Users
##### 🟦 **GET** Pesquisar Usuários

`/users?search=<string:nick_ou_nome>&first_result=0&max_results=5&ts_after=1746321693&ts_before=0`


##### 🟦 **GET** Informações do Usuário

`/users/<string:nick>`

**Headers**
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer Auth" // Gerado no /auth/toke
}
```

**Body - EMPTY**

**Response - JSON**
```json
[
    {
        "bio": "dasdaaadad",
        "count_seguidores": 0,
        "count_seguindo": 0,
        "dt_criacao": "2025-05-03T04:15:26.925508",
        "dt_nascimento": "1980-01-01",
        "nick": "teste",
        "nome": "Markus Luan",
        "uuid": "85909aae-4e70-43d9-b5ad-2d189dda3943"
    }
]
```


##### 🟦 **POST** Salvar Usuário

`/users/`

**Headers**
```json
{
    "Content-Type": "application/json",
    "Authorization": "Basic Auth" // Consultar variaveis de ambiente em config
}
```

**Body** - JSON
```json
{
"dt_nascimento": "2024-04-12",
"nick": "markus_lu",
"nome": "markus_lu",
"email": "markus_lun@test.com",
"bio": "teste",
"senha": "1234"
}
```
</div>

<div id="feed">

# 📁 Feed
##### 🟦 **GET** Carregar Feed

`/feed/`

**Headers**
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer Auth" // Gerado no /auth/toke
}
```

##### 🟦 **GET** Carregar Imagem da Postagem

`/feed/<uuid:uuid_feed>/img`


##### 🟦 **POST** Criar Postagem

`/feed`

**Headers**
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer Auth" // Gerado no /auth/toke
}
```

**Body**
```json
{
"texto": "olá, testando postagem"
}
````
##### 🟦 **POST** Criar Postagem com Imagem

`/feed`

**Headers**
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer Auth" // Gerado no /auth/toke
}
```

**Body - JSON** 
```json
```

##### 🟦 **DELETE** Deletar Postagem

`/feed/<uuid:uuid_feed>`

**Headers**
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer Auth" // Gerado no /auth/toke
}
```
</div>
<div id="likes">

# 📁 Likes
##### 🟦 **GET** Listar curtidas

`/likes/<uuid:uuid_feed>`

**Headers**
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer Auth" // Gerado no /auth/toke
}
```

##### 🟦 **POST** Deixar Like

`/likes/<uuid:uuid_feed>`

**Headers**
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer Auth" // Gerado no /auth/toke
}
```

##### 🟦 **DELETE** Remover Like

`/likes/<uuid:uuid_feed>`

**Headers**
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer Auth" // Gerado no /auth/toke
}
```
</div>
<div id="followers">

# 📁 Followers
##### 🟦 **GET** Listar Seguidores do Usuário Logado

`/followers`

**Headers**
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer Auth" // Gerado no /auth/toke
}
```

##### 🟦 **POST** Seguir Usuário

`/followers/<uuid:uuid_feed>`

**Headers**
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer Auth" // Gerado no /auth/toke
}
```

##### 🟦 **DELETE** Deixar de Seguir

`/followers/<uuid:uuid_feed>`

**Headers**
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer Auth" // Gerado no /auth/toke
}
```
</div>
