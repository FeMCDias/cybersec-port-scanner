import socket
from tkinter import *
from tkinter import messagebox
import threading

well_known_ports = {
    20: "FTP Data",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3389: "RDP",
}

def scan_ports(host, port_range):
    open_ports = []
    for port in range(port_range[0], port_range[1] + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                service = well_known_ports.get(port, "Unknown Service")
                open_ports.append((port, service))
            sock.close()
        except Exception as e:
            print(f"Erro ao conectar na porta {port}: {e}")
    return open_ports

def start_scan():
    host = entry_host.get()
    try:
        port_start = int(entry_port_start.get())
        port_end = int(entry_port_end.get())
        result_text.delete(1.0, END)
        result_text.insert(END, f"Escaneando {host} de {port_start} a {port_end}...\n")
        threading.Thread(target=execute_scan, args=(host, port_start, port_end)).start()
    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor, insira números válidos para as portas.")

def execute_scan(host, port_start, port_end):
    ports = scan_ports(host, (port_start, port_end))
    result_text.delete(1.0, END)
    for port, service in ports:
        result_text.insert(END, f"Porta {port}: {service}\n")
    if not ports:
        result_text.insert(END, "Nenhuma porta aberta encontrada.\n")

# Prepara a interface gráfica
app = Tk()
app.title("Port Scanner")

# Campo para o Host
label_host = Label(app, text="Host:")
label_host.grid(row=0, column=0)
entry_host = Entry(app)
entry_host.grid(row=0, column=1)

# Campos para o intervalo de portas
label_port_start = Label(app, text="Porta Inicial:")
label_port_start.grid(row=1, column=0)
entry_port_start = Entry(app)
entry_port_start.grid(row=1, column=1)

label_port_end = Label(app, text="Porta Final:")
label_port_end.grid(row=2, column=0)
entry_port_end = Entry(app)
entry_port_end.grid(row=2, column=1)

# Botão para iniciar o escaneamento
button_scan = Button(app, text="Escanear", command=start_scan)
button_scan.grid(row=3, column=0, columnspan=2)

# Área de texto para os resultados
result_text = Text(app, height=15, width=50)
result_text.grid(row=4, column=0, columnspan=2)

app.mainloop()