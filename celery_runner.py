#
# Generate a Celery instance with our Flask configs
#   PS: use this command to run Celery:
#       celery -A celery_runner.celery_app worker --loglevel=info
#   BONUS: Enable RabbitMQ web app Management:
#       $> sudo rabbitmq-plugins enable rabbitmq_management

from celery import Celery
from main import app


def make_celery(app):
    """Generate celery instance from flask config"""
    celery = Celery(
        app.import_name,  # APP name as str; used only for RabbitMQ to identify your tasks
        broker=app.config['CELERY_BROKER_URL'],  # We'll read them from flask config
        backend=app.config['CELERY_RESULT_BACKEND'],  # We'll read them from flask config
        include=['tasks']  # Here add your tasks file
    )
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask

    return celery


celery_app = make_celery(app)
#
# OR you can generate the celery runnner like this:
# celery_app = Celery(
#   'tasks_app',
#   include=['tasks'],
#   broker='pyamqp://USER:PASSWORD@localhost/YOUR_VHOST')
