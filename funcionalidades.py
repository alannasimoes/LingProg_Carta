from fpdf import FPDF
import os

def salvar_txt(data, destinatario, remetente,carta_formatada):
    nome_arq = data+'_'+destinatario+'_'+remetente+'.txt'
    arq = open(nome_arq, 'w')
    arq.write(carta_formatada)
    arq.close()
    return nome_arq

def salvar_pdf(nome_arq):
    txtPdf = FPDF()
    txtPdf.add_page()
    txtPdf.set_font('Arial', size=11)
    arq = open(nome_arq, 'r')
    linhas = arq.readlines()
    for linha in linhas:
        txtPdf.multi_cell(180, 10, linha)
    nome_arq = nome_arq[:-4]
    txtPdf.output(f'{nome_arq}.pdf')