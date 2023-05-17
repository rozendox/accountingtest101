import sqlite3


class Cont:
    def __init__(self):
        self.conn = sqlite3.connect("contabilidadeteste2.db")
        self.cursor = self.conn.cursor()

    def adicionar_dados_seg(self):
        try:
            sql_query = f"INSERT INTO janeiro(entrada,gastos)Values ({entrada}, {gastos})"
            self.cursor.execute(sql_query)
            self.conn.commit()
            return "dados inseridos"
        except Exception as e:
            return f"Operação não-sucedida. Erro {e}"
