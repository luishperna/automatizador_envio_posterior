from tkinter import Frame, Tk, Label, Button, Entry, messagebox, END
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, mm
from datetime import datetime


# Salva as opções do usuário incremantadas nas listas
qtd_bornes = lista_bornes_de_passagem = []
qtd_capacitor = lista_capacitor_cilindrico = []
qtd_gavetas = lista_gavetas = []
qtd_inversor = lista_inversor_de_frequencia = []
qtd_mca = lista_modulos_mca = []
qtd_soft = lista_soft_starter = []
qtd_switch = lista_switch_gerenciavel = []
qtd_tampa_traseira = lista_tampa_traseira = []
qtd_tampa_lateral = lista_tampa_lateral = []


# Função pega a opção do usuário e trabalha nas condições incrementando nas listas
def input_usuario(evento=None):
    try:
        numero = int(escolha.get())
        valor = quantidade.get()
        escolha.delete(0, END)
        quantidade.delete(0, END)

        if (numero == 1) and (valor == ''):
            lista_bornes_de_passagem.append(1)

        elif (numero == 1) and (int(valor) >= 0):
            lista_bornes_de_passagem.append(int(valor))

        if (numero == 2) and (valor == ''):
            lista_capacitor_cilindrico.append(1)

        elif (numero == 2) and (int(valor) >= 0):
            lista_capacitor_cilindrico.append(int(valor))

        if (numero == 3) and (valor == ''):
            lista_gavetas.append(1)

        elif (numero == 3) and (int(valor) >= 0):
            lista_gavetas.append(int(valor))

        if (numero == 4) and (valor == ''):
            lista_inversor_de_frequencia.append(1)

        elif (numero == 4) and (int(valor) >= 0):
            lista_inversor_de_frequencia.append(int(valor))

        if (numero == 5) and (valor == ''):
            lista_modulos_mca.append(1)

        elif (numero == 5) and (int(valor) >= 0):
            lista_modulos_mca.append(int(valor))

        if (numero == 6) and (valor == ''):
            lista_soft_starter.append(1)

        elif (numero == 6) and (int(valor) >= 0):
            lista_soft_starter.append(int(valor))

        if (numero == 7) and (valor == ''):
            lista_switch_gerenciavel.append(1)

        elif (numero == 7) and (int(valor) >= 0):
            lista_switch_gerenciavel.append(int(valor))

        if (numero == 8) and (valor == ''):
            lista_tampa_traseira.append(1)

        elif (numero == 8) and (int(valor) >= 0):
            lista_tampa_traseira.append(int(valor))

        if (numero == 9) and (valor == ''):
            lista_tampa_lateral.append(1)

        elif (numero == 9) and (int(valor) >= 0):
            lista_tampa_lateral.append(int(valor))

        elif numero >= 10:
            messagebox.showerror(
                "ERRO: Número não cadastrado", "O número que você digitou não está nas opções mostradas.\nFavor digitar apenas o número correspondente ao item!")

    except (ValueError):
        messagebox.showerror("ERRO: Número não detectado",
                             "Favor digitar um número das opções!")


