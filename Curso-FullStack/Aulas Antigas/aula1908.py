#sites para cores

#https://encycolorpedia.pt/
#https://color.adobe.com/pt/create/color-wheel
#paletadecolores
from tkinter import ttk
#subistituindo as ferramentas navitas do Tkinter por ferramentas mais modernas
from tkinter import *
from tkinter.ttk import *

#criando janela
janela = Tk()
janela.title('Cadastro')
janela.resizable(False, False)
janela.geometry("1080x800")


#criar lista
dias_semana = [
    'Domingo',
    'Segunda',
    'Terca',
    'Quarta',
    'Quinta',
    'Sexta',
    'Sabado'
]

cursos_disponiveis = [
    'Programacao',
    'Design',
    'Art',
    'Film',
    'Marketing',
    'Fotografia'
]

mensagem = ttk.Label(janela, text='   Digite seu nome',background='green')
mensagem.pack(ipadx=10, ipady=10)

digite_nome = ttk.Entry(janela)
digite_nome.pack(padx=20, pady= 20)

idade = Label(text='Digite a data de nascimento')
idade.pack()

digite_idade = ttk.Entry(janela)
digite_idade.pack()

curso = Label(text="Escolha o curso")
curso.pack()
cursos = ttk.Combobox(janela, values=cursos_disponiveis)
cursos.pack()

combobox = ttk.Combobox(janela,values=dias_semana)
#posicionando o Combobox dentro do janela utilizando o pack
combobox.pack()






#render do conteudo, rodando a janela
janela.mainloop()

