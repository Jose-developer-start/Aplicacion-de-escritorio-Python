import sqlite3

class query():
	def __init__(self):
		self.db = "database.db"
	def ejecutar_consultar(self,sql,parametros=()):
		with sqlite3.connect(self.db) as conn:
			cursor = conn.cursor()
			result = cursor.execute(sql,parametros)
			conn.commit()
			return result

	def save(self,name,email):
		sql = "INSERT INTO empleados(Name,Email) VALUES(?,?)"
		parametros =(name,email)
		self.ejecutar_consultar(sql, parametros)

	def read(self):
		sql = "SELECT * FROM empleados ORDER BY ID ASC"
		results = self.ejecutar_consultar(sql)
		return results