#include <stdio.h>
#include <stdlib.h>


char *str_cat(char *a, int n, char *b);

int main(){
    char *a="Programmazione";
    char *b=" degli Elaboratori";
    int n=14;
    int i=0;

    char *p;

    printf("Prima\n");
    while(a[i]!='\0'){
        printf("%c",a[i]);
        i++;
    }

    printf("\n");

    a=str_cat(a,n,b);
    p=a;

    i=0;
    printf("Dopo\n");
    while(a[i]!='\0'){
        printf("%c",a[i]);
        i++;
    }

    printf("\n");

    return 0;
}

char *str_cat(char *a, int n, char *b){
    int conta_b=0;
    int i=0;
    int j=0;
    char *p;

    //conto i caratteri di b
    while(b[i]!='\0'){
        conta_b++;
        i++;
    }

    //ora ridimensiono a
    p=malloc( (n+conta_b+1)*sizeof(char) );
    i=0;
    
    //concateno b ad a
    while(a[j]!='\0'){
        p[i]=a[j];
        i++;
        j++;
    }
    j=0;
    while(b[j]!='\0'){
        p[i]=b[j];
        i++;
        j++;
    }

    //inserisco la chiusura
    p[i]='\0';

    return p;
}