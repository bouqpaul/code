#include <stdlib.h>
#include <stdio.h>
#include "mem_targa.h"

/* Free the memory allocated for the given image structure. */
void freeImage(image_desc *pDesc)
{
  free(pDesc->pBlue); pDesc->pBlue = NULL;
  free(pDesc->pGreen); pDesc->pGreen = NULL;
  free(pDesc->pRed); pDesc->pRed = NULL;
}

/* Write an image given a header structure and an image
 * structure into a file named fName.  */
int readImage(image_desc *pDesc, targa_header *pHeader, char * fName)
{
  FILE * fDesc;
  int i = 0, err = 1;
  /* Open fDesc file */
  fDesc = fopen(fName,"r");
  if (fDesc == NULL) {
    fprintf(stderr, "Cannot read the file \"%s\".\n", fName);
    return 0;
  }
  /* Read the header */
  fread(pHeader, sizeof(targa_header), 1, fDesc);

  printf("[mem_targa] Header : %u %u %u %u %u\n",
          pHeader->idlength, pHeader->colourmaptype, pHeader->datatypecode, pHeader->width, pHeader->height);

  /* Initialize image struct */
  err = mallocImage(pDesc, pHeader->width, pHeader->height);
  if(!err){
    fprintf(stderr, "Cannot initialize the image \n");
    return 0;
  }

  /* Fill pixel by pixel the 3 color layers */
  for(i=0; i<pHeader->width*pHeader->height; i++)
  {
    // read 1 int : blue
    fread(pDesc->pBlue+i, sizeof(uint8_t), 1, fDesc);
    // read 1 int : green
    fread(pDesc->pGreen+i, sizeof(uint8_t), 1, fDesc);
    // read 1 int : red
    fread(pDesc->pRed+i, sizeof(uint8_t), 1, fDesc);
  }
  printf("[readImage] Number of pixels : %d\n", i);

  fclose(fDesc);

  return 1;
}


/* Read an image from fName and create a header structure and an image
 * structure pointed to by pHeader and pDesc.  */
int writeImage (image_desc desc, targa_header head, char * fName)
{
  FILE *fDesc;
  int i;

  /* Open output image file */
  if ((fDesc = fopen(fName, "w")) == NULL)
  {
    fprintf (stderr, "Cannot create the file \"%s\".\n", fName);
    return 0;
  }

  /* Write the header in fDesc*/
  head.width = desc.width;
  head.height = desc.height;
  printf("[write mem_targa] Header : %u %u %u %u %u \n",
         head.idlength, head.colourmaptype, head.datatypecode, head.width, head.height);

  fwrite(&head, sizeof(targa_header), 1, fDesc);

  /* Write in fDesc head.width*head.height pixels for each color */
  for(i=0; i<head.width*head.height; i++)
  {
    fwrite((desc.pBlue)+i, sizeof(uint8_t), 1, fDesc);
    fwrite((desc.pGreen)+i, sizeof(uint8_t), 1, fDesc);
    fwrite((desc.pRed)+i, sizeof(uint8_t), 1, fDesc);
  }
  printf("[writeImage] Number of pixels : %d\n", i);

  fclose(fDesc);

  return 1;
}


/* Allocate memory for the content of the image structure given in parameter.
 * return 1 if allocation succeeds,
 * 0 otherwise.
 */
int mallocImage(image_desc *pDesc, uint16_t width, uint16_t height)
{
  /* Do not reallocate if the pDesc pointer is already initialized */
  if (pDesc == NULL)
  {
    printf("Pointer on image structure must be allocated first\n");
    pDesc = (image_desc*)malloc(sizeof(image_desc));
  }

  pDesc->width = width;
  pDesc->height = height;

  /* Allocate memory for each image plane */
  pDesc->pBlue = (uint8_t *) malloc(sizeof(uint8_t) * height * width);
  pDesc->pGreen = (uint8_t *) malloc(sizeof(uint8_t) * height * width);
  pDesc->pRed = (uint8_t *) malloc(sizeof(uint8_t) * height * width);
  if (pDesc->pBlue == NULL || pDesc->pGreen == NULL || pDesc->pRed == NULL) {
    return 0;
  }

  return 1;
}


int swapColors(image_desc * pDesc, targa_header * pHeader, char * fName){
    uint8_t * temp = pDesc->pBlue;
    pDesc->pBlue = pDesc->pRed;
    pDesc->pRed = temp;
    writeImage(*pDesc, *pHeader, fName);
    return 1;
    
}

int threshold(image_desc * pDesc, targa_header * pHeader, char * fName, uint8_t valBlue, uint8_t valGreen, uint8_t valRed){
    int i;
    for(i = 0; i < pHeader->width * pHeader->height; i++){
        if((pDesc->pBlue)[i]< valBlue && (pDesc->pRed)[i] < valRed && (pDesc->pGreen)[i] < valGreen){
            (pDesc->pBlue)[i] = 0;
            (pDesc->pRed)[i] = 0;
            (pDesc->pGreen)[i] = 0;
            }
            else
            {
            pDesc->pBlue[i] = 255;
            (pDesc->pRed)[i] = 255;
            (pDesc->pGreen)[i] = 255;
            }
                        
    }
   writeImage(*pDesc, *pHeader, fName);   
    return 1;
}

