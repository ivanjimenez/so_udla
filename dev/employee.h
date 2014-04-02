#define LOWER 0
#define UPPER 300
#define STEP 20
void imprime_saludo (){
     printf("Ciao\n");
}

struct Employee {
	char *name;
	int DNI;
        float salary, tax_to_date;
};

struct Employee secretary;
secretary.name = "Miss Paper";
printf("Secrataria: %s\n", secretary.name);
