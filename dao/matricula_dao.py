from dao.db_config import get_connection

class MatriculaDAO:
    sqlSelect = 'SELECT matricula.id, turma.semestre, aluno.nome, curso.nome_curso, professor.nome, professor.disciplina FROM matricula JOIN aluno ON matricula.aluno_id = aluno.id JOIN curso ON matricula.curso_id = curso.id JOIN turma ON matricula.turma_id = turma.id JOIN professor ON turma.professor_id = professor.id order by matricula.id desc'

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        conn.close()
        return lista

    def salvar(self, id, aluno_id, curso_id, turma_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            if id: # Atualizar pois um valor para o ID foi informado
                cursor.execute(
                    'UPDATE matricula SET aluno_id = %s, curso_id = %s, turma_id = %s WHERE id = %s',
                    (aluno_id, curso_id, turma_id, id)
                )
            else: # Inserir
                cursor.execute(
                    'INSERT INTO matricula (aluno_id, curso_id, turma_id) VALUES (%s, %s, %s)',
                    (aluno_id, curso_id, turma_id)
                )
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()

    def buscar_por_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, aluno_id, curso_id, turma_id FROM matricula WHERE id = %s', (id,))
        registro = cursor.fetchone()
        conn.close()
        return registro

    def remover(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM matricula WHERE id = %s', (id,))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()