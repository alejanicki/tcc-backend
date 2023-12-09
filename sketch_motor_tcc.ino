// Define stepper motor connections and steps per revolution:
#define DIR_PIN 9
#define STEP_PIN 10
#define stepsPerRevolution 100

void setup() {
  // Declare pins as output:
  pinMode(DIR_PIN, OUTPUT);
  pinMode(STEP_PIN, OUTPUT);

  Serial.begin(9600);
  Serial.println("Ready to receive commands.");
}

void loop() {
  // Aguarda comandos a partir do Python
  if (Serial.available() > 0) {
    char command = Serial.read();
    
    // Verifica o comando recebido
    switch (command) {
      case 'R':  // Comando para girar para a direita (sentido horário)
        digitalWrite(DIR_PIN, HIGH);
        rotateOneRevolution();
        digitalWrite(DIR_PIN, LOW);
        rotateOneRevolution();
        break;
      
      case 'L':  // Comando para girar para a esquerda (sentido anti-horário)
        digitalWrite(DIR_PIN, LOW);
        rotateOneRevolution();
        digitalWrite(DIR_PIN, HIGH);
        rotateOneRevolution();
        break;
    }
  }
}

void rotateOneRevolution() {
  // Gira o motor uma revolução
  for (int i = 0; i < stepsPerRevolution; i++) {
    // Estas quatro linhas resultam em 1 passo:
    digitalWrite(STEP_PIN, HIGH);
    delayMicroseconds(2000);
    digitalWrite(STEP_PIN, LOW);
    delayMicroseconds(2000);
  }
}
