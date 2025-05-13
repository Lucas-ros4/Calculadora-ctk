import customtkinter as  ctk

#Configuracao de aparencia
ctk.set_appearance_mode('dark')

#Criação da janela principal
app = ctk.CTk() 
app.geometry('300x400')
app.title('CalculadoraCTK')
app.resizable(False, False) #para não poder redimensionar a janela

#variavel global para poder usar os numeros digitados em todas as funções
expressao = ""


def atualizar_display(n):
    global expressao
    expressao += str(n) #concatena todos os valores digitados
    label_resultado.configure(text=expressao)

def limpar_display():
    global expressao
    expressao = "0"
    label_resultado.configure(text=expressao)

def calcular():
    global expressao
    try:
        resultado = str(eval(expressao))   #eval() avalia a string como uma expressao e interpreta como uma expressao matematica(consegue detectar precedencia tbm)
        label_resultado.configure(text=resultado)
        expressao = resultado
    except:  #caso a função não consiga realizar o calculo cai aqui
        label_resultado.configure(text="Erro")
        expressao = "0"

def apagar_ultimo():
    global expressao
    expressao = expressao[:-1] #apaga o ultimo numero
    if expressao == '0':
        label_resultado.configure(text='0')
    else:
        label_resultado.configure(text=expressao)



label_resultado = ctk.CTkLabel( #display 
    app,
    text='0', 
    font=("Arial", 26),
    width=295,
    height=50,
    fg_color=('white', 'gray25'),
    anchor="e" #faz o texto ficar na direita do label

)
label_resultado.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")




#primeira linha de botoes
bC = ctk.CTkButton(app, text='C', width=50, height=50, command=lambda: limpar_display(), fg_color="red")
bPorcentagem = ctk.CTkButton(app, text='%', width=50, height=50, command=lambda: atualizar_display('%'), fg_color="#F18F01", text_color="black")
bDividir = ctk.CTkButton(app, text='/', width=50, height=50, command=lambda: atualizar_display('/'), fg_color="#F18F01", text_color="black")
bMulti = ctk.CTkButton(app, text='*', width=50, height=50, command=lambda: atualizar_display('*'), fg_color="#F18F01", text_color="black")

#segunda linha de botoes
b7 = ctk.CTkButton(app, text='7', width=50, height=50, command=lambda: atualizar_display('7'), fg_color="#3E454A")
b8 = ctk.CTkButton(app, text='8', width=50, height=50, command=lambda: atualizar_display('8'), fg_color="#3E454A")
b9 = ctk.CTkButton(app, text='9', width=50, height=50, command=lambda: atualizar_display('9'), fg_color="#3E454A")
bMenos = ctk.CTkButton(app, text='-', width=50, height=50, command=lambda: atualizar_display('-'), fg_color="#F18F01", text_color="black")

#terceira linha de botoes
b4 = ctk.CTkButton(app, text='4', width=50, height=50, command=lambda: atualizar_display('4'), fg_color="#3E454A")
b5 = ctk.CTkButton(app, text='5', width=50, height=50, command=lambda: atualizar_display('5'), fg_color="#3E454A")
b6 = ctk.CTkButton(app, text='6', width=50, height=50, command=lambda: atualizar_display('6'), fg_color="#3E454A")
bMais = ctk.CTkButton(app, text='+', width=50, height=50, command=lambda: atualizar_display('+'), fg_color="#F18F01", text_color="black")

#quarta linha de botoes
b1 = ctk.CTkButton(app, text='1', width=50, height=50, command=lambda: atualizar_display('1'), fg_color="#3E454A")
b2 = ctk.CTkButton(app, text='2', width=50, height=50, command=lambda: atualizar_display('2'), fg_color="#3E454A")
b3 = ctk.CTkButton(app, text='3', width=50, height=50, command=lambda: atualizar_display('3'), fg_color="#3E454A")
bIgual = ctk.CTkButton(app, text='=', width=50, height=50, command=lambda: calcular(), fg_color="green")

#quinta linha de botões
b0 = ctk.CTkButton(app, text='0', width=100, height=50, command=lambda: atualizar_display('0'), fg_color="#3E454A")
bPonto = ctk.CTkButton(app, text='.', width=50, height=50, command=lambda: atualizar_display('.'), fg_color="#3E454A")
bApagar = ctk.CTkButton(app, text='Apagar', height=50, width=50, command=lambda: apagar_ultimo(), fg_color="#F18F01", text_color="black")

#posicionamento dos botões usando grid(linha 1, colunas 0 a 3)
bC.grid(row=1, column=0, padx=5, pady=5, sticky="nsew") #sticky="nsew" faz o botão preencer o espaço da céluca
bPorcentagem.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
bDividir.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
bMulti.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")

#posicionamento dos botões usando grid(linha 2, colunas 0 a 3)
b7.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
b8.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
b9.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
bMenos.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

#posicionamento dos botões usando grid(linha 3, colunas 0 a 3)
b4.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
b5.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
b6.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
bMais.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")

#posicionamento dos botões usando grid(linha 4, colunas 0 a 3)
b1.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
b2.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
b3.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")
bIgual.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

#posicionamento dos botöes usando grid(linha 5, colucas 1 a 3)
b0.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
bPonto.grid(row=5, column=2, padx = 5, pady=5, sticky="nsew")
bApagar.grid(row=5, column=3, padx=5, pady=5, sticky="nsew")

#centralizar os botões na janela
app.grid_columnconfigure((0, 1, 2, 3), weight=1)
#iniciar a aplicação
app.mainloop()