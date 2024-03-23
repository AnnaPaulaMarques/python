def soma(a, b):
    return a + b
    
def sub(a, b):
    return a - b
    
def div(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    else:
        return a / b
    
def mult(a, b):
    return a * b
    
def listar():
    vantagens = [
        "Python é uma linguagem limpa",
        "Python tem uma comunidade ativa",
        "Python tem uma biblioteca extensa"
        ]
    for vantagens in vantagens:
        print(vantagens)

print("Olá!")

menu = int(input("Escolha uma opção de 1 a 5! Somar=1,  Subtrair=2 , Dividir=3 , Multiplicar=4 e Listar vantagens PYTHON=5"))

if menu < 5:
    a = float(input("Qual primeiro número?"))
    b = float(input("Qual segundo número?"))

if menu == 1:  
    print(soma(a, b))
elif menu == 2:
    print(sub(a, b))
elif menu == 3:
    print(div(a, b))
elif menu == 4:
    print(mult(a, b))
elif menu ==5:
    print("Vantagens do Python")
    listar()
else:
    print ("Opção inválida!")






