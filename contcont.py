import sqlite3


class Cont:
    def __init__(self):
        self.conn = sqlite3.connect("contabilidadeteste1.db")
        self.cursor = self.conn.cursor()

    def adicionar_dados_seg(self, entrada, gastos):
        try:
            sql_query = f"INSERT INTO janeiro(entrada,gastos)Values ({entrada}, {gastos})"
            self.cursor.execute(sql_query)
            self.conn.commit()
            return "dados inseridos"
        except Exception as e:
            return f"Operação não-sucedida. Erro {e}"

    def adicionar_dados_fev(self, entrada, gastos):
        try:
            sql_query = f"INSERT INTO fevereiro(entrada, gastos) Values ({entrada}, {gastos})"
            self.cursor.execute(sql_query)
            self.conn.commit()
            return "Dados Inseridos"
        except Exception as e:
            return f"operação não sucedida. Erro {e}"
