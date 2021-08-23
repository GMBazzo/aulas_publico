class Soma:

    @staticmethod
    def soma(numeros):
        resultado = 0
        for numero in numeros:
            resultado = resultado + numero
        return resultado

numeros = [2, 5 ,7, 4, 6,]
resultado = Soma.soma(numeros)
print("Minha da idade atual é: "+ str(resultado))
