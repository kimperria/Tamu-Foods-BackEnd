from app import  createapp,db


app = createapp()



@app.shell_context_processor
def make_shell_context():
    return dict(db=db)