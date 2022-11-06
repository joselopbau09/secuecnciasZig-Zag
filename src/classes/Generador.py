
class Generador:
    def __init__(self,longitudSecuencia, numZigZag):
        self.secuencia = []
        self.generaSecuencia(longitudSecuencia, numZigZag)
    
    def generaSecuencia(self,longitudSecuencia, numZigZag):
        mitadSecuencia = longitudSecuencia // 2
        mitadSecuenciaAvanza = mitadSecuencia + 1 
        avanzaRetrocede = True
        elemtosAgergados = 0 

        for i in range(0, longitudSecuencia):
            if avanzaRetrocede:
                self.secuencia.append(mitadSecuenciaAvanza)
                mitadSecuenciaAvanza += 1
                elemtosAgergados += 1
                if(elemtosAgergados == numZigZag):
                    avanzaRetrocede = False
                    elemtosAgergados = 0
            else:
                self.secuencia.append(mitadSecuencia)
                mitadSecuencia -= 1 
                elemtosAgergados += 1
                if(elemtosAgergados == numZigZag):
                    avanzaRetrocede = True
                    elemtosAgergados = 0            

    def getSecuencia(self):
        return self.secuencia