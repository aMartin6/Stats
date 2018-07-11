/* Adds drive force to the statistics */

#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>
#include<sys/stat.h>

int main ()
{ 
  FILE *in;
  FILE *outv;
  FILE *outc;
  FILE *outn;
  double drive;
  char trash[120];
  double trash2;
  int trash3;

  //open drive data file
  if ((in = fopen("Pa0", "r")) == NULL)
    {
      printf("Input file Pa0 not found \n");
      exit(-1);
    }

  if ((outv = fopen("../../velocity_stats.txt", "a")) == NULL)
    {
      printf("Output file velocity_stats.txt not found \n");
      exit(-1);
    }

  if ((outc = fopen("../../cluster_stats.txt", "a")) == NULL)
    {
      printf("Output file cluster_stats.txt not found \n");
      exit(-1);
    }
  
  if ((outn = fopen("../../nn_stats.txt", "a")) == NULL)
    {
      printf("Output file nn_stats.txt not found \n");
      exit(-1);
    }

  fscanf (in,"%s %f\n",&trash,&trash2);
  fscanf (in,"%s %f\n",&trash,&trash2);
  fscanf (in,"%s %f\n",&trash,&trash2);
  fscanf (in,"%s %f\n",&trash,&trash2);
  fscanf (in,"%s %f\n",&trash,&trash2);
  fscanf (in,"%s %d\n",&trash,&trash3);
  fscanf (in,"%s %f\n",&trash,&trash2);
  fscanf (in,"%s %f\n",&trash,&trash2);
  fscanf (in,"%s %d\n",&trash,&trash3);
  fscanf (in,"%s %d\n",&trash,&trash3);
  fscanf (in,"%s %f\n",&trash,&trash2);
  fscanf (in,"%s %f\n",&trash,&trash2); 
  fscanf (in,"%s %f\n",&trash,&trash2);
  fscanf (in,"%s %f\n",&trash,&trash2);
  fscanf (in,"%s %f\n",&trash,&trash2);
  fscanf (in,"%s %lf\n",&trash,&drive);


  printf ("Drive = %lf\n",trash, drive);
  fflush (stdout);

  fprintf(outv, "%lf ", drive);
  fprintf(outc, "%lf ", drive);
  fprintf(outn, "%lf ", drive);
  
  fclose (in);
  fclose (outv);
  fclose (outc);
  fclose (outn);

  return 0;
}
  
