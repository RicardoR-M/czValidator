class ErrorValidacion:
    def __init__(self, fila, col, cabecera, valor, msg):
        self.cabecera = cabecera
        self.fila = fila
        self.msg = msg
        self.col = col
        self.valor = valor
