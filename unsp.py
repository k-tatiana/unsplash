from app import app, db
from app.models import Images, User

#PORT = 5002
app.run(debug=True, use_reloader=False)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Images': Images}
