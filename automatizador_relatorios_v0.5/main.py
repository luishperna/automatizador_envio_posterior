from gerador_pdf import gerar_relatorio
from tkinter import *


# Listas para salvar as opções do usuario
lista_bornes_de_passagem = []
lista_capacitor_cilindrico = []
lista_disjuntor = []
lista_fusivel = []
lista_gavetas = []
lista_inversor_de_frequencia = []
lista_modulos_mca = []
lista_soft_starter = []
lista_switch_gerenciavel = []
lista_tampa_traseira = []
lista_tampa_lateral = []


# Função pega a opção do usuario e trabalha nas condições incrementando nas listas
# ___Lembrete:___ Remover os prints das condições quando os dados estiverem no pdf
def input_usuario():
    numero = int(escolha.get())
    print(numero)  # Apenas para verificar o get nos testes
    escolha.delete(0, END)

    if numero == 0:
        print('Sair...')
        return

    elif numero == 1:
        lista_bornes_de_passagem.append(1)
        quantidade = sum(lista_bornes_de_passagem)
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


# Variavel para exibir na interface
opcoes = ["Sair",
          "Bornes de passagem",
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
home = Tk()
home.title('Automatizador - Envio Posterior de Itens')


# Exibe texto informativo
texto_orientacao = Label(home, text='Escolha uma das opções abaixo:')
texto_orientacao.grid(column=0, row=0, padx=200, pady=20)


# Trabalhando com a lista opcoes na interface
for item in opcoes:
    index_e_item = f'{opcoes.index(item)} - {item}'
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
botao_emitir = Button(home, text='EMITIR PDF', command=gerar_relatorio)
botao_emitir.grid(column=0, row=17)

espacamento2 = Label(home, text='')
espacamento2.grid(column=0, row=18)


# Mantém a interface aberta (loop)
home.mainloop()
