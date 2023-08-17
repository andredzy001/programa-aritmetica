Nome = input ("Digite o nome do aluno: ")
BIM1 =float(input ("Digite a nota do Bimestre 1: "))
BIM2=float(input ("Digite a nota do Bimestre 2: "))
BIM3 = float(input ("Digite a nota do Bimestre 3: "))
BIM4= float(input ("Digite a nota do Bimestre 4: "))
MEDIA= ((BIM1+BIM2+BIM3+BIM4)/4)
print ("A média foi: ",MEDIA)
if MEDIA >= 9:
    print ("Aprovado com Louvor")
elif MEDIA >= 7:
     print ("Aprovado")
elif MEDIA <7:
     print ("Reprovado") 