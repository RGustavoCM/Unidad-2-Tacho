class login:
    def todo(self):
        def askUser():
            username = input("Ingresa Tu Usuario: ")
            password = input("Ingresa Tu Contrasenia: ")
            checkPass(username, password)
        def checkPass(use, pwd):
            if use == "utng" and pwd == "mexico":
                login(use)
            else:
                print ("AlV Morro No Lo Quiero Ver Mas Aqui!!")
                askUser()
        def login(use):
            print("Bienvenido")
            
            print (" BBBBBBBBBBBBBBBBB     iiii                                                                                                   iiii              d::::::d             ")
            print (" B::::::::::::::::B   i::::i                                                                                                 i::::i             d::::::d                 ")
            print (" B::::::BBBBBB:::::B   iiii                                                                                                   iiii              d::::::d                 ")
            print (" BB:::::B     B:::::B                                                                                                                           d:::::d                  ")
            print ("   B::::B     B:::::Biiiiiii     eeeeeeeeeeee    nnnn  nnnnnnnn vvvvvvv           vvvvvvv eeeeeeeeeeee    nnnn  nnnnnnnn    iiiiiii     ddddddddd:::::d    ooooooooooo   ")
            print ("   B::::B     B:::::Bi:::::i   ee::::::::::::ee  n:::nn::::::::nnv:::::v         v:::::vee::::::::::::ee  n:::nn::::::::nn  i:::::i   dd::::::::::::::d  oo:::::::::::oo ")
            print ("   B::::BBBBBB:::::B  i::::i  e::::::eeeee:::::een::::::::::::::nnv:::::v       v:::::ve::::::eeeee:::::een::::::::::::::nn  i::::i  d::::::::::::::::d o:::::::::::::::o")
            print ("   B:::::::::::::BB   i::::i e::::::e     e:::::enn:::::::::::::::nv:::::v     v:::::ve::::::e     e:::::enn:::::::::::::::n i::::i d:::::::ddddd:::::d o:::::ooooo:::::o")
            print ("   B::::BBBBBB:::::B  i::::i e:::::::eeeee::::::e  n:::::nnnn:::::n v:::::v   v:::::v e:::::::eeeee::::::e  n:::::nnnn:::::n i::::i d::::::d    d:::::d o::::o     o::::o")
            print ("   B::::B     B:::::B i::::i e:::::::::::::::::e   n::::n    n::::n  v:::::v v:::::v  e:::::::::::::::::e   n::::n    n::::n i::::i d:::::d     d:::::d o::::o     o::::o")
            print ("   B::::B     B:::::B i::::i e::::::eeeeeeeeeee    n::::n    n::::n   v:::::v:::::v   e::::::eeeeeeeeeee    n::::n    n::::n i::::i d:::::d     d:::::d o::::o     o::::o")
            print ("   B::::B     B:::::B i::::i e:::::::e             n::::n    n::::n    v:::::::::v    e:::::::e             n::::n    n::::n i::::i d:::::d     d:::::d o::::o     o::::o")
            print (" BB:::::BBBBBB::::::Bi::::::ie::::::::e            n::::n    n::::n     v:::::::v     e::::::::e            n::::n    n::::ni::::::id::::::ddddd::::::ddo:::::ooooo:::::o")
            print (" B:::::::::::::::::B i::::::i e::::::::eeeeeeee    n::::n    n::::n      v:::::v       e::::::::eeeeeeee    n::::n    n::::ni::::::i d:::::::::::::::::do:::::::::::::::o")
            print (" B::::::::::::::::B  i::::::i  ee:::::::::::::e    n::::n    n::::n       v:::v         ee:::::::::::::e    n::::n    n::::ni::::::i  d:::::::::ddd::::d oo:::::::::::oo ")
            print (" BBBBBBBBBBBBBBBBB   iiiiiiii    eeeeeeeeeeeeee    nnnnnn    nnnnnn        vvv            eeeeeeeeeeeeee    nnnnnn    nnnnnniiiiiiii   ddddddddd   ddddd   ooooooooooo   ")
            print ("Haz Ingresado Los Datos Correctos!")
            askCom()
        def askCom():
            command = input("Ingresa Un Commando: ")
            if command == "salir" or command == "q":
                username = ""
                password = ""
                print ("Haz Cerrado La Sesion")
                askUser()
            else:
                print ("Commando Desconocido")
                askCom()
        askUser()

logear = login()
logear.todo()
