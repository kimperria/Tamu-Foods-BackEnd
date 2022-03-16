from app import  createapp,db
from app.model import User


app = createapp()



@app.shell_context_processor
def make_shell_context():
    return dict(db=db, user=User)