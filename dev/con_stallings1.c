#include <stdio.h>
int chin;
int chout;

void echo() {

	chin = getchar();
	chout = chin;
	putchar(chout);
	printf("\n");
}

int main() {

	echo();


}
