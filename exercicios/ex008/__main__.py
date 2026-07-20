from ex008 import ContaBancaria

def main():
    c1 = ContaBancaria(111, "Maria", 5_000)
    c1.depositar(1000)
    
    c1.titular = "Pedro" # Aqui ele cria outro e deixa o original intacto
    c1._titular = "Pedro" # Ele deixa, mas não mexa pois 'Adultos estão consentindo'...

    c1.__saldo = 0 # Aqui no privado ele não deixa criar
    c1._ContaBancaria__saldo = 0 # Aqui já muda

    print(c1)

if __name__ == '__main__':
    main()