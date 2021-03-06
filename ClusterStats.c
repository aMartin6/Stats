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
  int start = 200;
  int end = 600000;
  int count;
  double sum = 0.0;
  double average;
  double stddev1;
  int clump = 0;
  int trash;
  int particle_number = 0;
  int total_particles = 2160;

  //open drive data file
  if ((in = fopen("bigcluster.dat", "r")) == NULL)
    {
      printf("Input file fxtest_1_big.csv not found \n");
      exit(-1);
    }
   //open drive data file
  if ((out = fopen("../../cluster_stats.txt", "a")) == NULL)
    {
      printf("Output file cluster_stats.txt not found \n");
      exit(-1);
    }
  
  //else printf("Reading file \n");
  //fflush(stdout);

  //printf("Start value = %d, End value = %d\n", start, end);
  
  //Calcualte sum within range
  while (!feof(in) && count <= end)
  {
    fscanf(in, "%d %d\n", &trash, &clump);
    if (count > 0 && count >= start)
      {
	sum += clump;
	particle_number += 1;
      }
    count += 1;
  }

  //Calculate average
  average = sum / particle_number;
  printf("Average Cluster Size = %lf\n", average);

  count = 0;
  sum = 0;
  particle_number = 0;
  rewind(in);

  //Calculate standard deviation
  while (!feof(in) && count <= end)
  {
    fscanf(in, "%d %d\n", &trash, &clump);
    if (count > 0 && count >= start)
      {
	sum += (clump - average)*(clump - average);
	particle_number += 1;
      }
    count += 1;
  }

  stddev1 = sqrt(sum / (particle_number - 2)); // Count - 2 = number of data points - 1
  printf("Standard Deviation = %lf\n", stddev1);
  
  average = average / total_particles;
  stddev1 = stddev1 / total_particles;
  
  fprintf(out, "%f ", average);
  fprintf(out, "%f\n", stddev1);
  fclose (in);
  fclose (out);

  return 0;
}
  
