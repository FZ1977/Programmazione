#include <stdio.h>
#include <stdlib.h>

struct array_int {
    int *a;
    int n;
};

typedef struct array_int array_int;

array_int posizione_vocali(char *s);

int main(){
    char *s="Algoritmi";
    array_int res;
    res=posizione_vocali(s);

    for(int i=0; i<res.n; i++){
        printf("%d ",res.a[i]);
    }

    return 0;
}

array_int posizione_vocali(char *s){
    array_int x;
    int i=0; //indice che scorre la stringa
    int j=0; //indice dell'array di interi
    x.n=0;

    //Conto il numero di vocali
    while(s[i]!='\0'){
        if(s[i]=='a' || s[i]=='A' || s[i]=='e' || s[i]=='E' || s[i]=='i' || s[i]=='I' || s[i]=='o' || s[i]=='O' || s[i]=='u' || s[i]=='U'){
            x.n++;
        }
        i++;
    }

    i=0;
    //Istanzio l'array
    x.a = malloc(x.n*sizeof(int));
    //Inseri gli indici nell'array
    while(s[i]!='\0'){
        if(s[i]=='a' || s[i]=='A' || s[i]=='e' || s[i]=='E' || s[i]=='i' || s[i]=='I' || s[i]=='o' || s[i]=='O' || s[i]=='u' || s[i]=='U'){
            x.a[j]=i;
            j++;
        }
        i++;
    }
    //Il costo computazionale è pari a Teta(2n)
    //Il costo in termini di memoria supplementare è O(n) perchè la stringa potrebbe essere composta solo da stringhe
    return x;
}