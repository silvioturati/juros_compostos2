from mortgage import Loan

if __name__ == '__main__':
    emprestimo = float(input("Qual o valor do empréstimo: "))
    juros_anual = float(input("Qual a taxa de juros anual: "))
    prazo = int(input("Qual o prazo em anos: "))
    financiamento = Loan(emprestimo, (juros_anual / 100), prazo, currency=" ")  # calculo usando o mortgage

    print("\nCálculo usando o módulo Mortgage")
    print(financiamento.summarize)
