#include <stdio.h>
#include <signal.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>


int main() {

	for (;;) {
		if(!fork()) {exit(0);}
		sleep(1);

	}
	return 0;
}
