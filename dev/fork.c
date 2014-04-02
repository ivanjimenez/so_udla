#include <unistd.h> 
#include <stdio.h> 
void main(void){ 
 	int i=0; 
	 if (MIFORK()==0){ 
 		i=1; 
	 if (MIFORK()!=0) 
 		i=2; 
 	else 
 		i=3; 
 	} 
 	else 
	 printf("%d\n", i); 
} 
