from tkinter import Tk, Label, Button, Entry, END
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, mm


# Salvar as opções do usuario incremantadas nas listas
qtd_bornes = lista_bornes_de_passagem = []
qtd_capacitor = lista_capacitor_cilindrico = []
qtd_disjuntor = lista_disjuntor = []
qtd_fusivel = lista_fusivel = []
qtd_gavetas = lista_gavetas = []
qtd_inversor = lista_inversor_de_frequencia = []
qtd_mca = lista_modulos_mca = []
qtd_soft = lista_soft_starter = []
qtd_switch = lista_switch_gerenciavel = []
qtd_tampa_traseira = lista_tampa_traseira = []
qtd_tampa_lateral = lista_tampa_lateral = []


# Função pega a opção do usuario e trabalha nas condições incrementando nas listas
def input_usuario(evento=None):
    numero = int(escolha.get())
    escolha.delete(0, END)

    if numero == 1:
        lista_bornes_de_passagem.append(1)
        quantidade = sum(qtd_bornes)
        print(
            f'Você escolheu => Bornes de passagem\nA quantidade atual => {quantidade}')

    elif numero == 2:
        lista_capacitor_cilindrico.append(1)
        quantidade = sum(lista_capacitor_cilindrico)
        print(
            f'Você escolheu => Capacitor cilíndrico\nA quantidade atual => {quantidade}')

    elif numero == 3:
        lista_disjuntor.append(1)
        quantidade = sum(lista_disjuntor)
        print(
            f'Você escolheu => Disjuntor\nA quantidade atual => {quantidade}')

    elif numero == 4:
        lista_fusivel.append(1)
        quantidade = sum(lista_fusivel)
        print(
            f'Você escolheu => Fusível\nA quantidade atual => {quantidade}')

    elif numero == 5:
        lista_gavetas.append(1)
        quantidade = sum(lista_gavetas)
        print(
            f'Você escolheu => Gavetas\nA quantidade atual => {quantidade}')

    elif numero == 6:
        lista_inversor_de_frequencia.append(1)
        quantidade = sum(lista_inversor_de_frequencia)
        print(
            f'Você escolheu => Inversor de frequência\nA quantidade atual => {quantidade}')

    elif numero == 7:
        lista_modulos_mca.append(1)
        quantidade = sum(lista_modulos_mca)
        print(
            f'Você escolheu => Modulos MCA\nA quantidade atual => {quantidade}')

    elif numero == 8:
        lista_soft_starter.append(1)
        quantidade = sum(lista_soft_starter)
        print(
            f'Você escolheu => Soft-starter\nA quantidade atual => {quantidade}')

    elif numero == 9:
        lista_switch_gerenciavel.append(1)
        quantidade = sum(lista_switch_gerenciavel)
        print(
            f'Você escolheu => Switch gerenciavel\nA quantidade atual => {quantidade}')

    elif numero == 10:
        lista_tampa_traseira.append(1)
        quantidade = sum(lista_tampa_traseira)
        print(
            f'Você escolheu => Tampa traseira\nA quantidade atual => {quantidade}')

    elif numero == 11:
        lista_tampa_lateral.append(1)
        quantidade = sum(lista_tampa_lateral)
        print(
            f'Você escolheu => Tampa lateral\nA quantidade atual => {quantidade}')

    else:
        print('ERRO: Esse valor não está cadastrado, favor digitar novamente')


# Função para gerar um arquivo em pdf
def gerar_pdf():
    dados_tabela = [
        ["Item", "Descrição", "Qtd"],
        ["1", "Bornes de passagem", str(sum(qtd_bornes))],
        ["2", "Capacitor cilíndrico", str(sum(qtd_capacitor))],
        ["3", "Disjuntor", str(sum(qtd_disjuntor))],
        ["4", "Fusivel", str(sum(qtd_fusivel))],
        ["5", "Gavetas", str(sum(qtd_gavetas))],
        ["6", "Inversor de frequencia", str(sum(qtd_inversor))],
        ["7", "Modulos mca", str(sum(qtd_mca))],
        ["8", "Soft-starter", str(sum(qtd_soft))],
        ["9", "Switch gerenciavel", str(sum(qtd_switch))],
        ["10", "Tampa traseira", str(sum(qtd_tampa_traseira))],
        ["11", "Tampa lateral", str(sum(qtd_tampa_lateral))],
    ]

    # Estilos para os paragrafos
    titulo_style = ParagraphStyle('Heading1', fontName='Helvetica-Bold',
                                  fontSize=20, textColor=colors.black, leading=20, alignment=1, spaceAfter=30)

    paragrafo_style = ParagraphStyle('Heading2', fontName='Helvetica',
                                     fontSize=14, textColor=colors.black, leading=20, alignment=1, spaceAfter=15)

    # Paragrafos do pdf
    titulo = Paragraph('Relatório - Relação de Envio Posterior', titulo_style)
    paragrago1 = Paragraph(
        'Segue abaixo relação de itens:', paragrafo_style)

    # Tabela do pdf já com estilização
    tabela = Table(dados_tabela, [12*mm, 50*mm, 12*mm], 12*[10*mm])
    tabela.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ALIGN', (1, 1), (1, -1), 'LEFT'),
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, None),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')
    ]))

    # Cria o arquivo .pdf e construi a pagina
    doc = SimpleDocTemplate("Relatório - Relação de Envio Posterior.pdf", pagesize=A4,
                            rightMargin=10*mm, leftMargin=10*mm, topMargin=20*mm, bottonMargin=10*mm)

    doc.build([titulo, paragrago1, tabela])


# Apenas para exibição na interface
opcoes = ["Bornes de passagem",
          "Capacitor cilíndrico",
          "Disjuntor",
          "Fusivel",
          "Gavetas",
          "Inversor de frequencia",
          "Modulos mca",
          "Soft-starter",
          "Switch gerenciavel",
          "Tampa traseira",
          "Tampa lateral"]


# Criando Interface
# home = Tk()
home = Tk()
home.title('Automatizador - Envio Posterior de Itens')


# Exibe texto informativo
texto_orientacao = Label(home, text='Escolha uma das opções abaixo:')
texto_orientacao.grid(column=0, row=0, padx=200, pady=20)


# Trabalhando com a lista opcoes na interface
for item in opcoes:
    index_e_item = f'{opcoes.index(item) + 1} - {item}'
    textos_opcoes = Label(home, text=index_e_item)
    textos_opcoes.grid(column=0, row=(opcoes.index(item) + 1))


espacamento = Label(home, text='')
espacamento.grid(column=0, row=13)


# Cria input para o usuario escolher uma opção
escolha = Entry(home, width=20)
escolha.grid(column=0, row=14)


# Botão executa a função input_usuario()
botao_input = Button(home, text='Enviar opção', command=input_usuario)
botao_input.grid(column=0, row=15)


# Exibe texto informativo
texto_emitir = Label(
    home, text='Para emitir o relátorio clique em EMITIR PDF')
texto_emitir.grid(column=0, row=16, pady=20)


# Botão executa a função gerar_relatorio() importado de gerador_pdf.py
botao_emitir = Button(home, text='EMITIR PDF', command=gerar_pdf)
botao_emitir.grid(column=0, row=18)

espacamento2 = Label(home, text='')
espacamento2.grid(column=0, row=19)


# Ao apertar Enter executa a função input_usuario()
home.bind('<Return>', input_usuario)


# Mantém a interface aberta (loop)
home.mainloop()
