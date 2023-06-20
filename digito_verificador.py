rut_sin_dv = input("Ingrese el RUT sin el dígito verificador: ")
rut_reverso = rut_sin_dv[::-1]
serie = [2, 3, 4, 5, 6, 7]
total = 0

for i in range(len(rut_reverso)):
    num = rut_reverso[i]
    total += int(num) * serie[i % len(serie)]

resto = total % 11

if resto == 0:
    digito_verificador = 0
elif resto == 10:
    digito_verificador = "K"
else:
    digito_verificador = 11 - resto

print("El dígito verificador es:", digito_verificador)
print("Tu rut es: {}-{}".format(rut_sin_dv, digito_verificador))
