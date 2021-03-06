
# ABRIMOS ARCHIVO, LO LEEMOS Y LO CONVERTIMOS A MINUSCULA
constitucion_file= open("D:/Descargas/BorradorNC.txt", encoding="utf-8", mode= "r")
constitucion_words = constitucion_file.read().lower()

# QUITAMOS CARACTERES NO DESEADOS
quitar_caracteres = ",;:.-()°º\n!\"'"
for caracter in quitar_caracteres:
    constitucion_words = constitucion_words.replace(caracter, " ")

# CONVERTIMOS EL TEXTO A LISTA DE PALABRAS
constitucion_words = constitucion_words.split(" ")

# CONTAMOS LA CANTIDAD DE VECES QUE SE REPITE UNA PALABRA
dic_frecuencia = {}

for palabra in constitucion_words:
    if palabra in dic_frecuencia:
        dic_frecuencia[palabra] += 1
    else:
        dic_frecuencia[palabra] = 1

# MOSTRAMOS LAS PALABRAS QUE SE REPITAN UN CANTIDAD X DE VECES -
# EXCEPTUAMOS LAS PALABRAS NO DESEADAS

quitar_palabras = ["la", "entre", "serán","más", "si", "éstas", "este", "éste", "ni", "artículo", "lo", 
                   "como", "ser", "al", "esta", "no", "es", "las", "los", "un", "que", "el", "por", "son",
                   "de", "a", "en", "para", "con", "se", "sus", "del", "y", "su", "una", "o", "e", "a1",
                   "u", "una", "así", "uno", "podrá" , "será" , "sobre", "sin" , "toda", "demás", ""]

dic_palabras = {}

for palabra in dic_frecuencia:
    frecuencia = dic_frecuencia[palabra]
    if palabra in quitar_palabras:
        continue
    if frecuencia > 50:
        dic_palabras[palabra] = frecuencia
        print (f"El término '{palabra}' se repite: {frecuencia} veces.\n")



# ORDENAR FRECUENCIA DE PALABRAS 
''' for palabra in sorted(dic_palabras.values()):
    frecuencia = dic_frecuencia[palabra]
    print(f"El término '{palabra}' se repite: {frecuencia} veces.") '''


constitucion_file.close()
