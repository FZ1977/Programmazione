#include <stdio.h>
#include <stdlib.h>

struct int_array {
    int dim;
    int *v;
};

typedef struct int_array int_array;

int_array pos_max(float *a, int n);

int main(){
    int_array res;
    float a[]={3.14,2.71,1.1,0.5,3.14,2.71};
    res=pos_max(a,6);

    for(int i=0; i<res.dim; i++){
        printf("%d ",res.v[i]);
    }

    return 0;
}

int_array pos_max(float *a, int n){
    int_array x;
    int i=0; //indice per l'array di float
    int j=0; //indice per l'array degli indici
    float massimo=0;
    x.dim=0;

    //cerco il massimo valore
    for(i=0; i<n; i++){
        if(a[i]>massimo){
            massimo = a[i];
        }
    }

    //conto i massimi contenuto nell'array dato
    for(i=0; i<n; i++){
        if(a[i]==massimo){
            x.dim++;
        }
    }

    //creo l'array di interi per gli indici che contengono il massimo
    x.v = malloc(x.dim*sizeof(int));

    //inserisco il valore degli indici dei massimi nell'array di interi
    for(i=0; i<n; i++){
        if(a[i]==massimo){
            x.v[j]=i;
            j++;
        }
    }

    return x;
}

//Il costo computazionale dell'algoritmo Teta(3n)
//Il costo in termini di memoria corrisponde a O(n)