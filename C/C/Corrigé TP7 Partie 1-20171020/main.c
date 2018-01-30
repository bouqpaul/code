#include <stdio.h>
#include "mem_targa.h"
#include "mem_targa.c"
#include "fun_targa.h"

int main(){
    image_desc desc;
    targa_header head;
    
    image_desc * pDesc = &desc;
    targa_header * phead = &head;
    
    image_desc descCol;
    targa_header headCol;
    
    image_desc * pDescCol = &descCol;
    targa_header * pheadCol = &headCol;
    
    char * fName = "./input/lena_color.tga";
    char * fCopie = "Copy.tga";
    char * fSwap = "Swap.tga";
    char * fThres = "Threshold.tga";
    char * fInv = "Inverted.tga";
    char * fFlip = "Flipped.tga";
    char * fRota = "Rotated.tga";
    char * fDrawOver = "DrawOver.tga";
	
    readImage(pDescCol, pheadCol, fName);
    readImage(pDesc, phead, fName);

    writeImage(desc, head, fCopie);
    
    swapColors(pDesc, phead, fSwap);
    
    threshold(pDesc, phead, fThres,128,128,128);
    
    invertimage(pDesc, phead, fInv);
    
    flipImage(pDesc, phead, fFlip);
    
    rotateImage(pDesc, phead, fRota);
    
    drawImageOver(pDescCol, pDesc, pheadCol, fDrawOver);
    
    return 0;
    }
    
