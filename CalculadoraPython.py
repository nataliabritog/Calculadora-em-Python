#importando tkinter
#Tkinter é uma biblioteca padrão do Python usada para criar interfaces gráficas de usuário
from tkinter import *
from tkinter import ttk

cor1='#303030'# preta
cor2='#4f4f4f'#cinza
cor3='#1c1c1c'#preto mais escuro
cor4='#ffffff'#branca


janela =Tk()
janela.title("Calculadora")
janela.geometry("236x310")


frame_tela =Frame(janela,width=235,height=50,bg=cor1)
frame_tela.grid(row= 0,column=0)

frame_corpo =Frame(janela,width=235,height=268,bg=cor1)
frame_corpo.grid(row= 1,column=0)

#criando função
todos_valores=''

def entrar_valores(e):
    global todos_valores

    todos_valores = todos_valores + str(e)
    
    
    #passando valor para tela 
    valor_texto.set(todos_valores)

#função pra calcular
def calcular():
    global todos_valores
    resultado = eval (todos_valores)
    valor_texto.set(str(resultado))

#função de limpar tela
def limpar_tela():
    global todos_valores
    todos_valores=""
    valor_texto.set("")


#criando label resultado
valor_texto= StringVar()

app_label =Label(frame_tela,textvariable=valor_texto,width=16,height=2,padx=7,relief=FLAT,anchor="e", justify=RIGHT,font=('Ivy 18 '),bg=cor1,fg=cor4)
app_label.place(x=0,y=0)


#criando botões
b_1 =Button (frame_corpo,command=limpar_tela, text="C",width=11,height=2,bg=cor2,fg=cor4,font=('Ivy 13 bold'),relief=RAISED,overrelief='ridge')
b_1.place(x=0 ,y=0)
b_2 =Button (frame_corpo,command=lambda:entrar_valores('%'), text="%",width=5,height=2,bg=cor2,fg=cor4,font=('Ivy 13 bold'),relief=RAISED,overrelief='ridge')
b_2.place(x=118 ,y=0)
b_3 =Button (frame_corpo, command=lambda:entrar_valores('/'),text="/",width=5,height=2,bg=cor2,fg=cor4,font=('Ivy 13 bold'),relief=RAISED,overrelief='ridge')
b_3.place(x=177,y=0)
#2 linha
b_4 =Button (frame_corpo, command=lambda:entrar_valores('7'),text="7",width=5,height=2,bg=cor2,fg=cor4,font=('Ivy 13 bold'),relief=RAISED,overrelief='ridge')
b_4.place(x=0 ,y=52)
b_5 =Button (frame_corpo, command=lambda:entrar_valores('8'),text="8",width=5,height=2,bg=cor2,fg=cor4,font=('Ivy 13 bold'),relief=RAISED,overrelief='ridge')
b_5.place(x=59,y=52)
b_6 =Button (frame_corpo, command=lambda:entrar_valores('9'),text="9",width=5,height=2,bg=cor2,fg=cor4,font=('Ivy 13 bold'),relief=RAISED,overrelief='ridge')
b_6.place(x=118,y=52)
b_7 =Button (frame_corpo, command=lambda:entrar_valores('*'),text="*",width=5,height=2,bg=cor2,fg=cor4,font=('Ivy 13 bold'),relief=RAISED,overrelief='ridge')
b_7.place(x=177,y=52)
#3 linha
b_8=Button (frame_corpo, command=lambda:entrar_valores('4'),text="4",width=5,height=2,bg=cor2,fg=cor4,font=('Ivy 13 bold'),relief=RAISED,overrelief='ridge')
b_8.place(x=0 ,y=104)
b_9 =Button (frame_corpo, command=lambda:entrar_valores('5'),text="5",width=5,height=2,bg=cor2,fg=cor4,font=('Ivy 13 bold'),relief=RAISED,overrelief='ridge')
b_9.place(x=59,y=104)
b_10 =Button (frame_corpo, command=lambda:entrar_valores('6'),text="6",width=5,height=2,bg=cor2,fg=cor4,font=('Ivy 13 bold'),relief=RAISED,overrelief='ridge')
b_10.place(x=118,y=104)
b_11=Button (frame_corpo, command=lambda:entrar_valores('-'),text="-",width=5,height=2,bg=cor2,fg=cor4,font=('Ivy 13 bold'),relief=RAISED,overrelief='ridge')
b_11.place(x=177,y=104)
#4 linha
b_12=Button (frame_corpo, command=lambda:entrar_valores('1'),text="1",width=5,height=2,bg=cor2,fg=cor4,font=('Ivy 13 bold'),relief=RAISED,overrelief='ridge')
b_12.place(x=0 ,y=156)
b_13=Button (frame_corpo, command=lambda:entrar_valores('2'),text="2",width=5,height=2,bg=cor2,fg=cor4,font=('Ivy 13 bold'),relief=RAISED,overrelief='ridge')
b_13.place(x=59,y=156)
b_14=Button (frame_corpo, command=lambda:entrar_valores('3'),text="3",width=5,height=2,bg=cor2,fg=cor4,font=('Ivy 13 bold'),relief=RAISED,overrelief='ridge')
b_14.place(x=118,y=156)
b_15=Button (frame_corpo, command=lambda:entrar_valores('+'),text="+",width=5,height=2,bg=cor2,fg=cor4,font=('Ivy 13 bold'),relief=RAISED,overrelief='ridge')
b_15.place(x=177,y=156)
#5 linha
b_16 =Button (frame_corpo, command=lambda:entrar_valores('0'),text="0",width=11,height=2,bg=cor2,fg=cor4,font=('Ivy 13 bold'),relief=RAISED,overrelief='ridge')
b_16.place(x=0 ,y=208)
b_17=Button (frame_corpo, command=lambda:entrar_valores(','),text=",",width=5,height=2,bg=cor2,fg=cor4,font=('Ivy 13 bold'),relief=RAISED,overrelief='ridge')
b_17.place(x=118 ,y=208)
b_18=Button (frame_corpo, command=calcular,text="=",width=5,height=2,bg=cor2,fg=cor4,font=('Ivy 13 bold'),relief=RAISED,overrelief='ridge')
b_18.place(x=177,y=208)






janela.mainloop()
