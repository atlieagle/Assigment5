# Fæ input frá notanda um lengd sequence
n = int(input("Enter the length of the sequence: ")) # Do not change this line

# For loopa keyrð jafn oft og notandi sló inn
for i in range(1,n+1):
    # Fyrstu þrjár tölurnar prentaðar út strax
    if i == 1:
        svar = 1
        first_num = svar
    elif i == 2:
        svar = 2
        second_num = svar
    elif i == 3:
        svar = 3
        third_num = svar
    # Ef hlaupabreyta ef stærri en fyrsta tala
    elif i > first_num:
        # Þá leggjum við saman fyrri þrjár tölurnar á undan
        svar = first_num + second_num + third_num
        # Shiftum svo núverandi 3 svörum í breytur
        first_num = second_num
        second_num = third_num
        third_num = svar
    # Prenta út svar
    print(svar)