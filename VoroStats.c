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
  FILE *out;
  int start = 0;
  int end = 600000;
  int count = 0;
  double sum4 = 0.0;
  double sum5 = 0.0;
  double sum6 = 0.0;
  double sum7 = 0.0;
  float average4;
  float average5;
  float average6;
  float average7;
  float stddev4;
  float stddev5;
  float stddev6;
  float stddev7;
  float p4 = 0.0;
  float p5 = 0.0;
  float p6 = 0.0;
  float p7 = 0.0;
  int particle_number = 0;

  //open drive data file
  if ((in = fopen("voro_stats.txt", "r")) == NULL)
    {
      printf("Input file voro_stats.txt not found \n");
      exit(-1);
    }
   //open drive data file
  if ((out = fopen("../../nn_stats.txt", "a")) == NULL)
    {
      printf("Output file nn_stats.txt not found \n");
      exit(-1);
    }
  
  //Calcualte sum within range
  while (!feof(in) && count <= end)
  {
    fscanf(in, "%f %f %f %f\n", &p4, &p5, &p6, &p7);
    if (count >= start)
      {
	sum4 += p4;
	sum5 += p5;
	sum6 += p6;
	sum7 += p7;
	particle_number += 1;
      }
    count += 1;
  }

  //Calculate average
  average4 = sum4 / particle_number;
  average5 = sum5 / particle_number;
  average6 = sum6 / particle_number;
  average7 = sum7 / particle_number;

  count = 0;
  sum4 = 0.0;
  sum5 = 0.0;
  sum6 = 0.0;
  sum7 = 0.0;
  particle_number = 0;
  rewind(in);

  //Calculate standard deviation
  while (!feof(in) && count <= end)
  {
    fscanf(in, "%f %f %f %f\n", &p4, &p5, &p6, &p7);
    if (count >= start)
      {
	sum4 += (p4 - average4)*(p4 - average4);
	sum5 += (p5 - average5)*(p5 - average5);
	sum6 += (p6 - average6)*(p6 - average6);
	sum7 += (p7 - average7)*(p7 - average7);
	particle_number += 1;
      }
    count += 1;
  }
  
  // Count - 2 = number of data points - 1
  stddev4 = sqrt(sum4 / (particle_number - 2)); 
  stddev5 = sqrt(sum5 / (particle_number - 2));
  stddev6 = sqrt(sum6 / (particle_number - 2));
  stddev7 = sqrt(sum7 / (particle_number - 2));

  fprintf(out, "%f ", average4);
  fprintf(out, "%f ", stddev4);
  fprintf(out, "%f ", average5);
  fprintf(out, "%f ", stddev5);
  fprintf(out, "%f ", average6);
  fprintf(out, "%f ", stddev6);
  fprintf(out, "%f ", average7);
  fprintf(out, "%f\n", stddev7);

  printf("Average p4 = %f Standard Deviation = %f\n", average4, stddev4);
  printf("Average p5 = %f Standard Deviation = %f\n", average5, stddev5);
  printf("Average p6 = %f Standard Deviation = %f\n", average6, stddev6);
  printf("Average p7 = %f Standard Deviation = %f\n", average7, stddev7);
  
  fclose (in);
  fclose (out);

  return 0;
}
  
