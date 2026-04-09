import re

while True:

    entrada = input("CPF: ")
    cpf = re.sub(r'[^0-9]', '', entrada)
    
    nove_digitos = cpf[:9] # 746824890
    cr = 10 # contagem regressiva
    r = 0 # resultado
    s = 0
    f = 0
    rf_1 = 0 # resultado final
    dc_1 = 0
    for i in nove_digitos:
        r = int(i) * cr
        cr -= 1
        s += r
    f = s * 10
    rf_1 = f % 11
    dc_1 = rf_1
    
    # Segundo Digito
    
    nove_digitos_2 = cpf[:10] # 7468248907
    cr_2 = 11
    r = 0
    s2 = 0
    f = 0
    rf_2 = 0
    dc_2 = 0
    for i in nove_digitos_2:
        r = int(i) * cr_2
        cr_2 -= 1
        s2 += r
    f = s2 * 10
    rf_2 = f % 11
    dc_2 = rf_2
    
    if rf_1 > 9:
        dc_1 = 0
    else:
        dc_1 = rf_1
    
    if rf_2 > 9:
        dc_2 = 0
    else:
        dc_2 = rf_2
    
    if (str(dc_1) == cpf[9]) and (str(dc_2) == cpf[10]):
        print('esse cpf é válido✅')
    else:
        print('esse cpf é inválido! ❌')
    
    a = input("Deseja continuar? ")
    if a.lower().startswith("s"):
        continue
    else:
        break
