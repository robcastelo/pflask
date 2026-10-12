from flask import Flask, render_template, request
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.turma_dao import TurmaDAO
from dao.curso_dao import CursoDAO

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
    return render_template('aluno/lista.html', lista=lista)

@app.route('/professor')
def listar_professor():
    dao = ProfessorDAO()
    lista = dao.listar()
    return render_template('professor/lista.html', lista=lista)


@app.route('/turma')
def listar_turma():
    dao = TurmaDAO()
    lista = dao.listar()
    return render_template('turma/lista.html', lista=lista)

@app.route('/curso')
def listar_curso():
    dao = CursoDAO()
    lista = dao.listar()
    return render_template('curso/lista.html', lista=lista)


@app.route('/contato')
def contato():
    return render_template('dashboard/contato.html')

@app.route('/saudacao1/<nome>')
def saudacao1(nome):
    return render_template('saudacao/saudacao.html', valor_recebido=nome)


@app.route('/saudacao2/')
def saudacao2():
    nome = request.args.get('nome')
    return render_template('saudacao/saudacao.html', valor_recebido=nome)

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    senha = request.form['senha']
    email = request.form['email']
    dados = f"Usuário: {usuario}, Senha: {senha}, E-mail: {email}"
    return render_template('saudacao/saudacao.html', valor_recebido=dados)

@app.route('/desafio2/')
def desafio2():
    nome = request.args.get('nome')
    return render_template('desafio/desafio.html', valor_recebido=nome)


@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    nascimento = request.form['nascimento']
    cpf = request.form['cpf']
    nome_mae = request.form['nome_mae']
    dados = f"Usuário: {usuario}, Nascimento: {nascimento}, CPF: {cpf}, Nome da Mãe: {nome_mae}"
    return render_template('desafio/desafio.html', valor_recebido=dados)

@app.route('/desafio1/<nome>')
def desafio1(nome):
    return render_template('desafio/desafio.html', valor_recebido=nome)

if __name__ == '__main__':
    app.run(debug=True)
