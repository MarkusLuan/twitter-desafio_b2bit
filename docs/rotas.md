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
```

**Response - JSON**
```json
{
    "access_token": "<ACCESS_TOKEN>",
    "created_at": 1746317411.535121,
    "expires_in": 1746321011.535121,
    "refresh_token": "<REFRESH_TOKEN>"
}
```

##### 🟦 **GET** Obter informações do Usuario Logado

`/auth/info`

**Headers**
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer Auth" // Gerado no /auth/token
}
```

**Body - JSON**
```json
{
"username": "jisasas@dandsjnsad",
"senha": "dajdna"
}
```

**Response - JSON**
```json
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
```

##### 🟦 **POST** Renovar Token

`/auth/refresh`

**Headers**
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer Refresh_Token" // Gerado no /auth/token
}
```

**Body - EMPTY**

**Response - JSON**
```json
{
    "access_token": "<ACCESS_TOKEN>",
    "created_at": 1746317909.137471,
    "expires_in": 1746321509.137471,
    "refresh_token": "<REFRESH_TOKEN>"
}
```

##### 🟦 **GET** Obter informações do Usuario Logado

`/auth/info`

**Headers**
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer Auth" // Gerado no /auth/token
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
</div>

<div id="users" >

# 📁 Users
##### 🟦 **GET** Pesquisar Usuários

`/users?search=<string:nick_ou_nome>&first_result=0&max_results=5&ts_after=1746321693&ts_before=0`

**Headers**
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer Auth" // Gerado no /auth/token
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


##### 🟦 **GET** Informações do Usuário

`/users/<string:nick>`

**Headers**
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer Auth" // Gerado no /auth/token
}
```

**Body - EMPTY**

**Response - JSON**
```json
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

**Response - JSON**
```json
{
    "bio": "teste",
    "count_seguidores": 0,
    "count_seguindo": 0,
    "dt_criacao": "2025-05-03T04:15:26.925508",
    "dt_nascimento": "2024-04-12",
    "nick": "markus_lu",
    "nome": "markus_lu",
    "uuid": "85909aae-4e70-43d9-b5ad-2d189dda3943"
}
```

</div>

<div id="feed">

# 📁 Feed
##### 🟦 **GET** Carregar Feed

`/feed/?first_result=0&max_results=5&ts_after=1746321693&ts_before=0`

**Headers**
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer Auth" // Gerado no /auth/token
}
```

**Body - EMPTY**

**Response - JSON**
```json
[
    {
        "count_likes": 0,
        "created_by": "teste",
        "dt_criacao": "2025-05-03T22:36:47.388086",
        "has_image": true,
        "is_liked": false,
        "texto": "fddsdfsfdfs",
        "uuid": "f4f38e55-85f8-41db-b15a-574fd9e7ee27"
    },
    {
        "count_likes": 0,
        "created_by": "teste",
        "dt_criacao": "2025-05-03T22:24:23.695525",
        "has_image": false,
        "is_liked": false,
        "texto": "testando 1234",
        "uuid": "14747a71-cde9-420b-b0c8-3ca837ce598b"
    },
    {
        "count_likes": 0,
        "created_by": "teste",
        "dt_criacao": "2025-05-03T22:21:33.060783",
        "has_image": false,
        "is_liked": false,
        "texto": "adsadada",
        "uuid": "20ca84bb-5424-41f2-97e3-651d62428831"
    }
]
```

##### 🟦 **GET** Carregar Imagem da Postagem

`/feed/<uuid:uuid_feed>/img`

**Headers**
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer Auth" // Gerado no /auth/token
}
```

**Body - EMPTY**

**Response - Base64 IMAGE/\***
```json
"data:image/*;base64,<imageData>"
```

##### 🟦 **POST** Criar Postagem | 🟦 **PUT** Editar Postagem

`/feed`

**Headers**
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer Auth" // Gerado no /auth/token
}
```

**Body**
```json
{
"texto": "olá, testando postagem"
}
```

