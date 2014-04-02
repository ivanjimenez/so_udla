#include <stdio.h>
#include <stdarg.h>

int main (int argc, char **argv) {
	
	char buffer[512];
	char* path = "/bin/";

	while(1) {
		
		printf("/myShell>");
		fgets(buffer, 512, stdin);

		int pid = fork();
		if (pid!=0) {
		
			wait(NULL);
		}
		else {

			int num_of_args = countArgs(buffer);
			char *arguments[num_of_args + 1];
			parse(buffer, num_of_args, arguments);
			arguments[num_of_args] = NULL;
			char prog[512];
			strcpy(prog, path);
			strcat(prog, arguments[0]);
			int rv = execv(prog, arguments);
		}
	}
	return 0;
}
