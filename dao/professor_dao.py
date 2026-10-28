from dao.db_config import get_connection

class ProfessorDAO:

    sqlSelect = 'SELECT id, nome, disciplina from professor'

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        conn.close()
        return lista

    def salvar(self, id, nome, disciplina):
            conn = get_connection()
            cursor = conn.cursor()
            try:
                cursor.execute('INSERT INTO professor (nome, disciplina) VALUES (%s, %s)', (nome, disciplina))
                conn.commit()
                return {"status": "ok"}
            
            except Exception as e:
                return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
            
            finally:
                conn.close()

    def buscar_por_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, nome, disciplina FROM professor WHERE id = %s', (id,))
        professor = cursor.fetchone()
        conn.close()
        return professor

    def remover(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM professor WHERE id = %s', (id,))
            conn.commit()
            return {"status": "ok"}
        
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        
        finally:
            conn.close()