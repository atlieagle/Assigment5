max_int = 0

# Fæ input frá notanda
num_int = int(input("Input a number: "))    # Do not change this line

# Keyri while loopu á meðan input frá notanda er ekki neikvæð tala
while num_int >= 0:
    num_new = num_int

    # Ef ný tala er stærri en fyrri stærri tala
    if num_new > max_int:
        max_int = num_new

    # Prenta út stærstu tölu
    print("The maximum is", max_int)    # Do not change this line

    # Fæ input frá notanda
    num_int = int(input("Input a number: "))    # Do not change this line