# Função para gerar um arquivo em .pdf
def gerar_pdf():
    try:
        dados_tabela = [
            ["Item", "Descrição", "Qtd"],
            ["1", "Bornes de passagem", str(sum(qtd_bornes))],
            ["2", "Capacitor cilíndrico", str(sum(qtd_capacitor))],
            ["3", "Gaveta", str(sum(qtd_gavetas))],
            ["4", "Inversor de frequência", str(sum(qtd_inversor))],
            ["5", "Módulo MCA", str(sum(qtd_mca))],
            ["6", "Soft-starter", str(sum(qtd_soft))],
            ["7", "Switch gerenciável", str(sum(qtd_switch))],
            ["8", "Tampa traseira", str(sum(qtd_tampa_traseira))],
            ["9", "Tampa lateral", str(sum(qtd_tampa_lateral))],
        ]

        # Pegando a o pro9jeto digitado para incrementar no arquivo .pdf
        projeto_escolhido = str(definir_projeto.get()).upper()
        texto_projeto_escolhido = (f'Projeto: {projeto_escolhido}')

        # Pegando a data e a hora atual para incrementar no arquivo .pdf
        data_e_hora_atuais = datetime.now()
        data_e_hora_em_texto = data_e_hora_atuais.strftime(
            'Relatório emitido em %d/%m/%Y às %H:%M')

        # Estilos para os parágrafos
        titulo_style = ParagraphStyle('Heading1', fontName='Helvetica-Bold',
                                      fontSize=14, textColor=colors.black, leading=20, alignment=1, spaceAfter=30)

        paragrafo_projeto_style = ParagraphStyle('Heading2', fontName='Helvetica',
                                                 fontSize=12, textColor=colors.black, leading=20, alignment=1, spaceAfter=30)

        paragrafo_style = ParagraphStyle('Heading3', fontName='Helvetica',
                                         fontSize=12, textColor=colors.black, leading=20, alignment=1, spaceAfter=15)

        paragrafo_informacoes_style = ParagraphStyle('Heading4', fontName='Helvetica',
                                                     fontSize=12, textColor=colors.black, leading=20, alignment=1, spaceBefore=242)

        paragrafo_final_style = ParagraphStyle('Heading5', fontName='Helvetica',
                                               fontSize=8, textColor=colors.black, leading=20, alignment=1)

        # Parágrafos do pdf
        titulo = Paragraph(
            'Relatório - Relação de Envio Posterior', titulo_style)

        paragrafo_texto_projeto_escolhido = Paragraph(
            texto_projeto_escolhido, paragrafo_projeto_style)

        paragrafo = Paragraph(
            'Segue abaixo a relação dos itens para envio posterior:', paragrafo_style)

        paragrafo_informacoes = Paragraph(
            data_e_hora_em_texto, paragrafo_informacoes_style)

        paragrafo_final = Paragraph(
            'Automatizador - Relação de Envio Posterior developed by Luís Henrique Perna © 2022', paragrafo_final_style)

        # Tabela do pdf já com estilização
        tabela = Table(dados_tabela, [12*mm, 50*mm, 12*mm], 10*[10*mm])
        tabela.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('ALIGN', (1, 1), (1, -1), 'LEFT'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, None),
            ('BACKGROUND', (0, 0), (-1, 0), colors.green),
            ('BACKGROUND', (0, 2), (-1, 2), colors.gainsboro),
            ('BACKGROUND', (0, 4), (-1, 4), colors.gainsboro),
            ('BACKGROUND', (0, 6), (-1, 6), colors.gainsboro),
            ('BACKGROUND', (0, 8), (-1, 8), colors.gainsboro),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white)
        ]))

        # Cria o arquivo .pdf e construí a página
        doc = SimpleDocTemplate("Relatório - Relação de Envio Posterior.pdf", pagesize=A4,
                                rightMargin=10*mm, leftMargin=10*mm, topMargin=20*mm)

        doc.build([titulo, paragrafo_texto_projeto_escolhido, paragrafo, tabela,
                  paragrafo_informacoes, paragrafo_final])

        # Alteração nos Label de confirmação ao usuário
        texto_confirmacao_emitido.config(text="Relatório emitido com sucesso!")

        texto_retirar_na_pasta.config(
            text="Para pegá-lo favor acessar a pasta do programa")

    except (PermissionError):
        messagebox.showerror("ERRO: PDF Aberto",
                             "Favor fechar o relatório em pdf aberto para emitir o novo!")


# Opções exibidas da interface
opcoes = ["Bornes de passagem",
          "Capacitor cilíndrico",
          "Gaveta",
          "Inversor de frequência",
          "Módulo MCA",
          "Soft-starter",
          "Switch gerenciável",
          "Tampa traseira",
          "Tampa lateral"]


# Cria a interface
home = Tk()
home.title('Automatizador - Relação de Envio Posterior v1.0')
home.resizable(width=0, height=0)
home.configure(bg="#F8F8FF")


# Cria um frame na interface
frame_item_e_quantidade = Frame(home)
frame_item_e_quantidade.configure(bg="#2c2c2c")
frame_item_e_quantidade.grid(column=0, row=16, pady=10, ipady=3)


# Texto inicial do programa
texto_inicial = Label(home, text='Automatizador de Relação de Envio Posterior')
texto_inicial.configure(bg="#111111")
texto_inicial.configure(fg="#DCDCDC")
texto_inicial["font"] = ("Verdana", "12", "bold")
texto_inicial.grid(column=0, row=0, ipady=10, sticky='ew')


espacamento_inicial = Label(home, text='')
espacamento_inicial.configure(bg="#F8F8FF")
espacamento_inicial.grid(column=0, row=1, pady=3)


# Exibe texto para o usuário definir o projeto
texto_definicao_projeto = Label(
    home, text='Informe o projeto nos campos abaixo:')
texto_definicao_projeto.configure(bg="#F8F8FF")
texto_definicao_projeto["font"] = ("Verdana", "11", "bold")
texto_definicao_projeto.grid(column=0, row=2)


# Exibe exemplo de projeto ao usuário
texto_definicao_projeto = Label(
    home, text='Exemplo: SE-12 CCM12122')
