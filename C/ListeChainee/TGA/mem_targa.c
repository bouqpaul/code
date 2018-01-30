#include <stdio.h>
#include <stdlib.h>
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
        fread((pDesc->pBlue)+i, sizeof(uint8_t), 1, fd);
        fread((pDesc->pGreen)+i, sizeof(uint8_t), 1, fd);
        fread((pDesc->pRed)+i, sizeof(uint8_t), 1, fd);
    }

}

void writeTargaImage(image_desc * pDesc, FILE * fd){
    int i;
    for(i = 0; i < (pDesc->width * pDesc->height); i++){
        fwrite((pDesc->pBlue)+i, sizeof(uint8_t), 1, fd);
        fwrite((pDesc->pGreen)+i, sizeof(uint8_t), 1, fd);
        fwrite((pDesc->pRed)+i, sizeof(uint8_t), 1, fd);
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

void greyScale(image_desc *pDesc, targa_header * pHeader, char * fName){
    FILE * fd = fopen(fName, "wb");
    int i;
    for(i = 0; i < (pDesc->width * pDesc->height); i++){
        uint8_t * temp = (((pDesc->pBlue)+i) + ((pDesc->pRed)+i) + ((pDesc->Green)+i)) / 3;
        pDesc->Blue = temp;
        pDesc->Green = temp;
        pDesc->Red = temp;
    
    }
    writeTargaImage(pDesc, pHeader, fName);
    fclose(fd);

}


void main(){
    image_desc DD;
    targa_header TT;
    
    image_desc * pDD = &DD;
    targa_header * pTT = &TT;
    
    char * fName = "ensta_Tatoo_nb.tga";
    char * fCopie = "YY.tga";
    char * fGrey = "grey.tga";
    
    readImage(pDD, pTT, fName);
    //writeImage(pDD, pTT, fCopie);
    greyScale(pDD, pTT, fGrey);
    
}


