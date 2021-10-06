// ################################################################################
// Programa de ejemplo para tablero de control usando PYQT QT como interfaz grafica.
// Cualquier aporte, mejora, a mi correo JAHIRG@YAHOO.COM
// No soy experto en programacion, quiero aprender.
// Este codigo es desean hace proyectos usando interfaz grafica en pc
// ###############################################################################

//######################################################################
//# LISTA DE REGISTROS A USAR PARA EL ENVIO DE DATOS
//######################################################################

int au16data[16] = {
  300, 102, 1003, 104, 10000, 20000, 30000, 32000, 0, 0, 0, 0, 0, 0, 1, 1 };
const size_t dataLength = 16;


//######################################################################
//# DEFINICION DE PINES:
//# PLEASE DONT USE PULLUP INSTRUCTIONS CAUSE FAULT IN COMMUNICTIONS
//######################################################################
void setup() {
  // #### Slider para PMW
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);   
  pinMode(7,OUTPUT);
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT); 
  pinMode(10,OUTPUT);
  pinMode(11,OUTPUT);

  // ### Senales de pulsadores 
  pinMode(62,INPUT);
  pinMode(63,INPUT);
  pinMode(64,INPUT);
  pinMode(65,INPUT);
  pinMode(66,INPUT);
  pinMode(67,INPUT);
  pinMode(68,INPUT);
  pinMode(69,INPUT);

  // ### Senales para indicadores
  pinMode(22,OUTPUT);
  pinMode(23,OUTPUT); 
  pinMode(24,OUTPUT);
  pinMode(25,OUTPUT);
  pinMode(26,OUTPUT);
  pinMode(27,OUTPUT); 
  pinMode(28,OUTPUT);
  pinMode(29,OUTPUT);

  Serial.begin( 9600 ); // baud-rate at 9600
  }

//##################################################################
//# ENVIO DE DATOS AL PC
//##################################################################
void sendBytes(uint16_t value)
  {
  Serial.write(highByte(value));
  Serial.write(lowByte(value));
  }

//##################################################################
//# ACTIVACION LEDS
//##################################################################
void vProcessaUart(String s)
  {
  if(s == "22H")
    digitalWrite(22,HIGH);
  if(s == "22L")
    digitalWrite(22,LOW);

  if(s == "23H")
    digitalWrite(23,HIGH);
  if(s == "23L")
    digitalWrite(23,LOW);

  if(s == "24H")
    digitalWrite(24,HIGH);
  if(s == "24L")
    digitalWrite(24,LOW);

  if(s == "25H")
    digitalWrite(25,HIGH);
  if(s == "25L")
    digitalWrite(25,LOW);

  if(s == "26H")
    digitalWrite(26,HIGH);
  if(s == "26L")
    digitalWrite(26,LOW);

  if(s == "27H")
    digitalWrite(27,HIGH);
  if(s == "27L")
    digitalWrite(27,LOW);

  if(s == "28H")
    digitalWrite(28,HIGH);
  if(s == "28L")
    digitalWrite(28,LOW);

  if(s == "29H")
    digitalWrite(29,HIGH);
  if(s == "29L")
    digitalWrite(29,LOW);


//#####################################################################
//# SECCION PWM 
//#####################################################################
  String pwm =s;
  int datapwm=0;
  pwm.remove(0, 3);
  datapwm=pwm.toInt();
  s.remove(3);

  if(s == "P04")
    analogWrite(4, datapwm);
  
  if(s == "P05")
    analogWrite(5, datapwm);
  
  if(s == "P06")
    analogWrite(6, datapwm); 
  
  if(s == "P07")
    analogWrite(7, datapwm); 
  
  if(s == "P08")
    analogWrite(8, datapwm);
  
  if(s == "P09")
    analogWrite(9, datapwm);
  
  if(s == "P10")
    analogWrite(10, datapwm); 
  if(s == "P11")
    analogWrite(11, datapwm);
  }


//#####################################################################
//# BUCLE PRINCIPAL
//#####################################################################
void loop() {
  
  //#### Registro 0 al 7 son entradas analogas
  au16data[0]=analogRead(A0);
  au16data[1]=analogRead(A1);
  au16data[2]=analogRead(A2);
  au16data[3]=analogRead(A3);
  au16data[4]=analogRead(A4);
  au16data[5]=analogRead(A5);
  au16data[6]=analogRead(A6);
  au16data[7]=analogRead(A7);

  //#### Registro 8 al 15 son entradas digitales
  if(digitalRead(62))
    au16data[8]=621;
  else
    au16data[8]=620;

  if(digitalRead(63))
    au16data[9]=631;
  else
    au16data[9]=630;

  if(digitalRead(64))
    au16data[10]=641;
  else
    au16data[10]=640;

  if(digitalRead(65))
    au16data[11]=651;
  else
    au16data[11]=650;

  if(digitalRead(66))
    au16data[12]=661;
  else
    au16data[12]=660;

  if(digitalRead(67))
    au16data[13]=671;
  else
    au16data[13]=670;

  if(digitalRead(68))
    au16data[14]=681;
  else
    au16data[14]=680;

  if(digitalRead(69))
    au16data[15]=691;
  else
    au16data[15]=690;


  //#### Envio de datos al PC #########
  for(int n = 0; n < 16; n++){
    sendBytes(au16data[n]);
  }

  //#### Captura de datos del PC ######
  String sz = "";
  char ch;
  int nCmpt = 0;
  while (Serial.available() > 0) {
    sz += (char)Serial.read();
    nCmpt++;
    delay(2);
    }
  if(nCmpt)
  vProcessaUart(sz);
  delay(100);
}
