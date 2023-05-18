import sqlite3


class connect:
    def __init__(self):
        self.conn = sqlite3.connect("contabilidadeteste1.db")
        self.cursor = self.conn.cursor()


class Cont(connect):

    def adicionar_dados_jan(self, entrada, gastos):
        try:
            sql_query = f"INSERT INTO janeiro(entrada, gastos) Values ({entrada}, {gastos})"
            self.cursor.execute(sql_query)
            self.conn.commit()
            return "DATA ENTERED SUCESSFULY"
        except Exception as e:
            return f"OPERATION NOT SUCCESSFUL. ERROR {e}"

    def adicionar_dados_fev(self, entrada, gastos):
        try:
            sql_query = f"INSERT INTO fevereiro(entrada, gastos) Values ({entrada}, {gastos})"
            self.cursor.execute(sql_query)
            self.conn.commit()
            return "DATA ENTERED SUCESSFULY"
        except Exception as e:
            return f"OPERATION NOT SUCCESSFUL. ERROR {e}"

    def adicionar_dados_mar(self, entrada, gastos):
        try:
            sql_query = f"INSERT INTO marco(entrada, gastos) Values ({entrada}, {gastos})"
            self.cursor.execute(sql_query)
            self.conn.commit()
            return "DATA ENTERED SUCESSFULY"
        except Exception as e:
            return f"OPERATION NOT SUCCESSFUL. ERROR {e}"


class ContVer(connect):

    @property
    def return_jan(self):
        try:
            self.cursor.execute("SELECT * FROM janeiro")
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
            self.conn.close()
            return "DATA ENTERED SUCESSFULY"
        except Exception as e:
            return "OPERATION NOT SUCCESSFUL. ERROR: {}".format(e)

    def return_fev(self):
        try:
            self.cursor.execute("SELECT * FROM fevereiro")
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
            self.conn.close()
            return "DATA ENTERED SUCESSFULY"
        except Exception as e:
            return "OPERATION NOT SUCCESSFUL. ERROR: {}".format(e)
