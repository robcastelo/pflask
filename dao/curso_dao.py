from dao.db_config import get_connection

class CursoDAO:
    sqlSelect = 'SELECT id, nome_curso, duracao FROM curso'

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        return lista