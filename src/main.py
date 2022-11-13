from classes.DoublyLinkedList import DoublyLinkedList
from classes.Generador import Generador

def getInt(mensaje, error,min, max):
    while (True):
        print(mensaje)
        val = input()
        if val.isnumeric():
            if (int(val) < min or max < int(val)):
                print(error)
            else:
                return int(val)
        else:
            print(error)
def insertionSort(secuencia):
    operaciones = 0
    for i in range(1, len(secuencia)):
        temp = secuencia[i]
        operaciones += 1
        j = i-1
        operaciones += 1
        while (j >= 0 and temp < secuencia[j]) :
            operaciones += 1
            secuencia[j + 1] = secuencia[j]
            j -= 1
            operaciones += 1
        secuencia[j + 1] = temp
        operaciones += 1

    return operaciones
        
def localInsertionSort(secuencia):
    operaciones = 0
    biList = DoublyLinkedList()
    biList.push(secuencia[0])
    operaciones += 1

    pointer = biList.head
    operaciones += 1

    for i in range(1, len(secuencia)):
        if (pointer.dato < secuencia[i]): 
            while (pointer.dato < secuencia[i]):
                if (pointer.next != None):
                    pointer = pointer.next
                    operaciones += 1
                else:
                    break    
            biList.agregarDespues(pointer, secuencia[i])
            operaciones += 1
        else:
            while (pointer.dato > secuencia[i]):
                if (pointer.prev != None):
                    operaciones += 1
                    pointer = pointer.prev
                else:
                    break    
            if ( pointer.prev == None):
                biList.push(secuencia[i])
                operaciones += 1
                pointer = biList.head
                operaciones += 1
            else:        
                biList.agregarAntes(pointer, secuencia[i])   
                operaciones += 1

    i = 0
    p = biList.peek()
    operaciones += 1
    while(p != None):
        secuencia[i] = p.dato
        operaciones += 1
        p = p.next
        operaciones += 1
        i += 1
    return operaciones


def main():
    longitudSecuencia = getInt('Ingresa la longitud de la secuencia: ', 'Ingresa un entero positivo!', 1, 2**1000)
    numZigZag = getInt('Ingresa el numero de Zig-Zag: ', f'Ingresa un número entre 1 y {longitudSecuencia // 2}', 1, longitudSecuencia // 2)    
    generador = Generador(longitudSecuencia, numZigZag)
    secuencia = generador.getSecuencia()

    secuenciaLocal = secuencia.copy()

    print(f'La secuenia en {numZigZag}-zig-zag: {secuencia}')
    operacionesLocal = localInsertionSort(secuenciaLocal)
    operacionesInsertion = insertionSort(secuencia)
    print(f'Operaciones realizadas con Insertion Sort: {operacionesInsertion}')
    print(f'Operaciones realizadas con Local Insertion Sort: {operacionesLocal}')
    print(secuencia)
main()

