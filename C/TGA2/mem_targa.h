#include "fun_targa.h"

/* Libère la mémoire occuper par l'image du descripteur */
void freeImage(image_desc *pdesc);

/* Ecrit une image .tga au chemin fName */
int writeImage(image_desc *desc, targa_header *head, char* fName);

/* Lit une image .tga depuis le chemin fName */
int readImage(image_desc *pDesc, targa_header *pHeader, char * fName);

/* Alloue en mémoire l'image contenu dans le descripteur pDesc */
int mallocImage(image_desc *pDesc, uint16_t width, uint16_t height);

void writeTargaImage(image_desc * pDesc, FILE * fd);

void readTargaImage(image_desc * pDesc, FILE * fd);

void greyScale(image_desc *pDesc, targa_header * pHeader, char * fName, int coeffBlue, int coeffGreen, int coeffRed);

void mirror(image_desc * pDesc, targa_header * pHeader, char * fName);

void image_clone(image_desc imgIn, image_desc *pimgOut);
