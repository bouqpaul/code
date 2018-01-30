/**
 * Creation date: 2015-10-22
 * Description:
 *    This file contains the functions for serializing/deserializing an image given a filename
 */

#include "fun_targa.h"

/* Free the memory allocated for the given image structure. */
void freeImage(image_desc *pdesc);

/* Write an image given a header structure and an image
 * structure into a file named fName.  */
int writeImage(image_desc desc, targa_header head, char* fName);

/* Read an image from fName and create a header structure and an image
 * structure pointed to by pHeader and pDesc.  */
int readImage(image_desc *pDesc, targa_header *pHeader, char * fName);

/* Allocate memory for the image structure given in parameter. */
int mallocImage(image_desc *pDesc, uint16_t width, uint16_t height);

/* Ecrit les pixels noirs de imgBin dans imgCol */
int drawImageOver(image_desc * imgCol, image_desc * imgBin, targa_header * pHeaderCol, char * fName);

/* Tourne de 90 degrés dans le sens horaires (ne marche pas)*/
int rotateImage(image_desc * pDesc, targa_header * pHeader, char * fName);

/* Effet miroir horizontal*/
int flipImage(image_desc * pDesc, targa_header * pHeader, char * fName);

/* Inverse une image binaire*/
int invertimage(image_desc * pDesc, targa_header * pHeader, char * fName);

/* Transforme une image en image binaire*/
int threshold(image_desc * pDesc, targa_header * pHeader, char * fName, uint8_t valBlue, uint8_t valGreen, uint8_t valRed);

/* Permute les niveaux de bleus et de rouge */
int swapColors(image_desc * pDesc, targa_header * pHeader, char * fName);
