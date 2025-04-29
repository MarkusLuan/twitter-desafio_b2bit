# Preparando sistema
FROM python:3.13-slim

RUN apt-get update
RUN apt-get install -y apache2 apache2-dev
RUN apt-get install -y apache2-mod-wsgi

# Copiando projeto
WORKDIR /app
COPY requirements.txt /tmp/requirements.txt
COPY src .
COPY site.conf /etc/apache2/sites-available/000-default.conf
RUN python3 -m pip install -U pip mod_wsgi
RUN pip3 install -r /tmp/requirements.txt
RUN mod_wsgi-express install-module

# Alterando permissões
RUN chown -R www-data:www-data *
RUN chmod -R 755 *

# Subindo projeto
EXPOSE 80
CMD ["apachectl", "-D", "FOREGROUND"]