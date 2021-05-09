For DEV
1. git clone https://github.com/Yehuda1977/flask_skeleton <NEW_DIRECTORY_NAME>
2. Make sure that after you clone the repository you change your remote origin using the following command:
    git remote set-url origin <NAME_OF_YOUR_GIT_REPOSITORY>
3. pip3 install -r requirements.txt
4. export set SECRET_KEY="whatever_you_want"
5. export set FLASK_ENV="dev"
6. export set MAIL_PASSWORD="whateveryourmailpasswordis"   #best to user google application password
7. flask db init
8. flask db migrate
9. flask db upgrade


For PRODUCTION
1. heroku login
2. heroku apps:create <name_of_the_app>
3. heroku addons:create heroku-postgresql:hobby-dev --app <app_name>
4. heroku run flask db upgrade --app <app_name>
5. heroku config:set SECRET_KEY="whatever_you_want"
6. heroku config:set FLASK_ENV="prod"
7. git add .
8. git commit -m "deploy"
9. git push heroku master


