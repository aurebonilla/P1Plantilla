#CREO LA CLASE VARIABLE
class Variable:
    def __init__(self, fila, columna, ori, tam, valor):
        self.fila=fila
        self.columna=columna
        self.ori=ori
        self.tam=tam
        self.valor=None

#LO HICE PARA COMPROBAR EL CONSTRUCTOR YA QUE LLEVABA TIEMPO SIN PROGRAMAR Y MENOS EN PYTHON
#def show(self):
#    print(self.fila, " y ", self.columna)
#C=Variable(1,3,'vertical')
#C.show()