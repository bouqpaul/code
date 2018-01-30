#include <stdlib.h>
#include <stdio.h>
struct cell {
    int value;
    struct cell *next;
    };
    
struct list {
    int taille;
    struct cell *first;
    };

void push(struct list *l, int value) {
    struct cell *c;
    c = malloc(sizeof(struct cell));
    c->value = value;
    c->next = l->first;
    l->first = c;
    
    (l->taille)++;
    }
    
int pop(struct list *l) {
    int res;
    if((!(l->first))){
        printf("Liste vide.\n");
        res = -1;
        }
    else{
        res = l->first->value;

        struct cell *newFirst;
        newFirst = l->first->next;
        free(l->first);
        l->first = newFirst;
    
        }
    (l->taille)--;
    return res;
    }

void reverse(struct list *l){
    struct cell *courant = l->first;
    struct cell *precedent = {NULL};
    while(courant != NULL){
        struct cell *temp = courant->next;
        courant->next = precedent;
        precedent = courant;
        courant = temp;
    }
    l->first = precedent;
}

void print(struct list *l){
    printf("[");
    if(l->first != NULL){
        struct cell *courant = l->first;
    
        while(courant->next){
            printf("%i, ", courant->value);
            courant = courant->next;
    
            }
        printf("%i", courant->value);
    }
    printf("]\n");

}

void split(int x, struct list *l, struct list *l1, struct list *l2){
    struct cell *courant = l->first;
    while(courant != NULL){
        int temp = pop(l);
        if((temp) <= x){
            push(l1, temp);
        }else{
            push(l2, temp);
        }
        courant = l->first;
    }


}

int main(){
    struct list l = {0, NULL};
    push(&l, 4);
    push(&l, 6);
    push(&l, 16);
    push(&l, 1654546);            
    print(&l);
    
    reverse(&l);
    print(&l);
    struct list l1 = {0, NULL};
    struct list l2 = {0, NULL};
    split(6, &l, &l1, &l2);
    print(&l);
    print(&l1);
    print(&l2);
    return 0;


}
