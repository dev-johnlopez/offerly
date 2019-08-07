web: flask db upgrade; gunicorn offerly:app
admin: flask users create john@johnlopez.org --password some-dummy-password --active
#worker: rq worker -u $REDIS_URL offerly-tasks
