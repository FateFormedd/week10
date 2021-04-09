from app import create_app, db
from app.models import Divvy

if __name__ == '__main__'".env":
    App.run(host=localhost, port=5555)


app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Kekambas': Kekambas, 'Product': Product}