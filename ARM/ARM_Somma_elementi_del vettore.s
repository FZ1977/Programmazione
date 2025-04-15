.global _start
_start:
	
v: .word 3,2,5,6

ldr r0, =v //punto al primo elemento del vettore
ldr r2, [r0] //carico il valore del primo elemento del vettore
mov r3, #0 //puntatore alla fine del vettore
add r3, r2, lsl #2 
mov r1, #4 //indice
mov r4, #0 //somma dei termini
while:
cmp r1,r3
bgt fine
ldr r2, [r0, r1]
add r4, r4, r2 //calcolo la somma dei valori
add r1, r1, #4 //incremento il valore dell'indice
b while
fine:
.end