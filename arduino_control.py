import serial
import serial.tools.list_ports
import time


BAUD_RATE = 9600


def find_arduino_port():
    ports = list(serial.tools.list_ports.comports())

    for port in ports:
        # Arduino UNO系はだいたい usbmodem
        if "usbmodem" in port.device:
            return port.device

    raise RuntimeError("Arduinoのポートが見つかりません。USB接続とBoard/Port設定を確認してください。")


def send_command(ser, command):
    ser.write((command + "\n").encode("utf-8"))
    ser.flush()

    # Arduinoから返答があれば読む
    time.sleep(0.1)
    while ser.in_waiting:
        line = ser.readline().decode("utf-8", errors="ignore").strip()
        if line:
            print("Arduino:", line)


def main():
    port = find_arduino_port()
    print(f"接続先: {port}")

    with serial.Serial(port, BAUD_RATE, timeout=1) as ser:
        # Arduino UNOはシリアル接続時にリセットされるので少し待つ
        time.sleep(2)

        print("ready")
        print("u: 上昇 / d: 下降 / s: 停止 / q: 終了")

        while True:
            key = input("> ").strip().lower()

            if key == "u":
                send_command(ser, "up")
            elif key == "d":
                send_command(ser, "down")
            elif key == "s":
                send_command(ser, "stop")
            elif key == "q":
                send_command(ser, "stop")
                print("終了")
                break
            else:
                print("u / d / s / q のどれかを入力")


if __name__ == "__main__":
    main()
