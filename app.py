def imcCalculo(peso,altura):
   imc = round (peso / (altura **2), 1)
   if imc <= 18.5:
      classificacao = "abaixo"
   elif imc >= 18.6 and imc <= 24.9:
      classificacao = "ideal"
   elif imc >= 25.0 and imc <= 29.9:
      classificacao = "sobrepeso"
   elif imc >= 30.0 and imc <= 34.9:
      classificacao = "obesidade 1"
   elif imc >= 35.0 and imc <= 39.9:
      classificacao = "obesidade 2"
   elif imc >= 40:
      classificacao = "obesidade 3"

   return classificacao
