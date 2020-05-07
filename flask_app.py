from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

##### Configurar o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bancoDeDados.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#####

##### Criar o modelo para o registro do usuario
# class Usuario(db.Model):
#     codigo = 

class Apontamento(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_usuario = db.Column(db.String(25), nullable=True)
    hora = db.Column(db.DateTime, default=datetime.now)

db.create_all()

@app.route('/inicio')
@app.route('/')
def mostra_inicio():
    return render_template('index.html')

# @app.route('/api/funcionarios', methods=['GET', 'POST'])
# def funcionarios():
#     usuario = Apontamento(nome_usuario=)
#     db.session.add(usuario)
#     db.session.commit()



@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/login')
def login():
    return render_template('login.html')





## Para rodar o projeto em desenvolvimento

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
