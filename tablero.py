from variable import * # Importa la clase Variable

# Representa el crucigrama: medidas y matriz correspondiente a las celdas
class Tablero:    
    def __init__(self, FILS, COLS):
        self.ancho=COLS
        self.alto=FILS    
        self.tablero=[]
        
        for i in range(self.alto):
            self.tablero.append([])
            for j in range(self.ancho):
                self.tablero[i].append('-')
                 
        
    def __str__(self):
        salida=""
        for f in range(self.alto):            
            for c in range(self.ancho):
                salida += self.tablero[f][c]                
            salida += "\n"
        return salida
       
    def reset(self):
        for f in range(self.alto):
            for c in range(self.ancho):
                self.tablero[f][c]='-'        
       
    def getAncho(self):
        return self.ancho
    
    def getAlto(self):
        return self.alto
    
    def getCelda(self, fila, col):
        return self.tablero[fila][col]
    
    def setCelda(self, fila, col, val):
        self.tablero[fila][col]=val    
    
    #FUNCIÓN PARA SABER SI ESTA OCUPADA
    def Ocupada(self, fila, col):
        return self.tablero[fila][col] != '-'
    
    def contador_variables(self):
        variables = []
        for fila in range(self.alto): #FILAS
            for col in range(self.ancho): #COLUMNAS
                # busco variables horizontales
                if self.Ocupada(fila, col) == False and (col == 0 or self.Ocupada(fila, col-1)):
                    longitud = 0
                    while col+longitud < self.ancho and self.Ocupada(fila, col+longitud) == False:
                        longitud += 1
                    if longitud > 1:
                        variables.append(Variable("", fila, col, "horizontal", longitud))
                # busco variables verticales
                if self.Ocupada(fila, col) == False and (fila == 0 or self.Ocupada(fila-1, col)):
                    longitud = 0
                    while fila+longitud < self.alto and self.Ocupada(fila+longitud, col) == False:
                        longitud += 1
                    if longitud > 1:
                        variables.append(Variable("", fila, col, "vertical", longitud))
        return variables
    
