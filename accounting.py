import sqlite3

"""conn = sqlite3.connect('accountingtest101.db')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE Acc_Year
                  (year INTEGER, month text, Cash_Inflow REAL, Cash_Outflow REAL, Days_Balance REAL)''')


cursor.execute('''CREATE TRIGGER calculate_days_balance 
                  AFTER INSERT ON Acc_Year
                  FOR EACH ROW
                  BEGIN
                      UPDATE Acc_Year
                      SET Days_Balance = NEW.Cash_Inflow - NEW.Cash_Outflow
                      WHERE rowid = NEW.rowid;
                  END;''')

conn.close()"""


class connect:
    def __init__(self):
        self.conn = sqlite3.connect("accountingtest101.db")
        self.cursor = self.conn.cursor()


class accountancy(connect):
    def add_data(self, year, month, Cash_Inflow, Cash_Outflow):
        try:
            query = "INSERT INTO Acc_Year (year, month, Cash_Inflow, Cash_Outflow) VALUES (?, ?, ?, ?)"
            args = (year, month, Cash_Inflow, Cash_Outflow)
            self.cursor.execute(query, args)
            self.conn.commit()
            return "DATA ENTERED SUCCESSFULLY"
        except Exception as e:
            return f"OPERATION NOT SUCCESSFUL. ERROR {e}"


class ViewAccontM(connect):
    def view_by_month(self):
        try:
            month = str(input("Inform the Month "))
            self.cursor.execute("SELECT * FROM Acc_Year WHERE month = ?", (month,))
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
            self.conn.close()
            return "DATA VISUALIZED SUCCESSFULLY "
        except Exception as e:
            return f"OPERATION NOT SUCESSFUL. ERROR {e}"


class ViewAccounntY(connect):
    def view_by_year(self):
        try:
            year = str(input("Inform the Year"))
            self.cursor.execute("Select From Acc_Year where Year = ?", (year,))
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
            self.conn.close()
            return "DATA FILTERED BY YEAR VISUALIZED SUCESSFULLY"
        except Exception as e:
            return f"OPERATION NOT SUCECSSFUL. ERROR {e}"
