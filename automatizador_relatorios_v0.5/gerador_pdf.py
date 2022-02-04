# Lembrete:
#   - Incrementar mais informações e melhoria no visual
#   - Trazer os dados obtidos nas listas para o pdf
#   - Caso possivel, emitir tabela ou grafico dos itens no pdf


from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


# Função gera um relatorio em pdf
def gerar_relatorio():
    relatorio = canvas.Canvas('Relatorio de Analise.pdf', pagesize=A4)
    relatorio.drawString(
        165, 750, 'Relatório - Analise de Mateirais para Envio Posteior')
    relatorio.drawString(165, 700, 'Quantidades por item:')
    relatorio.save()
    print('Emitido com sucesso!')
