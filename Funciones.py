
def llenar(arreglo):
    x = 0
    for f in range (10):
        for c in range (10):
            x = x + 1
            if len(str(x))<2:
                arreglo[f][c]='0'+str(x)
            else:
                arreglo[f][c] = str(x)

def mostrar(arreglo):
    for f in range (10):
        fila = ''
        for c in range (10):
            fila = fila+' | '+str(arreglo[f][c])
        print(fila)

def comprar(arreglo, num_ubicacion):
    x = 0
    for f in range (10):
        for c in range(10):
            x = x + 1
            if str(x) == str(num_ubicacion):
                arreglo[f][c]='XX'

def comprobarUbicacion(arreglo, num_ubicacion):
    x = 0
    for f in range(10):
        for c in range (10):
            x = x + 1
            if str(x) == str(num_ubicacion):
                if arreglo[f][c]=='XX':
                    return False
    return True