class frase:
    def reversa(self):
        txt = input ("Ingresa Una Frase o Lo Que Sea :  ")
        txtt = txt[::-1]

        print ('La Frase Original Es: ' + txt)
        print('La Frase Al Revez Es: ' + txtt)

plint = frase()
plint.reversa()
