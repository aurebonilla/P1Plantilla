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
    
    #Para saber si la celda está ocupada
    def Ocupada(self, fila, col):
        return self.tablero[fila][col] != '-'
    
    #Contador de número y longitud de varibales
    def contador_variables(self):
        variables = {}
        num_variable = 1
        
        # Para contar las variables en dirección horizontal
        for fila in range(self.getAlto()):
            col = 0
            while col < self.getAncho():
                if self.Ocupada(fila, col):
                    col += 1
                else:
                    longitud = 0
                    while col+longitud < self.getAncho() and not self.Ocupada(fila, col+longitud):
                        longitud += 1
                    if longitud > 1:
                        nombre = f"Horizontal {num_variable}"
                        variables[nombre] = {"fila": fila, "columna": col, "direccion": "horizontal", "longitud": longitud}
                        num_variable += 1
                    col += longitud

        # Para contar las variables en dirección vertical
        for col in range(self.getAncho()):
            fila = 0
            while fila < self.getAlto():
                if self.Ocupada(fila, col):
                    fila += 1
                else:
                    longitud = 0
                    while fila+longitud < self.getAlto() and not self.Ocupada(fila+longitud, col):
                        longitud += 1
                    if longitud > 1:
                        nombre = f"Vertical {num_variable}"
                        variables[nombre] = {"fila": fila, "columna": col, "direccion": "vertical", "longitud": longitud}
                        num_variable += 1
                    fila += longitud

        # Para imprimir la información de las variables encontradas
        for nombre, variable in variables.items():
            print(f"{nombre}: longitud={variable['longitud']}, dirección={variable['direccion']}")
        
        return variables

