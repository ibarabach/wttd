#Eventex

Sistema de Eventos encomendado pela Morena.

## Como desenvolver?

1. Clone o repositorio
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv
4. Instale as dependencias
5. Configure a instancia com o .env
6. Execute os testes.

```console
git clone git@github:ivan.barabach/eventex.git wtdd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test

```

## Como fazer o deploy?

1. Crie uma instancia no heroku
2. Envie as configuracoes para o heroku
3. Define uma SECRET_KEY segura para a instancia
4. Defina  DEBUG=False
5. Configure o servico de email
6. Envie o codigo para o heroku

```console
heroku create minhainsctancia
heroku config:push
heroku config:set SECRET_KEY=ASFDGAFDASDFAS
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force

```