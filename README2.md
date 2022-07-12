# Additional commands that need to be run in environment:
# -----------------------------------------------------------------
(env) wswong2$ pip3 install gunicorn

(env) wswong2$ pip3 freeze > requirements.txt

(env) wswong2$ git init

(env) wswong2$ git add .

(env) wswong2$ git commit -m "Init app"

Also need to have a Procfile with following contents:
------------------------------------------------------------
web: gunicorn  app:app

