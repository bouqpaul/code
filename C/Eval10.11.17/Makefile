default: eval.c
	gcc eval.c -o eval.o
	eval.o

clean: *.o
	rm *.o

tar:
	tar --exclude='./Archive' -cvf ./Archive/Bouquet_Clavier_36C.zip ./

man:
	cat ./eval.h
