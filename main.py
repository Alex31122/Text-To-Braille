# Diccionario de mapeo de letras a Braille
braille_dict = {
    'a': [['1', '0'],['0', '0'],['0', '0']],
    'b': [['1', '0'],['1', '0'],['0', '0']],
    'c': [['1', '1'],['0', '0'],['0', '0']],
    'a': [['1', '0'],['0', '0'],['0', '0']],
    'b': [['1', '0'],['1', '0'],['0', '0']],
    'c': [['1', '1'],['0', '0'],['0', '0']],
    'd': [['1', '1'],['0', '1'],['0', '0']],
    'e': [['1', '0'],['0', '1'],['0', '0']],
    'f': [['1', '1'],['1', '0'],['0', '0']],
    'g': [['1', '1'],['1', '1'],['0', '0']],
    'h': [['1', '0'],['1', '1'],['0', '0']],
    'i': [['0', '1'],['1', '0'],['0', '0']],
    'j': [['0', '1'],['1', '1'],['0', '0']],
    'k': [['1', '0'],['0', '0'],['1', '0']],
    'l': [['1', '0'],['1', '0'],['1', '0']],
    'm': [['1', '1'],['0', '0'],['1', '0']],
    'n': [['1', '1'],['0', '1'],['1', '0']],
    'o': [['1', '0'],['0', '1'],['1', '0']],
    'p': [['1', '1'],['1', '0'],['1', '0']],
    'q': [['1', '1'],['1', '1'],['1', '0']],
    'r': [['1', '0'],['1', '1'],['1', '0']],
    's': [['0', '1'],['1', '0'],['1', '0']],
    't': [['0', '1'],['1', '1'],['1', '0']],
    'u': [['1', '0'],['0', '0'],['1', '1']],
    'v': [['1', '0'],['1', '0'],['1', '1']],
    'w': [['0', '1'],['1', '1'],['0', '1']],
    'x': [['1', '1'],['0', '0'],['1', '1']],
    'y': [['1', '1'],['0', '1'],['1', '1']],
    'z': [['1', '0'],['0', '1'],['1', '1']],
    # Agrega más letras y caracteres aquí
}

def text_to_braille(text):
    braille_grid = []
    for char in text.lower():
        if char in braille_dict:
            braille_grid.append(braille_dict[char])
        else:
            braille_grid.append([[' '], [' '], [' ']])  # Mantener caracteres no mapeados como espacios en blanco
    return braille_grid

# Ejemplo de uso
texto_entrada = input("Ingrese el texto que desea traducir a Braille: ")
texto_braille = text_to_braille(texto_entrada)

# Imprime el texto en Braille como una cuadrícula
for i in range(3):
    for row in texto_braille:
        print(' '.join(row[i]), end='  ')
    print()
