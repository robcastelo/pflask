from flask import Flask, render_template
import sqlite3    


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')




@app.route('/aluno')
def listar_aluno():
    DB_PATH = "banco_escola.db"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id, nome, idade, cidade FROM aluno')
    lista = cursor.fetchall()
    conn.close()
    return render_template('aluno/lista.html', lista=lista)


@app.route('/professor')
def lista_professor():
    DB_PATH = "banco_escola.db"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id, nome, disciplina FROM professor')
    lista = cursor.fetchall()    
    conn.close()    
    return render_template('professor/lista.html')

@app.route('/turma')
def lista_turma():    
    DB_PATH = "banco_escola.db"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()    
    cursor.execute('select turma.id, semestre, curso.nome_curso, professor.nome from turma join curso on curso.id=turma.curso_id join professor on professor.id=turma.professor_id')    
    lista = cursor.fetchall()    
    conn.close()
    return render_template('turma/lista.html', lista=lista)


@app.route('/contato')
def contato():
    return render_template('contato.html')



@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


if __name__ == '__main__':
    app.run(debug=True)