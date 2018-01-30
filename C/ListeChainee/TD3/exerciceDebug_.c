#include <stdlib.h>
#include <stdio.h>

void echange(int* a, int* b) {
  int tmp;
  tmp = *b;
  *b = *a;
  *a = tmp;

}

int main(int argc, char *argv[]) {
  int valeur1 = 15;
  int valeur2 = 42;
  int *valeur3;
  
  printf("Avant echange\nvaleur1=%d\nvaleur2=%d\n", valeur1, valeur2);
  echange(&valeur1, &valeur2);
  printf("Apres echange\nvaleur1=%d\nvaleur2=%d\n", valeur1, valeur2);
  
  int temp = 217;
  valeur3 = &temp;
  
  printf("Avant echange\nvaleur1=%d\nvaleur3=%d\n", valeur1, *valeur3);
  echange(&valeur1, valeur3);
  printf("Apres echange\nvaleur1=%d\nvaleur3=%d\n", valeur1, *valeur3);
  
  return EXIT_SUCCESS;
}
