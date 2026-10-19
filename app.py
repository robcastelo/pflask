from flask import Flask, render_template, request, redirect, flash
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.turma_dao import TurmaDAO
from dao.curso_dao import CursoDAO

from dao.aluno_dao import alunoDAO
from dao.professor_dao import professorDAO

app = Flask(__name__)
app.secret_key = "uma_chave_muito_secreta_e_unica

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

@app.route('/aluno/form')
def form_aluno():
    return render_template('aluno/form.html', aluno=None)

@app.route('/aluno/salvar', methods=['POST'])
def salvar_aluno(id=None):
    nome = request.form['nome']
    idade = request.form['idade']
    cidade = request.form['cidade']
    dao = AlunoDAO()
    resultado = dao.salvar(None, nome, idade, cidade)
    if resultado["status"] == "ok":
        flash("Aluno salvo com sucesso!", "success")
    else:
        flash(f"Erro ao salvar aluno: {resultado['mensagem']}", "danger")
    return redirect('/aluno')

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



@app.route('/desafio/')
def desafio():
    nome = request.args.get('nome')
    return render_template('desafio/desafio.html', valor_recebido=nome)

@app.route('/formulario', methods=['POST'])
def formulario():
    nome = request.form['nome']
    data_nascimento = request.form['data_nascimento']
    cpf = request.form['cpf']
    nome_da_mae = request.form['nome_da_mae']
    dados = f"Nome: {nome}, Data de Nascimento: {data_nascimento}, CPF: {cpf}, Nome da Mãe: {nome_da_mae}"
    return render_template('desafio/desafio.html', valor_recebido=dados)



if __name__ == '__main__':
    app.run(debug=True)
