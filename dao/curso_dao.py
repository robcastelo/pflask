from dao.db_config import get_connection

class CursoDAO:

    sqlSelect = 'SELECT id,nome_curso,duracao from curso'

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        conn.close()
        return lista

    def salvar(self, id, curso, duracao):
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                'INSERT INTO curso (nome_curso, duracao) VALUES (%s, %s)',(curso, duracao))

            conn.commit()
            return {"status": "ok"}

        except Exception as e:
            conn.rollback()
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}

        finally:
            cursor.close()
            conn.close()