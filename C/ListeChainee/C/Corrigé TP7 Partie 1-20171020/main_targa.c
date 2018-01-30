#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdint.h>
#include <getopt.h>
#include "fun_targa.h"
#include "mem_targa.h"
int main(int argc, char *argv[])
{
  char *inputfn=NULL, *outputfn=NULL; /* input image file, output image file */
  image_desc i_img, o_img;
  targa_header i_head; /* Header of input image */
  char c;
  static struct option long_options[] =
    {
      /* These options don’t set a flag.
         We distinguish them by their indices. */
      {"example", no_argument,        0, 'e'},
      {"input",   required_argument , 0, 'i'},
      {"output",  required_argument,  0, 'o'},
      {0, 0, 0, 0}
    };
  /* Parse command line arguments */
  int option_index = 0;
  while ((c = getopt_long (argc, argv, "ei:o:", long_options, &option_index)) != -1) {
    switch (c) {
    case 'i':
      /* optarg : global var from unistd.h */
      inputfn = optarg;
      break;
    case 'o':
      outputfn = optarg;
      break;
    case 'e':
      printf("If we had an --example or -e option in command...\n");
      break;
    default:
      printf("unrecognized argument\n");
      exit(EXIT_FAILURE);
    }
  }

  /* Below: uncomment for a unit test without using command-line options */
  /*
  inputfn = "./input/logo.tga";
  outputfn = "logoOutput.tga"; */

  if (inputfn==NULL || outputfn==NULL) {
		fprintf(stderr, "Usage : %s -i <input_file> -o <output_file>\n", argv[0]);
		fprintf(stderr, "No input and/or output file.\n");
		exit(EXIT_FAILURE);
  }

	// READ
	readImage(&i_img, &i_head, inputfn);

  image_clone(i_img, &o_img);

  // WRITE. Note: input image header of clone is also the same as output image header.
  writeImage(o_img, i_head, outputfn);
  freeImage(&o_img);


	exit(EXIT_SUCCESS);
}
