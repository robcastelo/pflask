from flask import Flask, render_template    


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')




@app.route('/aluno')
def listar_aluno():
    lista_alunos = [
        (1, "Ana", 20, "Teresina"),
        (2, "Paulo", 20, "Altos"),
        (3, "Claudio", 18, "Codó"),
        (4, "Mateus", 19, "Teresina"),
        (5, "Julia", 21, "Parnaíba")
    ]
    return render_template('aluno/lista.html', lista_alunos=lista_alunos)


@app.route('/professor')
def lista_professor():    
    return render_template('professor/lista.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')



@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


if __name__ == '__main__':
    app.run(debug=True)