texto_definicao_projeto.configure(bg="#F8F8FF")
texto_definicao_projeto["font"] = ("Verdana", "10", "italic")
texto_definicao_projeto.grid(column=0, row=3)


# Cria input para o usuário definir o projeto
definir_projeto = Entry(home, width=30)
definir_projeto.configure(bg="#F5FFFA")
definir_projeto.grid(column=0, row=4)


# Exibe texto informativo
texto_orientacao = Label(
    home, text='Digite o número de uma das opções abaixo por vez no campo:')
texto_orientacao.configure(bg="#F8F8FF")
texto_orientacao["font"] = ("Verdana", "11", "bold")
texto_orientacao.grid(column=0, row=5, padx=100, pady=30)


# Trabalhando com a lista opcoes = [] na interface
for item in opcoes:
    index_e_item = f'{opcoes.index(item) + 1} - {item}'
    textos_opcoes = Label(home, text=index_e_item)
    textos_opcoes.configure(bg="#F8F8FF")
    textos_opcoes["font"] = ("Verdana", "10")
    textos_opcoes.grid(column=0, row=(opcoes.index(item) + 6))


espacamento = Label(home, text='')
espacamento.configure(bg="#F8F8FF")
espacamento.grid(column=0, row=15)


# Texto informe o item (dentro do frame)
texto_escolha = Label(frame_item_e_quantidade, text='Informe o item:')
texto_escolha.configure(bg="#2c2c2c")
texto_escolha.configure(fg="#F8F8FF")
texto_escolha["font"] = ("Verdana", "8", "bold")
texto_escolha.grid(column=0, row=0, padx=10)


# Cria input para o usuário escolher uma opção (dentro do frame)
escolha = Entry(frame_item_e_quantidade, width=20)
escolha.configure(bg="#F5FFFA")
escolha.grid(column=0, row=1, padx=10)


# Texto quantidade (dentro do frame)
texto_quantidade = Label(frame_item_e_quantidade, text='Quantidade:')
texto_quantidade.configure(bg="#2c2c2c")
texto_quantidade.configure(fg="#F8F8FF")
texto_quantidade["font"] = ("Verdana", "8", "bold")
texto_quantidade.grid(column=1, row=0, padx=10)


# Cria input para o usuário digitar a quantidade (dentro do frame)
quantidade = Entry(frame_item_e_quantidade, width=20)
quantidade.configure(bg="#F5FFFA")
quantidade.grid(column=1, row=1, padx=10)


# Botão executa a função input_usuario()
botao_input = Button(home, text='Enviar opção', command=input_usuario)
botao_input.configure(bg="#2c2c2c")
botao_input.configure(fg="#DCDCDC")
botao_input["font"] = ("Verdana", "10", "bold")
botao_input.grid(column=0, row=17, ipadx=8)


# Exibe texto informativo
texto_emitir = Label(
    home, text='Para emitir o relátorio clique em EMITIR PDF')
texto_emitir.configure(bg="#F8F8FF")
texto_emitir["font"] = ("Verdana", "10")
texto_emitir.grid(column=0, row=18, pady=25)


# Confirmação visual ao usuário da emissão do pdf
texto_confirmacao_emitido = Label(home, text='')
texto_confirmacao_emitido.configure(bg="#F8F8FF")
texto_confirmacao_emitido["font"] = ("Verdana", "9", "italic")
texto_confirmacao_emitido.grid(column=0, row=19)


# Confirmação visual ao usuário da emissão do pdf
texto_retirar_na_pasta = Label(home, text='')
texto_retirar_na_pasta.configure(bg="#F8F8FF")
texto_retirar_na_pasta["font"] = ("Verdana", "9", "italic")
texto_retirar_na_pasta.grid(column=0, row=20)


# Botão executa a função gerar_pdf()
botao_emitir = Button(home, text='EMITIR PDF', command=gerar_pdf)
botao_emitir.configure(bg="#111111")
botao_emitir.configure(fg="#DCDCDC")
botao_emitir["font"] = ("Verdana", "10", "bold")
botao_emitir.grid(column=0, row=21, ipadx=14)


espacamento2 = Label(home, text='')
espacamento2.configure(bg="#F8F8FF")
espacamento2.grid(column=0, row=22, pady=6)


# Citando o desenvolvedor
texto_credito = Label(
    home, text='Automatizador - Relação de Envio Posterior developed by Luís Henrique Perna © 2022')
texto_credito.configure(bg="#111111")
texto_credito.configure(fg="#DCDCDC")
texto_credito["font"] = ("Verdana", "8")
texto_credito.grid(column=0, row=23, sticky='ew')


# Ao apertar Enter executa a função input_usuario()
home.bind('<Return>', input_usuario)


# Mantém a interface aberta (loop)
home.mainloop()
