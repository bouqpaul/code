#include <stdio.h>
#include <stdlib.h>

struct cell {
	int value;
	struct cell * next;
};

struct list {
	struct cell * first;
};

void push(struct list * l, int value){
	struct cell * c;
	c = malloc(sizeof(struct cell));
	c->value = value;
	c->next = l->first;
	l->first = c;
	
	
}


void print(struct list *l){
	printf("[");
	struct cell * courant = l->first;
	while(courant != NULL){
		printf("%i", courant->value);
		courant = courant->next;
		if(courant != NULL){printf(", ");}
		
	}
	printf("]\n");
}


int pop(struct list * l){
	if(l->first != NULL){
	struct cell * premier = l->first;
	int resPop = premier->value;
	l->first = premier->next;
	free(premier);
	return resPop;
	}else{
		printf("Erreur: Liste vide.\n");
		return -1;
}
}



void reverse(struct list * l){
	struct cell * courant = l->first;
	struct cell * precedent = {0, NULL};
	while(courant != NULL){
		struct cell * tempCC = courant->next;
		courant->next = precedent;
		
		
		struct cell * CC = courant;
		courant = tempCC;
		precedent = CC;
	}
	l->first = precedent;
	
}


void split(int x, struct list * l, struct list * l1, struct list * l2){
	int valCourant = pop(l);
	while(valCourant != -1){
		if(valCourant <= x){push(l1, valCourant);}
		else{push(l2, valCourant);}
		valCourant = pop(l);
		
		
	}

}

void append(struct list * l1, struct list * l2, struct list * l){
	struct cell * courant = l1->first;
	while(courant != NULL){
		push(l, courant->value);
		courant = courant->next;
		
	}
	
	courant = l2->first;
	while(courant != NULL){
		push(l, courant->value);
		courant = courant->next;
		
	}
	//reverse(l);
	
	
}

/*void quick_sort(struct list * l){
	printf("Quick Sort recurs.\n");
	int cle = pop(l);
	struct list * sub = malloc(sizeof(struct list));
	struct list * sup = malloc(sizeof(struct list));
	
	
	if(cle == -1){
		printf("Liste source vide.\n");
		append(sub, sup, l);
		
	
		
	}else{
		printf("Split.\n");
		split(cle, l, sub, sup);
		
		printf("Recurs1.\n");
		quick_sort(sub);
		
		printf("Recurs2.\n");
		quick_sort(sup);
		push(sup, cle);
		//struct list * sorted = {NULL};
	}
	free(sub);
	free(sup);
}
*/


void main(){
	struct list l = {NULL};
	//struct list l1 = {NULL};
	//struct list l2 = {NULL};
	
	push(&l, 10);
	push(&l, 9);
	push(&l, 8);
	
	push(&l, 4);
	push(&l, 354);
	push(&l, 41);
	push(&l, 44561);
	push(&l, 44422121);
	push(&l, 41777);
	push(&l, 499991);
	
	print(&l);
	//quick_sort(&l);
	print(&l);
	//print(&l);
	//append(&l1, &l2, &l);
	//print(&l);
	
	
}

