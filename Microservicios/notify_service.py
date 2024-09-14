import sys

def notify(message):
    print(f"Notificación: {message}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        message = sys.argv[1]
        notify(message)
    else:
        print("No se proporcionó ningún mensaje para notificar.")
