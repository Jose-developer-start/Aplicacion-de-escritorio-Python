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

	def guardar(self):
		name = self.name.get()
		email = self.email.get()
		if(email !='' and email !=''):
			self.query.save(name,email)
			message.showinfo(message="Datos almacenados", title="Guardados")
		else:
			message.showinfo(message="Ingrese los datos", title="Por favor")


if __name__=="__main__":
	root = Tk()
	Aplicacion = app(root)
	root.mainloop()