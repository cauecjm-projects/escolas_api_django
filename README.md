# Escolas API - Django Restframework

App Open Source Escolas API - Desenvolvido em Django Restframework com Docker

# Iniciar o projeto

Como o projeto está dockerizado, utilizar o docker-compose para inicialização.

```
sudo docker-compose up
```

Criar superuser para utilizar o Django Admin:

```
sudo docker-compose exec app python manage.py createsuperuser
```

# Features

- API desenvolvida em Django Restframework.
- Organização da arquitetura de pastas e arquivos do framework.
- Versionamento da API, considerando diferentes funcionalidades entre versões.
- Paginação do resultado da API.
- Customização e tratamento das respostas.
- Validações customizadas.