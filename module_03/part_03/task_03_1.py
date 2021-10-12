mass = [5, 6, 901, 91, 1, 0, 66, 661, 2, 8]

res_ch = ""

mass_str = [str(el) for el in mass]
mass_str = sorted(mass_str, reverse = True)

res_ch = res_ch.join(mass_str)

print(res_ch)
