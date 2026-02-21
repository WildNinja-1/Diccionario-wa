meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "GG": "Una palabra diciendo victoria pero abrevivado, aveces escrito en forma minuscula.",
            "CREEPY ": "aterrador, siniestro.",
            "AGGRO": "ponerse agresivo/enojado",
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Esa palabra no esta en el diccionario.")
