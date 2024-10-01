import os
import sys
import socket
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from threading import Thread, Event
import os


def get_base_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    base_ip = '.'.join(ip.split('.')[:-1]) + '.'
    return base_ip


def send_file_to_server(file_path, server_ip, server_port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((server_ip, server_port))
            with open(file_path, 'rb') as file:
                while chunk := file.read(4096):
                    sock.sendall(chunk)
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return False
    return True


def scan_network_for_servers(port, ip_entry_widget, stop_event, status_label, scan_button):
    base_ip = get_base_ip()
    status_label.config(text="Scanning network...")
    for i in range(1, 255):
        if stop_event.is_set():
            break
        ip = f"{base_ip}{i}"
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            try:
                sock.connect((ip, port))
                ip_entry_widget.delete(0, tk.END)
                ip_entry_widget.insert(0, ip)
                status_label.config(text=f"PS5 found at {ip}")
                messagebox.showinfo("PS5 Found", f"PS5 found at {ip}")
                scan_button.config(state=tk.NORMAL)
                return
            except:
                continue
    status_label.config(text="Scan complete: No PS5 found")
    scan_button.config(state=tk.NORMAL)
    messagebox.showerror("Scan Complete", "No PS5 found")


def start_transfer():
    server_ip = ip_entry.get()
    if not server_ip:
        messagebox.showerror("Input Error", "Please enter PS5 IP")
        return

    selected_file = file_combobox.get()
    if selected_file == "Other":
        file_path = filedialog.askopenfilename()
    else:
        file_path = os.path.join(jar_folder, selected_file)

    if not file_path:
        return

    success = send_file_to_server(file_path, server_ip, 9025)
    if success:
        messagebox.showinfo("Success", "Payload sent successfully")
    else:
        messagebox.showerror("Error", "Failed to send payload")


def start_scan():
    scan_button.config(state=tk.DISABLED)
    stop_event.clear()
    scan_thread = Thread(target=scan_network_for_servers, args=(9025, ip_entry, stop_event, status_label, scan_button),
                         daemon=True)
    scan_thread.start()


def scan_jar_files(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    jar_files = [f for f in os.listdir(folder) if f.endswith('.jar')]
    jar_files.append("Select Manually")
    return jar_files


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)



root = tk.Tk()
root.title("PS5 Payload Injector - StatikkRaccoon")


icon_path = resource_path("icon.png")
icon_image = tk.PhotoImage(file=icon_path)
root.iconphoto(False, icon_image)

style = ttk.Style()
style.configure("TFrame", padding=10)
style.configure("TLabel", padding=5)
style.configure("TButton", padding=5, relief="flat")
style.configure("TCombobox", padding=5)

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill="x", expand=True)

ip_label = ttk.Label(frame, text="PS5 IP:")
ip_label.grid(row=0, column=0, sticky="e")

ip_entry = ttk.Entry(frame, width=30)
ip_entry.grid(row=0, column=1, pady=5, padx=5, sticky="ew")

file_label = ttk.Label(frame, text="Select Payload:")
file_label.grid(row=1, column=0, sticky="e")

jar_folder = "payloads"
jar_files = scan_jar_files(jar_folder)

file_combobox = ttk.Combobox(frame, values=jar_files, state="readonly")
file_combobox.set("Select Manually")
file_combobox.grid(row=1, column=1, pady=5, padx=5, sticky="ew")

button_frame = ttk.Frame(frame)
button_frame.grid(row=2, columnspan=2, pady=10, padx=5)

scan_button = ttk.Button(button_frame, text="Scan Network", command=start_scan)
scan_button.pack(side="left", padx=5)

send_button = ttk.Button(button_frame, text="Send Payload", command=start_transfer)
send_button.pack(side="right", padx=5)

status_label = ttk.Label(frame, text="")
status_label.grid(row=3, columnspan=2, pady=5, padx=5, sticky="ew")

stop_event = Event()

frame.columnconfigure(1, weight=1)
frame.rowconfigure(4, weight=1)

root.mainloop()