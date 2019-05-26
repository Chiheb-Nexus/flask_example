#
# Shell entrypoint to manage our APP
#

from models import (
    app,
    db,
    User,
    Post,
    Comment,
    migrate
)


@app.shell_context_processor
def make_shell_context():
    """Create a shell context"""
    return dict(
        app=app,
        db=db,
        User=User,
        Post=Post,
        Comment=Comment,
        migrate=migrate
    )
