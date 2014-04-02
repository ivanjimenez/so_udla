#include <stdio.h>

main () {
	
	int temp;
	int celsius = 0;
	
	printf("Fahrenheit\t");	
	printf("Celsius \n");

	for(temp=0; temp <= 300; temp=temp + 20) {
	       printf("%d\t",temp);	
	       celsius = (5 * (temp - 32)) / 9;
	       printf("%d\n",celsius);
	}

}

