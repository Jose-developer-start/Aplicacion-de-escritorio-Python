from tkinter import *
from tkinter import ttk
from tkinter import messagebox as message
import consultas
class app:
	def __init__(self, windows):
		self.wind = windows
		self.wind.title("Aplicacion CRUD")
		#	Instanciando un objeto
		self.query = consultas.query()
		#Frame Label
		frame = LabelFrame(self.wind, text="Registrar")
		frame.grid(row=0, column=0, columnspan=3,ipadx=20)
		Label(frame,text="Nombre: ").grid(row=1, column=1)
		self.name = Entry(frame)
		self.name.grid(row=1, column=2, pady=5)

		Label(frame,text="Email: ").grid(row=2, column=1)
		self.email = Entry(frame)
		self.email.grid(row=2, column=2, pady=5)

		#Btn enviar
		ttk.Button(frame, text="Guardar", command=self.guardar).grid(row=3, columnspan=3, sticky=W + E)

		self.tabla0 = ttk.Treeview(height=10, column=2)
		self.tabla0.grid(row=4, column=0, columnspan=2)
		self.tabla0.heading("#0",text="Nombre",anchor='center')
		self.tabla0.heading("#1",text="Correo",anchor='center')
		self.mostrar()
	def guardar(self):
		name = self.name.get()
		email = self.email.get()
		if(email !='' and email !=''):
			self.query.save(name,email)
			message.showinfo(message="Datos almacenados", title="Guardados")
			self.name.delete(0,END)
			self.email.delete(0,END)

			self.mostrar()
		else:
			message.showinfo(message="Ingrese los datos", title="Por favor")

	def mostrar(self):
		delete = self.tabla0.get_children()
		for elemento in delete:
			self.tabla0.delete(elemento)
		rows = self.query.read()
		for row in rows:
			self.tabla0.insert('',END, text=row[1],value=row[2])

if __name__=="__main__":
	root = Tk()
	Aplicacion = app(root)
	root.mainloop()