# Byrjunarreiturinn er 1.1 ef sett er inn "n" leggjum við 0.1 við 1.1(1.1 + 0.1 = 1.2) staðsetningin verður þá 1.2 og ef sett er
# inn "s" er það alveg eins nema við drögum frá 0.1. Ef sett er inn "e" leggjum við 1 við staðsetninguna(1.1 + 1 = 2.1) og eins ef
# sett er inn "w" nema þá er dregið frá. X- eða y-ás getur ekki orið hærra en 3(1.1 = x, y) það eru líka fleiri lokaðar áttir/leiðir
# sem þarf að passa. Ef staðsetningin verður 3.1 þá stoppar forritið. 

# https://github.com/aronhr/SC-T-111-PROG/tree/master/Verkefni%208

pos = 1.1
travel = "(N)orth."
no_print = True

while True:
    round_pos = round(pos, 1)

    if round_pos == 3.1:
        print("Victory!")
        break

    if round_pos == 1.1:
        travel = "(N)orth."
    elif round_pos == 1.2:
        travel = "(N)orth or (E)ast or (S)outh."
    elif round_pos == 2.2:
        travel = "(S)outh or (W)est."
    elif round_pos == 2.1:
        travel = "(N)orth."
    elif round_pos == 1.3:
        travel = "(E)ast or (S)outh."
    elif round_pos == 2.3:
        travel = "(E)ast or (W)est."
    elif round_pos == 3.3:
        travel = "(S)outh or (W)est."
    elif round_pos == 3.2:
        travel = "(N)orth or (S)outh."

    if no_print:
        print("You can travel:", travel)

    direction = input("Direction: ").lower()

    if direction == "n":
        if round_pos == 1.3 or round_pos == 2.3 or round_pos == 3.3 or round_pos == 2.2:
            print("Not a valid direction!")
            no_print = False
            continue
        pos += 0.1
        no_print = True
    elif direction == "s":
        if round_pos == 1.1 or round_pos == 2.1 or round_pos == 2.3 or round_pos == 3.1:
            print("Not a valid direction!")
            no_print = False
            continue
        pos -= 0.1
        no_print = True
    elif direction == "w":
        if round_pos == 1.1 or round_pos == 1.2 or round_pos == 2.1 or round_pos == 1.3 or round_pos == 3.2 or round_pos == 3.1:
            print("Not a valid direction!")
            no_print = False
            continue
        pos -= 1.0
        no_print = True
    elif direction == "e":
        if round_pos == 1.1 or round_pos == 2.2 or round_pos == 3.3 or round_pos == 3.2 or round_pos == 2.1 or round_pos == 3.1:
            print("Not a valid direction!")
            no_print = False
            continue
        pos += 1.0
        no_print = True
    else:
        print("Not a valid direction!")
        no_print = False
