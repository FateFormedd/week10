from app import app, db
from app.models import Divvy

if __name__ == '__main__'".env":
    app.run(host=localhost, port=5555)



@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Divvy': Divvy}