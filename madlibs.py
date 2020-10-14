def inputs():
    global noun
    global noun_prulal
    global Nouns
    global place
    global adjective
    global Noun

    print("""
    Please Enter the following : """)
    noun = input("noun: ")
    noun_prulal = input("noun (prulal): ")
    Noun = input("Noun: ")
    place = input("Place : ")
    adjective = input("Adjective : ")
    Nouns = input("Noun: ")


def phrase():
    print(f"""
    Be kind to your {Noun}-footed {noun_prulal}
    for a duck maybe somebody's {Noun}
    Be kind to your {Noun} in {place}
    Where the weather is always {adjective}
    You may think that this is the {Nouns}""")
inputs()
phrase()
