class Carro(object):
    carros = []
    def __init__(self, modelo, ano, valor):
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        carDic = {"modelo": self.modelo, "ano": self.ano,  "valor": self.valor}
        Carro.carros.append(carDic)

    def getModelo(self):
        return self.modelo
    def getAno(self):
        return self.ano
    def getValor(self):
        return self.valor

    def setModelo(self, novoModelo):
        self.modelo = novoModelo
    def setAno(self, novoAno):
        self.ano = novoAno
    def setValor(self,novoValor):
        if novoValor > 0:
            self.valor = novoValor

    def mostraDados(self, modelo, ano, valor):
        print('O modelo do carro é ', modelo)
        print('O ano do carro é ', ano )
        print('O valor do carro é ', valor)
    def retornaDados(self):
        return self.modelo, self.ano, self.valor

    def concessionaria(self, tam=25):
        tam = tam
        azul = '\033[4;30;44m'
        verde = '\033[4;30;42m'
        limpar = '\033[m'
        print("==== CONCESSIONÁRIA ====\n"
              f"{'veículos':^{tam}}")
        for pos, carro in enumerate(Carro.carros):
            if pos % 2 == 0:
                cor = azul
            else:
                cor = verde
            print(f'{cor}{pos:^{tam}}{limpar}')
            for chave, item in carro.items():
                #print(chave, ":",item)
                print(f'{cor}{f"{chave}: {item}":^{tam}}{limpar}')
            #print(carro)

    def trocaCarros(self, pos, modelo='', ano=0, valor=0):
        if modelo:
            Carro.carros[pos]['modelo'] = modelo
        if ano:
            Carro.carros[pos]['ano'] = ano
        if valor:
            Carro.carros[pos]['valor'] = valor

if __name__ == '__main__':
    carro1 = Carro("fiorino", 2020, 65_000)
    carro2 = Carro("mazda miata mx5", 1970, 300_000)
    #print(Carro.carros)
    carro1.concessionaria()
    carro1.trocaCarros(1, 'Mustang')
    carro1.concessionaria()