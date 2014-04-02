#include <stdio.h>
#include <sched.h>
#include <sys/types.h>
#include <unistd.h>
#include "employee.h"
#define LOWER 0
#define UPPER 300
#define SETP 20

void main(int argc, char *argv[]) {	
      
	int eof = EOF;
 
	imprime_saludo();
	printf('\n');
	printf("%d",eof);

}
