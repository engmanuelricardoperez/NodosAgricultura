// sistemaLuces.ino
int led1 =2;
int led2 =3;
int led3= 4;
int led4=13;
int fotocelda=0;
int valorFotocelda=0;
int salida1=0;
int salida2=0;
int salida3=0;
int salida4=0;
int senialFoto=0;
String leerSerial;
void setup() {
  pinMode(led1,OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  Serial.begin(9600);

}

void loop() {
  valorFotocelda=analogRead(fotocelda);
  
  
  if(valorFotocelda<400){
    digitalWrite(led1, HIGH);
    digitalWrite(led2, HIGH);
    digitalWrite(led3, HIGH);
    digitalWrite(led4, HIGH);
    senialFoto++;
    if(senialFoto>=2)
      senialFoto=2;
    delay(200);
  }else{

       if(salida1==0){
      digitalWrite(led1, LOW);
      senialFoto=0;
    }
    if(salida2==0){
      digitalWrite(led2, LOW);
      senialFoto=0;
    }
    if(salida3==0){
      digitalWrite(led3, LOW);
      senialFoto=0;
    }
    if(salida4==0){
      digitalWrite(led4, LOW);
      senialFoto=0;
    }

  }
  
  if(senialFoto==1){
    Serial.println("Sectores Encendidos Fotocelda");
      
  }
  
  while(Serial.available()){
    leerSerial= Serial.readString();
    if(leerSerial=="sectorA_1"){
      digitalWrite(led1, HIGH);
      Serial.println("Sector 1 Encendido Manual");
      salida1=1;
      //delay(0500);
    }else if(leerSerial=="sectorA_0"){
      digitalWrite(led1, LOW);
      Serial.println("Sector 1 Apagado");
      salida1=0;
        
    }else if(leerSerial=="sectorB_1"){
      digitalWrite(led2, HIGH);
      Serial.println("Sector 2 Encendido Manual");
      salida2=1;
        
    }else if(leerSerial=="sectorB_0"){
      digitalWrite(led2, LOW);
      Serial.println("Sector 2 Apagado");
      salida2=0;
        
    }else if(leerSerial=="sectorC_1"){
      digitalWrite(led3, HIGH);
      Serial.println("Sector 3 Encendido Manual");
      salida3=1;
        
    }else if(leerSerial=="sectorC_0"){
      digitalWrite(led3, LOW);
      Serial.println("Sector 3 Apagado");
      salida3=0;
        
    }else if(leerSerial=="sectorD_1"){
      digitalWrite(led4, HIGH);
      Serial.println("Sector 4 Encendido Manual");
      salida4=1;
        
    }else if(leerSerial=="sectorD_0"){
      digitalWrite(led4, LOW);
      Serial.println("Sector 4 Apagado");
      salida4=0;
        
    }
  }
  

}



