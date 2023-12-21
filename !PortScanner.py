#importa la libreria socket
import socket

def scan_ports(target_host, start_port, end_port):
    # Lista per memorizzare le informazioni sullo stato delle porte
    port_info = []

    # Ciclo attraverso i numeri di porta nel range specificato
    for port in range(start_port, end_port + 1):
        # Crea un oggetto socket per la connessione TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Imposta un timeout per la connessione
        sock.settimeout(1)

        # Tentativo di connessione alla porta specificata sull'host
        result = sock.connect_ex((target_host, port))

        # Memorizza l'informazione sullo stato della porta
        port_info.append({
            'port': port,
            'state': 'open' if result == 0 else 'closed'
        })

        # Chiude il socket dopo la connessione o il timeout
        sock.close()

    # Restituisce la lista delle informazioni sullo stato delle porte
    return port_info

def main():
    # Chiede all'utente di inserire l'indirizzo IP del server
    target_host = input("Inserisci l'indirizzo IP del server: ")

    # Chiede all'utente di inserire la porta di partenza della scansione
    start_port = int(input("Inserisci la porta di partenza della scansione: "))

    # Chiede all'utente di inserire la porta di fine della scansione
    end_port = int(input("Inserisci la porta di fine della scansione: "))

    # Stampa a schermo la scansione in corso dalla porta x alla porta y
    print(f"\nScansione in corso su {target_host} da porta {start_port} a {end_port}...\n")

    # Chiama la funzione di scansione e memorizza i risultati in port_info
    port_info = scan_ports(target_host, start_port, end_port)

    # Stampa informazioni sullo stato delle porte
    if port_info:
        print("Porte aperte:")
        for port in port_info:
            try:
                service_name = socket.getservbyport(port['port'])
            except OSError:
                service_name = "Servizio sconosciuto"

            print(f"Porta {port['port']} ({port['state']}): {service_name}")
    else:
        print("Nessuna porta aperta trovata.")

if __name__ == "__main__":
    main()
