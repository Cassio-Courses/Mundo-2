def desafio36():
    sal=float(input("Insira o salário\n"))
    casa=float(input("Insira o valor da casa\n"))
    anos=float(input("Insira quantos anos você pagará\n"))
    prestação=(casa/anos)/12
    cento=prestação/sal
    if cento>0.30:
        print("Você não pode comprar a casa pois a prestação ultrapassa 30% do seu salário")
    else:
        print("Seu emprestimo foi autorizado")
        print("O valor da sua prestação é: {}, representa {}% do seu salário".format(prestação,cento*100))
def desafio37():
    #binario octal hexadecimal
    x = int(input('Digite 1 para converter para Binário, 2 octal, 3 hexadecimal\n'))
    c = int(input("Digite o numero que deseja converter\n"))
    if x==1:
        bino = ((str(bin(c))))
        print("O numero convertido em binário é: {}".format(bino[2:]))
    elif x==2:
        octo = ((str(oct(c))))
        print("O numero convertido em octal é: {}".format(octo[2:]))
    elif x==3:
        hexo = ((str(hex(c))))
        print("O numero convertido em hexadecimal é: {}".format(hexo[2:]))
    else:
        print("Não foi escolhido nenhuma das opções acima")
def desafio38():
    x=input("Insira um valor")
    x2=input("insira um segundo valor")
    if x>x2:
        print("O Primeiro ({}), é maior que o segundo ({})".format(x,x2))
    elif x<x2:
        print("O segundo ({}), é maior que o primeiro({})".format(x2,x))
    else:
        print("Os dois são iguais, primeiro ({}), segundo ({})".format(x,x2))
def desafio39():
    from datetime import date
    x=int(input('Informe sua idade'))
    alistamento=18-x
    if alistamento<0:
        if alistamento==1:
            print("Passou-se o tempo do alistamento em {} ano".format(abs(alistamento)))
        else:
            print("Passou-se o tempo do alistamento em {} anos".format(abs(alistamento)))
    elif alistamento>0:
        if alistamento!=1:
            print("Você se alistará em {} anos".format(abs(alistamento)))
        else:
            print("Você se alistará em {} ano".format(abs(alistamento)))
    else:
        print("Você está no ano do alistamento")
def desafio48():
    a=0
    for c in range(1,501):
        if c%3==0:
            if c%2!=0:
                a+=c
                print(a,c)
    print ('fim {}'.format(a))
def desafio50():
    a=0
    for c in range(5):
        x=int(input("Insira o numero que deseja somar"))
        if x%2==0:
            a+=x
            print(a,x)
    print(a)
def desafio51():
    x=float(input('Insira o primeiro termo da PA'))
    r=float(input('Insira a razão da PA'))
    for c in range(10):
        x+=r
        print(x-r)
def desafio52():
    x=int(input("Insira o numero"))
    a=0
    if x==1:
        print("É numero primo")
    else:
        for c in range(1, x+1):
            if x%c==0:
                a+=c
        if a==x+1:
            print("É um numero primo")
        else:
            print("Não é numero primo")
def desafio53():
    x=input("Insira seu nome")
    a=len(x)
    nome=''
    for c in range(len(x)):
        a-=1
        nome+=x[a]
    if x.strip().lower()==nome.strip().lower():
        print("Sua frase é um palíndromo")
    else:
        print("não é palíndromo")
def desafio54():
    import datetime
    a=0; b=0
    for c in range(6):
        x=(datetime.date.today().year)-int(input('Qual seu ano de nascimento'))
        if x>= 18:
            a+=1
        else:
            b+=1
    print('{} pessoas atingiram maior idade'.format(a))
    print('{} pessoas ainda não atingiram maior idade'.format(b))
def desafio55():
    menor=10000
    maior=0
    for c in range(4):
        x=float(input("peso"))
        if x>maior:
            maior=x
        if x<menor:
            menor=x
    print(maior,menor)
def desafio56():
    
desafio56()
