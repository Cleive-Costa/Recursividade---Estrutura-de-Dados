def inverter_string(frase):
    if len(frase) == 0 or len(frase) == 1:
        return frase
    else:
        return frase[-1] + inverter_string(frase[:-1])

print(inverter_string("Vitamina B12"))