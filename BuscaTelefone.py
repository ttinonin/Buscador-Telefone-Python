import pyperclip, re


#re.VERBOSE nos permite usar comentários dentro do objeto
buscaNumero = re.compile(r'''(
    (\d{2})        #ddd
    (\s)           #espaço
    (\d{5})        #primeiros digitos
    (\s|-|\.)      #separador
    (\d{4})
    )''', re.VERBOSE)

#copia o texto da area de transferencia
texto = str(pyperclip.paste())

#escreve os números em um arquivo separado
with open('Desktop/scripts/lista.txt', 'w') as f:
    for groups in buscaNumero.findall(texto):
        f.write(f"Número encontrado: {groups[0]}\n")
