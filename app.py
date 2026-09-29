from flask import Flask, render_template
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.turma_dao import TurmaDAO

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard/index.html')


@app.route('/sobre')
def sobre():
    return render_template('dashboard/sobre.html')


@app.route('/aluno')
def listar_alunos():
    dao = AlunoDAO()
    lista = dao.listar()
    return render_template('aluno/lista_aluno.html', lista=lista)

@app.route('/professor')
def listar_professor():
    dao = ProfessorDAO()
    lista = dao.listar()
    return render_template('professor/lista_professor.html', lista=lista)


@app.route('/turma')
def listar_turma():
    dao = TurmaDAO()
    lista = dao.listar()
    return render_template('turma/lista_turma.html', lista=lista)




@app.route('/contato')
def contato():
    return render_template('dashboard/contato.html')

if __name__ == '__main__':
    app.run(debug=True)
