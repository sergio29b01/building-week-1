# Importa la libreria 'requests' per effettuare le varie richieste al server web
import requests

# Definisci una funzione 'scan_http_verbs' che effettua la scansione dei metodi HTTP su un determinato URL e porta
def scan_http_verbs(url, port):
    # Lista dei metodi HTTP da verificare
    verbs = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS']

    # Inizializza un dizionario per contenere i risultati delle scansioni dei vari metodi HTTP
    results = {}

    # Cicla attraverso i metodi HTTP
    for verb in verbs:
        try:
            # Esegue una richiesta HTTP per il metodo corrente sull'URL e la porta specificata
            response = requests.request(verb, f'http://{url}:{port}')
            
            # Verifica se la risposta ha un codice di stato inferiore a 400 (successo)
            has_handler = response.status_code < 400
            
            # Aggiunge il risultato al dizionario dei risultati, utilizzando il nome del metodo come chiave
            results[verb] = has_handler
        except requests.exceptions.RequestException as e:
            # Gestisce eventuali errori durante la richiesta e stampa un messaggio di errore
            print(f"Errore nella richiesta {verb}: {e}")
            
            # Se si verifica un errore, imposta il risultato per il metodo corrente su False
            results[verb] = False

    # Restituisce il dizionario dei risultati contenente la presenza o meno di handler per ciascun metodo HTTP
    return results

# Loop principale del programma
while True:
    # Richiedi all'utente di inserire l'IP
    url_to_scan = input('Inserisci un IP: ')
    
    # Richiedi all'utente di inserire la porta da scansionare
    custom_port = input('Inserisci la porta da scansionare: ')

    # Assicurati che l'input della porta sia un numero intero
    while True:
        try:
            custom_port = int(custom_port)
            break
        except ValueError:
            # Se l'input non è un numero intero, stampa un messaggio di errore e richiedi l'input della porta nuovamente
            print('La porta deve essere un numero intero. Riprova.')
            custom_port = input('Inserisci la porta da scansionare: ')

    # Stampa un'intestazione per la scansione sulla porta specificata
    print(f'\nScansione sulla porta {custom_port}:')

    # Esegui la scansione dei metodi HTTP sull'URL e la porta specificati utilizzando la funzione definita precedentemente
    scan_results = scan_http_verbs(url_to_scan, custom_port)

    # Stampa i risultati indicando se ciascun metodo è presente o meno
    for verb, has_handler in scan_results.items():
        print(f"{verb}: {'Metodo presente' if has_handler else 'Nessun metodo'}")

    # Richiedi all'utente se vuole eseguire un'altra scansione
    choice = input('\nVuoi scansionare un\'altra porta? (Sì/No): ').lower()
    
    # Se la scelta è diversa da "si", esce dal loop principale e termina il programma
    if choice != 'si':
        break