**Response - JSON**
```json
{
    "count_likes": 0,
    "created_by": "teste",
    "dt_criacao": "2025-05-04T00:39:11.791228",
    "has_image": false,
    "is_liked": false,
    "texto": "olá, testando postagem",
    "uuid": "29e71b37-c1ef-4908-a1ec-86a06765e098"
}
```

##### 🟦 **POST** Criar Postagem com Imagem | 🟦 **PUT** Editar Postagem com Imagem

`/feed`

**Headers**
```json
{
    "Content-Type": "multipart/form-data",
    "Authorization": "Bearer Auth" // Gerado no /auth/token
}
```

**Body - FormData**
```json
{
    "texto": "testando post com imagem",
    "img": "<binaryFile>"
}
```

**Response - JSON**
```json
{
    "count_likes": 0,
    "created_by": "teste",
    "dt_criacao": "2025-05-04T00:40:31.866312",
    "has_image": true,
    "is_liked": false,
    "texto": "testando post com imagem",
    "uuid": "c535367d-4017-4c69-adb3-57191fbd748d"
}
```

##### 🟦 **DELETE** Deletar Postagem

`/feed/<uuid:uuid_feed>`

**Headers**
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer Auth" // Gerado no /auth/token
}
```

**Body - EMPTY**

**Response - JSON**
```json
{
    "count_likes": 0,
    "created_by": "teste",
    "dt_criacao": "2025-05-04T00:40:31.866312",
    "has_image": true,
    "is_liked": false,
    "texto": "testando post com imagem",
    "uuid": "c535367d-4017-4c69-adb3-57191fbd748d"
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
    "Authorization": "Bearer Auth" // Gerado no /auth/token
}
```

**Body - EMPTY**

**Response - JSON**
```json
[
    {
        "dt_criacao": "2025-05-04T00:51:29.732808",
        "liked_by": "teste",
        "uuid": "af06e361-4ebf-47c5-bb00-d41a17d51581"
    }
]
```

##### 🟦 **POST** Deixar Like

`/likes/<uuid:uuid_feed>`

**Headers**
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer Auth" // Gerado no /auth/token
}
```

**Body - EMPTY**

**Response - JSON**
```json
{
    "dt_criacao": "2025-05-04T00:51:29.732808",
    "liked_by": "teste",
    "uuid": "af06e361-4ebf-47c5-bb00-d41a17d51581"
}
```

##### 🟦 **DELETE** Remover Like

`/likes/<uuid:uuid_feed>`

**Headers**
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer Auth" // Gerado no /auth/token
}
```

**Body - EMPTY**

**Response - JSON**
```json
{
    "dt_criacao": "2025-05-04T00:51:29.732808",
    "liked_by": "teste",
    "uuid": "af06e361-4ebf-47c5-bb00-d41a17d51581"
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
    "Authorization": "Bearer Auth" // Gerado no /auth/token
}
```

**Body - EMPTY**

**Response - JSON**
```json
[
    {
        "dt_criacao": "2025-05-04T00:55:44.342838",
        "seguidor": "teste",
        "seguindo": "sdfsdfds",
        "uuid": "bf5a2ac1-b6ef-415a-9acf-9df12741b1a4"
    }
]
```

##### 🟦 **POST** Seguir Usuário

`/followers/<string:nick>`

**Headers**
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer Auth" // Gerado no /auth/token
}
```

**Body - EMPTY**

**Response - JSON**
```json
{
    "dt_criacao": "2025-05-04T00:55:44.342838",
    "seguidor": "teste",
    "seguindo": "sdfsdfds",
    "uuid": "bf5a2ac1-b6ef-415a-9acf-9df12741b1a4"
}
```

##### 🟦 **DELETE** Deixar de Seguir

`/followers/<string:nick>`

**Headers**
```json
{
    "Content-Type": "application/json",
    "Authorization": "Bearer Auth" // Gerado no /auth/token
}
```

**Body - EMPTY**

**Response - JSON**
```json
{
    "dt_criacao": "2025-05-04T00:55:44.342838",
    "seguidor": "teste",
    "seguindo": "sdfsdfds",
    "uuid": "bf5a2ac1-b6ef-415a-9acf-9df12741b1a4"
}
```
</div>
