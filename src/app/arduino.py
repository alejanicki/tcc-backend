import serial
import time


def controlar_motor(sentido):
    # Abre a conexão com a porta serial do Arduino
    with serial.Serial('COM5', 9600, timeout=1) as ser:
        # Aguarda um breve momento antes de enviar o comando
        time.sleep(2)

        # Envia o comando para o Arduino com base no sentido
        if sentido == 'direita':
            ser.write(b'R')  # 'R' para girar para a direita
            print("Girando para a direita...")
        elif sentido == 'esquerda':
            ser.write(b'L')  # 'L' para girar para a esquerda
            print("Girando para a esquerda...")
        else:
            print("Sentido inválido. Use 'direita' ou 'esquerda'.")

        # Aguarda o Arduino concluir a rotação
        time.sleep(5)
