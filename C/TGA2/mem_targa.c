#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "mem_targa.h"


int readImage(image_desc *pDesc, targa_header *pHeader, char * fName){
    FILE * fd = fopen(fName, "rb");
    fread(pHeader, sizeof(targa_header), 1, fd);
    pDesc->fname = fName;
    mallocImage(pDesc, pHeader->width, pHeader->height);
    readTargaImage(pDesc, fd);
    fclose(fd);
    return 0;
    }


void readTargaImage(image_desc * pDesc, FILE * fd){
    int i;
    for(i = 0; i < (pDesc->width * pDesc->height); i++){
        fread((pDesc->pBlue) + i, sizeof(uint8_t), 1, fd);
        fread((pDesc->pGreen) + i, sizeof(uint8_t), 1, fd);
        fread((pDesc->pRed) + i, sizeof(uint8_t), 1, fd);
    }

}

void writeTargaImage(image_desc * pDesc, FILE * fd){
    int i;
    for(i = 0; i < (pDesc->width * pDesc->height); i++){
        fwrite((pDesc->pBlue) + i, sizeof(uint8_t), 1, fd);
        fwrite((pDesc->pGreen) + i, sizeof(uint8_t), 1, fd);
        fwrite((pDesc->pRed) + i, sizeof(uint8_t), 1, fd);
    }

}

int mallocImage(image_desc *pDesc, uint16_t width, uint16_t height){
    pDesc->width = width;
    pDesc->height = height;
    
    pDesc->pRed = malloc(sizeof(uint8_t) * (width * height));  
    pDesc->pGreen = malloc(sizeof(uint8_t) * (width * height));
    pDesc->pBlue = malloc(sizeof(uint8_t) * (width * height));
    return 0;

}

void freeImage(image_desc *pdesc){
    free(pdesc->pRed);
    free(pdesc->pBlue);
    free(pdesc->pGreen);
}


int writeImage(image_desc *pDesc, targa_header* pHeader, char* fName){
    FILE * fd = fopen(fName, "wb");
    fwrite(pHeader, sizeof(targa_header), 1, fd);
    writeTargaImage(pDesc, fd);
    fclose(fd);
    return 0;

}

void image_clone(image_desc imgIn, image_desc *pimgOut)
{
  int i = 0, err = 1;
  err = mallocImage(pimgOut, imgIn.width, imgIn.height);
  if(!err){
    return ;
  }

  /* Transformation  : equiv. to : for (i=0; i < i_img.width*i_img.height; i++)*/
  for (i=0; i<(imgIn.width) * (imgIn.height); i++) {
    (pimgOut->pBlue)[i] = (imgIn.pBlue)[i];
    (pimgOut->pGreen)[i] = (imgIn.pGreen)[i];
    (pimgOut->pRed)[i] = (imgIn.pRed)[i];
  }
}



void greyScale(image_desc *pDesc, targa_header * pHeader, char * fName, int coeffBlue, int coeffGreen, int coeffRed){
    FILE * fd = fopen(fName, "wb");
	fwrite(pHeader, sizeof(targa_header), 1, fd);
    int i;
	uint8_t * plan = malloc(sizeof(uint8_t) * (pHeader->width * pHeader->height));
	//mallocImage(pDesc, pHeader->width, pHeader->height);
	
	uint8_t temp;
    for(i = 0; i < (pDesc->width * pDesc->height); i += 3){
		temp = 0;
		/*
		temp += (*(pDesc->pBlue + i)) * coeffBlue;
		temp += (*(pDesc->pGreen + i)) * coeffGreen;
		temp += (*(pDesc->pRed + i)) * coeffRed;
		*/
		
		plan[i] = (*(pDesc->pBlue + i)) * coeffBlue;
		plan[i + 1] = (*(pDesc->pGreen + i)) * coeffGreen;
		plan[i + 2] = (*(pDesc->pRed + i)) * coeffRed;
           
    }
	
	pDesc->pBlue = plan;
	pDesc->pGreen = plan;
	pDesc->pRed = plan;
	
    writeTargaImage(pDesc, fd);
    fclose(fd);

}

void mirror(image_desc * pDesc, targa_header * pHeader, char * fName){
	FILE * fd = fopen(fName, "wb");
	fwrite(pHeader, sizeof(targa_header), 1, fd);
	uint8_t * plan = malloc(sizeof(uint8_t) * (pHeader->width * pHeader->height));
	int i, j;
	for(i = 0; i < pDesc->height; i++){
		printf("---------\n");
		for(j = pDesc->width; j > 0; j--){
			// pDesc->pBlue = (pDesc->pBlue) + (i + j);
			// pDesc->pGreen = (pDesc->pGreen) + (i + j);
			// pDesc->pRed = (pDesc->pRed) + (i + j);
			
			
			int indice = (pDesc->width * (i - 1)) + j;
			printf("INDICe: %i\n", indice);
			
			plan[indice] = *((pDesc->pBlue) + (indice));
			plan[indice - 1] = *((pDesc->pGreen) + (indice));
			plan[indice - 2] = *((pDesc->pRed) + (indice));
			
			
		}
		
	}

	pDesc->pBlue = plan;
	pDesc->pGreen = plan;
	pDesc->pRed = plan;

    writeTargaImage(pDesc, fd);
    fclose(fd);
	
}


int main(){
    image_desc DD;
    targa_header TT;
    
    image_desc * pDD = &DD;
    targa_header * pTT = &TT;
    
    char * fName = "ensta_Tatoo_nb.tga";
    char * fCopie = "Copy.tga";
    char * fGrey = "Greyscale.tga";
	char * fMirror = "Mirror.tga";
    
    readImage(pDD, pTT, fName);
    writeImage(pDD, pTT, fCopie);
    greyScale(pDD, pTT, fGrey, 1, 0, 0);
	//mirror(pDD, pTT, fMirror);
    return 0;
}


