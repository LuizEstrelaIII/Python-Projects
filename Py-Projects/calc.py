from tkinter import *


root = Tk()
root.title("calculator")
root.geometry('408x355')
root.minsize(408,355)
root.maxsize(408,355)

numero1 = ''

divisao = False
multiplica = False
adicao = False
subtracao = False



root.configure(background='#282828')

e= Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#FFFFFF', bg='#a7a28f', font=('futura', 25, 'bold'), justify=CENTER)
e.grid(row= 0, column=0, columnspan=4, pady=2)

#funções operadores
def botao_click(num):
    e.insert(END, num)
def botao_divisao():
    global numero1
    global divisao
    divisao = True
    e.get()
    e.delete(0, END)
def botao_multiplica():
    global numero1
    global multiplica
    multiplica= True
    e.get()
    e.delete(0, END)
def botao_subtracao():
    global numero1
    global subtracao
    subtracao = True
    e.get()
    e.delete(0, END)
def botao_adicao():
    global numero1
    global adicao
    adicao = True
    e.get()
    e.delete(0, END)
def botao_limpar():
    e.delete(0, END)
def botao_igual():
    global subtracao
    global adicao
    global multiplica
    global divisao
    
    numero1 = e.get()
    numero2 = e.get()
    e.delete(0, END)
    if adicao == True:
        e.insert(0, int(numero1) + int(numero2))
        adicao = False

    if multiplica == True:
        e.insert(0, int(numero1) * int(numero2))
        multiplica = False

    if subtracao == True:
        e.insert(0, int(numero1) - int(numero2))
        subtracao = False

    if divisao == True:
        e.insert(0, int(numero1) / int(numero2))
        divisao = False

#1° fileira:
divide = Button(root, text= '÷', padx=52, pady=20, command= botao_divisao, fg= '#FFFFFF' , bg='#320064', relief=FLAT, font=('futura', 12, 'bold'))
divide.grid(row=0, column=4, )


um = Button(root, text = '1' , padx=40, pady=20,command=lambda: botao_click(1), fg='#FFFFFF', bg = '#320064', relief = FLAT, font=('futura', 12, 'bold') )
um.grid(row = 1, column=1)


dois = Button(root, text = '2' , padx=40, pady=20,command=lambda: botao_click(2), fg='#FFFFFF', bg = '#320064', relief = FLAT, font=('futura', 12, 'bold') )
dois.grid(row = 1, column=2)


tres = Button(root, text = '3' , padx=40, pady=20,command=lambda: botao_click(3), fg='#FFFFFF', bg = '#320064', relief = FLAT, font=('futura', 12, 'bold') )
tres.grid(row = 1, column=3)


multiplica = Button(root, text = 'x' , padx=52, pady=20,command=botao_multiplica, fg='#FFFFFF', bg = '#320064', relief = FLAT, font=('futura', 12, 'bold') )
multiplica.grid(row = 1, column=4)

#2° fileira:
quatro = Button(root, text = '4' , padx=40, pady=20,command=lambda: botao_click(4), fg='#FFFFFF', bg = '#320064', relief = FLAT, font=('futura', 12, 'bold') )
quatro.grid(row = 2, column=1)

cinco = Button(root, text = '5' , padx=40, pady=20,command=lambda: botao_click(5), fg='#FFFFFF', bg = '#320064', relief = FLAT, font=('futura', 12, 'bold') )
cinco.grid(row = 2, column=2)

seis = Button(root, text = '6' , padx=40, pady=20,command=lambda: botao_click(6), fg='#FFFFFF', bg = '#320064', relief = FLAT, font=('futura', 12, 'bold') )
seis.grid(row = 2, column=3)

menos = Button(root, text = '--' , padx=52, pady=20,command=botao_subtracao, fg='#FFFFFF', bg = '#320064', relief = FLAT, font=('futura', 12, 'bold') )
menos.grid(row = 2, column=4)

#3° fileira:
sete = Button(root, text = '7' , padx=40, pady=20,command=lambda: botao_click(7), fg='#FFFFFF', bg = '#320064', relief = FLAT, font=('futura', 12, 'bold') )
sete.grid(row = 3, column=1)

oito = Button(root, text = '8' , padx=40, pady=20,command=lambda: botao_click(8), fg='#FFFFFF', bg = '#320064', relief = FLAT, font=('futura', 12, 'bold') )
oito.grid(row = 3, column=2)

nove = Button(root, text = '9' , padx=40, pady=20,command=lambda: botao_click(9), fg='#FFFFFF', bg = '#320064', relief = FLAT, font=('futura', 12, 'bold') )
nove.grid(row = 3, column=3)

mais = Button(root, text = '+' , padx=52, pady=20,command=botao_adicao, fg='#FFFFFF', bg = '#320064', relief = FLAT, font=('futura', 12, 'bold') )
mais.grid(row = 3, column=4)

#4° fileira:
zero = Button(root, text = '0' , padx=91, pady=20,command=lambda: botao_click(0), fg='#FFFFFF', bg = '#320064', relief = FLAT, font=('futura', 12, 'bold') )
zero.grid(row = 4, column=1, columnspan=2)

limpar = Button(root, text = 'c' , padx=40, pady=20,command=botao_limpar, fg='#FFFFFF', bg = '#320064', relief = FLAT, font=('futura', 12, 'bold') )
limpar.grid(row = 4, column=3)

igual = Button(root, text = '=' , padx=52, pady=20,command=botao_igual, fg='#FFFFFF', bg = '#320064', relief = FLAT, font=('futura', 12, 'bold') )
igual.grid(row = 4, column=4)

root.mainloop()