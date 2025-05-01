# Preparando sistema
FROM python:3.13-alpine

RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    build-base \
    apache2 \
    apache2-dev

RUN adduser -u 1000 -G www-data -s /bin/sh -D www-data

# Copiando projeto
WORKDIR /app
COPY requirements.txt /tmp/requirements.txt
COPY src .
COPY src/config/dev.py ./config/prod.py
COPY site.conf /etc/apache2/sites-available/000-default.conf

# Instalando dependencias
RUN python3 -m pip install --break-system-packages -U pip
RUN pip install --break-system-packages mod_wsgi
RUN pip install --break-system-packages -r /tmp/requirements.txt
RUN mod_wsgi-express install-module

RUN python3 migrate.py "config.prod"

# Subindo projeto
EXPOSE 80
CMD ["mod_wsgi-express", "start-server", "wsgi.py", "--port", "80", "--user", "www-data", "--group", "www-data"]