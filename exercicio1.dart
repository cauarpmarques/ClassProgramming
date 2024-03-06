//Exercício de Estrutura de Controle If-else:

import 'dart:io';
void main() {
  stdout.write("Digite um número aleatório inteiro:");
  int numero = int.parse(stdin.readLineSync()!);

  if (numero % 2 == 0 ) {
    print("$numero é um número par.");
  }else{
    print("$numero é um numero impar." );
  }
}


