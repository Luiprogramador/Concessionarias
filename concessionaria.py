from class_carro import Carro
from time import sleep
temp = 3
tam = 25


def entraDados():
    modelo = input("Digite o modelo do Carro: ")
    ano = int(input("Digite o ano do carro: "))
    valor = float(input("Digite o valor do carro: "))
    return modelo, ano, valor


if __name__ == '__main__':
    pintar = "\033[1;30;43m"
    terminarCor = "\033[m"
    modelo, ano, valor = entraDados()
    carro1 = Carro(modelo, ano, valor)
    modelo, ano, valor = entraDados()
    carro2 = Carro(modelo, ano, valor)
    carro1.concessionaria()
    trocarOCarro = input("Você quer trocar o carro? [s/n]\n")
    if trocarOCarro == "s":
        print(f"{'Troca de carros':^{tam}}")
        carro1.concessionaria()
        posi = int(input("Digite a posição do carro que você quer trocar: \n[começando do 0]\ndigite aqui: "))
        modelo, ano, valor = entraDados()
        carro1.trocaCarros(posi, modelo, ano, valor)
        carro1.concessionaria()
        print("-" * 50)
    print(f"{pintar}FINALIZANDO PROGRAMA.{terminarCor}")
    sleep(5)
    print("Agora sim.")
