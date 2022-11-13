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
    for i in range(1, len(secuencia)):
        temp = secuencia[i]
        j = i-1
        while (j >= 0 and temp < secuencia[j]) :
                secuencia[j + 1] = secuencia[j]
                j -= 1
        secuencia[j + 1] = temp
        
def localInsertionSort(secuencia):
    biList = DoublyLinkedList()
    biList.push(secuencia[0])
    pointer = biList.head

    for i in range(1, len(secuencia)):
        if (pointer.dato < secuencia[i]): 
            while (pointer.dato < secuencia[i]):
                if (pointer.next != None):
                    pointer = pointer.next
                else:
                    break    
            biList.agregarDespues(pointer, secuencia[i])
        else:
            while (pointer.dato > secuencia[i]):
                if (pointer.prev != None):
                    pointer = pointer.prev
                else:
                    break    
            if ( pointer.prev == None):
                biList.push(secuencia[i])
                pointer = biList.head
            else:        
                biList.agregarAntes(pointer, secuencia[i])   

    i = 0
    p = biList.peek()
    while(p != None):
        secuencia[i] = p.dato
        p = p.next
        i += 1

def main():
    longitudSecuencia = getInt('Ingresa la longitud de la secuencia: ', 'Ingresa un entero positivo!', 1, 2**1000)
    numZigZag = getInt('Ingresa el numero de Zig-Zag: ', f'Ingresa un número entre 1 y {longitudSecuencia // 2}', 1, longitudSecuencia // 2)    
    generador = Generador(longitudSecuencia, numZigZag)
    secuencia = generador.getSecuencia()

    secuenciaLocal = secuencia.copy()

    print(secuencia)
    localInsertionSort(secuenciaLocal)
    print(secuencia)

    insertionSort(secuencia)
main()

