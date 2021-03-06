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
		
	def delete(self,email):
		sql = "DELETE FROM empleados WHERE Email=?"
		parametros = (email,)
		results = self.ejecutar_consultar(sql,parametros)

	def update(self,nombre_nuevo,correo_nuevo,name,email):#Le pasamos los 4 parametros para actualizar el registro
		sql = "UPDATE empleados SET Name=?,Email=? WHERE Name=? AND Email=?"
		parametros = (nombre_nuevo,correo_nuevo,name,email)
		self.ejecutar_consultar(sql,parametros)
	
