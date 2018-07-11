/* Averages the driving force of particels over time */

#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>
#include<sys/stat.h>

int main ()
{
  
  FILE *in;
  FILE *inp;
  FILE *out;
  int start = 200;
  int end = 5000;
  int count = 0;
  double sum = 0.0;
  double average;
  double average_scaled;
  double stddev1;
  float drive;
  int particle_number = 0;
  double drive_force;
  char trash[120];
  double trash2;
  int trash3;

  //open drive data file
  if ((in = fopen("fxtest_1_big.csv", "r")) == NULL)
    {
      printf("Input file fxtest_1_big.csv not found \n");
      exit(-1);
    }
  
  if ((inp = fopen("Pa0", "r")) == NULL)
    {
      printf("Input file Pa0 not found \n");
      exit(-1);
    }
  
  if ((out = fopen("../../velocity_stats.txt", "a")) == NULL)
    {
      printf("Output file velocity_stats.txt not found \n");
      exit(-1);
    }
  
  //else printf("Reading file \n");
  //fflush(stdout);

  //printf("Start value = %d, End value = %d\n", start, end);

  //Read in Drive force
  
  fscanf (inp,"%s %f\n",&trash,&trash2);
  fscanf (inp,"%s %f\n",&trash,&trash2);
  fscanf (inp,"%s %f\n",&trash,&trash2);
  fscanf (inp,"%s %f\n",&trash,&trash2);
  fscanf (inp,"%s %f\n",&trash,&trash2);
  fscanf (inp,"%s %d\n",&trash,&trash3);
  fscanf (inp,"%s %f\n",&trash,&trash2);
  fscanf (inp,"%s %f\n",&trash,&trash2);
  fscanf (inp,"%s %d\n",&trash,&trash3);
  fscanf (inp,"%s %d\n",&trash,&trash3);
  fscanf (inp,"%s %f\n",&trash,&trash2);
  fscanf (inp,"%s %f\n",&trash,&trash2); 
  fscanf (inp,"%s %f\n",&trash,&trash2);
  fscanf (inp,"%s %f\n",&trash,&trash2);
  fscanf (inp,"%s %f\n",&trash,&trash2);
  fscanf (inp,"%s %lf\n",&trash,&drive_force);
  
  //Calcualte sum within range
  while (!feof(in) && count <= end)
  {
    fscanf(in, "%f\n", &drive);
    if (count >= start)
    {
      sum += drive;
      particle_number += 1;
    }
    count += 1;
  }
  
  //Calculate average
  average = sum / particle_number;
  printf("Average Velocity = %lf\n", average);

  count = 0;
  sum = 0;
  rewind(in);

  //Calculate standard deviation
  while (!feof(in) && count <= end)
  {
    fscanf(in, "%f\n", &drive);
    if (count > 0 && count >= start)
      {
	sum += (drive - average)*(drive - average);
	particle_number += 1;
      }
    count += 1;
  }

  // Count - 2 = number of data points - 1
  stddev1 = sqrt(sum / (particle_number - 2)); 
  printf("Standard Deviation = %lf\n", stddev1);

  average_scaled = average / drive_force;

  fprintf(out, "%f ", average_scaled);
  fprintf(out, "%f ", stddev1);
  fprintf(out, "%f\n", average);

  fclose (in);
  fclose (inp);
  fclose (out);

  return 0;
}
  
