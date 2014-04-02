#include <time.h> #include <stdlib.h> #include <stdio.h> #include <math.h>
#define N 1000
float first[N], second[N], result[N]; int i, j, interations = 1000;
clock_t start, end, elapsed;
void main ()
{ for (i=0; i<N; i++) /* initialize */ { first[i] = random();
	second[i] = random(); }
	start = clock (); /* start timer */ for (i=0; i<interations ; i++)
		for (j=0; j < N; j++)
			result[j] = first[j] * second[j];
	end = clock ();
	printf ("Timing Ended.\n\n");
	elapsed = end - start;
	printf ("Time : %fs\n",(float)(elapsed)/CLOCKS_PER_SEC);
}
