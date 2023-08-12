#aula de introducao TKINTER

from tkinter import *

#inicialization window Tk
janela = Tk(screenName='Marcus')

#settings
janela.title('janela do Marcao')    #Adiciona titulo
janela.geometry("300x300")          #Define tamanho padrao
janela.resizable(False, False)      #Define tamanho FIXO

#Itens
legenda = Label(text='Legenda')     
legenda.grid(row = 0, column = 0, columnspan=4)

botao7 = Button(
    text='7',
    font=('Arial', 16),
    height=2,
    bg= '#F7FDA7',
    activebackground='#F7FDA7',
)
botao7.grid(row=1, column=0, sticky=EW)

botao8 = Button(
    text='8',
    font=('Arial', 16),
    height=2,
    bg= '#F7FDA7',
    activebackground='#F7FDA7',
)
botao8.grid(row=1, column=1, sticky=EW)

botao4 = Button(
    text='4',
    font=('Arial', 16),
    height=2,
    bg= '#F7FDA7',
    activebackground='#F7FDA7',
)
botao4.grid(row=2, column=0, sticky=EW)

botao5 = Button(
    text='5',
    font=('Arial', 16),
    height=2,
    bg= '#F7FDA7',
    activebackground='#F7FDA7',
)
botao5.grid(row=2, column=4, sticky=EW)

#runing window
janela.mainloop()