int invertimage(image_desc * pDesc, targa_header * pHeader, char * fName){
    int i;
    for(i = 0; i < pHeader->width * pHeader->height; i++){
        if((pDesc->pBlue)[i]==0 ){
            (pDesc->pBlue)[i] = 255;
            (pDesc->pRed)[i] = 255;
            (pDesc->pGreen)[i] = 255;
            }
            else
            {
            pDesc->pBlue[i] = 0;
            (pDesc->pRed)[i] = 0;
            (pDesc->pGreen)[i] = 0;
            }
            }
    writeImage(*pDesc, *pHeader, fName);   
    return 1;
}


int flipImage(image_desc * pDesc, targa_header * pHeader, char * fName){
    int i;
    uint8_t tempB, tempR, tempG;
    
    for(i = 0; i<pHeader -> height/2;i++){
        int j;
        for (j=0;j<pHeader -> width; j++){
            tempB = (pDesc->pBlue)[(pHeader->height - i-1)*(pHeader -> width)+j];
            tempR  = (pDesc->pRed)[(pHeader->height - i-1)*(pHeader -> width)+j];
            tempG =(pDesc->pGreen)[(pHeader->height - i-1)*(pHeader -> width)+j];
            
            (pDesc->pBlue)[(pHeader->height - i-1)*(pHeader -> width)+j] =(pDesc->pBlue)[i*(pHeader -> width)+j] ;
            (pDesc->pRed)[(pHeader->height - i-1)*(pHeader -> width)+j] = (pDesc->pRed)[i*(pHeader -> width)+j];
            (pDesc->pGreen)[(pHeader->height - i-1)*(pHeader -> width)+j] =(pDesc->pGreen)[i*(pHeader -> width)+j];
            
            
            (pDesc->pBlue)[i*(pHeader -> width)+j] =tempB;
            (pDesc->pRed)[i*(pHeader -> width)+j] = tempR;
            (pDesc->pGreen)[i*(pHeader -> width)+j] =tempG;           
            
        }
    }
writeImage(*pDesc, *pHeader, fName);
return 0;
}

int rotateImage(image_desc * pDesc, targa_header * pHeader, char * fName){
    image_desc Rdesc;
    targa_header Rhead;
    
    image_desc * pRDesc = &Rdesc;
    targa_header * pRhead = &Rhead;
    
    //pRhead->width = pHeader->height;
    //pRhead->height = pHeader->width;
    
    int err = mallocImage(pRDesc, pHeader->height, pHeader-> width);
    int i;
    for (i = 0;  i<pHeader -> height;i++){
        int j;
        for (j = 0; j <pHeader -> width; j++){
            pRDesc->pBlue[(pHeader->height-i)*j] = pDesc->pBlue[i * pHeader->width + j];
            pRDesc->pRed[(pHeader->height-i)*j] = pDesc->pRed[i * pHeader->width + j];
            pRDesc->pGreen[(pHeader->height-i)*j] =  pDesc->pGreen[i * pHeader->width + j];
            
        }
    }
    writeImage(*pRDesc, *pHeader, fName);
    return 0;

}


int drawImageOver(image_desc * imgCol, image_desc * imgBin, targa_header * pHeaderCol, char * fName){
    if(imgCol->height != imgBin->height || imgCol->width != imgBin->width){
        printf("Image de tailles différentes.\n");
        return 1;
    }
    int i;
    for(i = 0; i < imgCol->height * imgCol->width; i++){
        if(imgBin->pBlue[i] ==0 && imgBin->pRed[i] ==0 && imgBin->pGreen[i] ==0){
            imgCol->pBlue[i] = 0;
            imgCol->pRed[i] = 0;
            imgCol->pGreen[i] = 0;
        }
    
    }
    writeImage(*imgCol, *pHeaderCol, fName);

}



/*int main(){
    image_desc desc;
    targa_header head;
    
    image_desc * pDesc = &desc;
    targa_header * phead = &head;
    
    image_desc descCol;
    targa_header headCol;
    
    image_desc * pDescCol = &descCol;
    targa_header * pheadCol = &headCol;
    
    char * fName = "background.tga";
    char * fCopie = "Copy.tga";
    char * fSwap = "Swap.tga";
    char * fThres = "Threshold.tga";
    char * fInv = "Inverted.tga";
    char * fFlip = "Flipped.tga";
    char * fRota = "Rotated.tga";
    char * fDrawOver = "DrawOver.tga";
	//char * fMirror = "Mirror.tga";
	
	printf("Toto\n");
    readImage(pDescCol, pheadCol, fName);
    readImage(pDesc, phead, fName);
    printf("Copy\n");
    //writeImage(desc, head, fCopie);
    
	printf("Tt\n");
    //swapColors(pDesc, phead, fSwap);
    
    threshold(pDesc, phead, fThres,128,128,128);
    
    //invertimage(pDesc, phead, fInv);
   //flipImage(pDesc, phead, fFlip);
    //rotateImage(pDesc, phead, fRota);
    drawImageOver(pDescCol, pDesc, pheadCol, fDrawOver);
    

}*/
