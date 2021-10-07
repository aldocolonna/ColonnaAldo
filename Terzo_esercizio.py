x = 0
def voto(x):
    if x < 0 or x > 10:
        print("Il valore del voto deve essere compreso tra 1 e 10")
try:
    profili = {
        "luca@liceo.it":{
            "nome":"",
            "cognome":"",
            "italiano":"",
            "scienze":"",
            "inglese":""
        },
        "lucia@liceo.it":{
            "nome":"",
            "cognome":"",
            "italiano":"",
            "scienze":"",
            "inglese":""
        },
        "marco@liceo.it":{
            "nome":"",
            "cognome":"",
            "italiano":"",
            "scienze":"",
            "inglese":""
        },
        "maria@liceo.it":{
            "nome":"",
            "cognome":"",
            "italiano":"",
            "scienze":"",
            "inglese":""
        },
        "francesca@liceo.it":{
            "nome":"",
            "cognome":"",
            "italiano":"",
            "scienze":"",
            "inglese":""
        }
    }
    mail = ["luca@liceo.it","lucia@liceo.it","marco@liceo.it","maria@liceo.it","francesca@liceo.it"]
    try:
        for i in range(0,5):
            profili[mail[i]]["nome"]= input(str("inserire il nome dell'utente " + mail[i] + ":" + "\n"))
            profili[mail[i]]["cognome"]= input(str("inserire il cognome dell'utente " + mail[i] + ":" + "\n"))
            profili[mail[i]]["italiano"]= voto(int(input("inserire il voto di italiano dell'utente " + mail[i] + ":" + "\n")))
            profili[mail[i]]["scienze"]= voto(int(input("inserire il voto di scienze dell'utente " + mail[i] + ":" + "\n")))
            profili[mail[i]]["inglese"]= voto(int(input("inserire il voto di inglese dell'utente " + mail[i] + ":" + "\n")))
        utente = input(str("inserisci una mail: " + "\n" ))
        print(profili[utente])
    except ValueError:
        print("il voto deve essere un numero")
except KeyError:
    print("la mail non è registrata")
