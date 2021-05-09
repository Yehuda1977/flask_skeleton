For DEV
1. git clone https://github.com/Yehuda1977/flask_skeleton <NEW_DIRECTORY_NAME>
2. pip3 install -r requirements.txt
3. export set SECRET_KEY="whatever_you_want"
4. export set FLASK_ENV="dev"
5. export set MAIL_PASSWORD="whateveryourmailpasswordis"   #best to user google application password
6. flask db init
7. flask db migrate
8. flask db upgrade


For PRODUCTION
1. heroku login
2. heroku apps:create <name_of_the_app>
3. heroku addons:create heroku-postgresql:hobby-dev --app <app_name>
4. heroku run flask db upgrade --app <app_name>
5. heroku config:set SECRET_KEY="whatever_you_want"
6. heroku config:set FLASK_ENV="dev"
7. git add .
8. git commit -m "deploy"
9. git push heroku master


