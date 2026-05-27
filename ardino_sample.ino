const int PIN_UP = 8;
const int PIN_DOWN = 10;

void releaseAll() {
  pinMode(PIN_UP, INPUT);    // ハイインピーダンス = 未接続
  pinMode(PIN_DOWN, INPUT);  // ハイインピーダンス = 未接続
}

void connectGndTo8() {
  releaseAll();
  digitalWrite(PIN_UP, LOW);
  pinMode(PIN_UP, OUTPUT);   // D8をGNDへ落とす
}

void connectGndTo10() {
  releaseAll();
  digitalWrite(PIN_DOWN, LOW);
  pinMode(PIN_DOWN, OUTPUT); // D10をGNDへ落とす
}

void setup() {
  Serial.begin(9600);
  releaseAll();
  Serial.println("ready");
}

void loop() {
  if (!Serial.available()) return;

  String cmd = Serial.readStringUntil('\n');
  cmd.trim();

  if (cmd == "up") {
    connectGndTo8();
    Serial.println("GND -> 8");
  } else if (cmd == "down") {
    connectGndTo10();
    Serial.println("GND -> 10");
  } else if (cmd == "stop") {
    releaseAll();
    Serial.println("release");
  } else {
    Serial.println("unknown");
  }
}
