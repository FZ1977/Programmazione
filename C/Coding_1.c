#include <stdio.h>
#include <stdlib.h>

int *x_array( int *a, int na, int *b, int nb );

int main(){
    int a[] = {1, 2, 3};
    int b[] = {10, 20, 30, 40};
    int *p;

    p=x_array(a, 3, b, 4);

    for(int i=0; i<12; i++){
        printf("%d ",p[i]);
    }

    return 0;
}

int *x_array( int *a, int na, int *b, int nb ){
    int *array;
    int i=0;
    
    array=calloc(na*nb,sizeof(int));

    for(int r=0; r<na; r++){
        for(int c=0; c<nb; c++){
            array[i]=a[r]*b[c];
            i++;
        }
    }

    return array;
}