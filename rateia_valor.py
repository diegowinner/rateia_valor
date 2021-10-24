from tkinter import *

def rateia_valor():
    try:
        total = float(v_principal.get())
        valor_ratear = float(v_retear.get())
        quantidade = float(v_quantidade.get())
        valor_unitario = float(v_unitario.get())

        rateio = ((quantidade*valor_unitario)*100)/total
        valor_rateado = float((valor_ratear*rateio)/100)

        resultado["text"] = ('% Rateio ='+str(rateio)+'% e o valor é: R$ '+str(valor_rateado)).replace('.',',')
        #print('Percentual de Rateio = '+str(rateio)+'% Valor do reateio =: R$'+str(valor_rateado))
    except ValueError:
        resultado["text"] = 'O Valor Inserido é Inválido para o Cálculo.' '\nO separador decimal aceito é ponto(.)'

janela = Tk()
janela.title(":: Calcula Rateio de Valores :: ::V1.00::")
janela.geometry("800x600")
texto_orientacao_v_principal = Label(janela, text = 'Valor Total Principal')
texto_orientacao_v_principal.grid(column=0, row=0)
v_principal = Entry()
v_principal.grid(column=0, row=2)

texto_orientacao_v_retear = Label(janela, text = 'Valor a Ratear')
texto_orientacao_v_retear.grid(column=0, row=3)
v_retear = Entry()
v_retear.grid(column=0, row=4)

texto_orientacao_v_quantidade = Label(janela, text = 'Quantidade do Item')
texto_orientacao_v_quantidade.grid(column=0, row=5)
v_quantidade = Entry()
v_quantidade.grid(column=0, row=6)

texto_orientacao_v_unitario = Label(janela, text = 'Valor Unitário')
texto_orientacao_v_unitario.grid(column=0, row=7)
v_unitario = Entry()
v_unitario.grid(column=0, row=8)

resultado = Label(janela, text = '')
resultado.grid(column=5, row=10)

btn_calcular = Button(janela, text = 'Calcular', command=rateia_valor)
btn_calcular.grid(column=0, row=9)
janela.mainloop()

