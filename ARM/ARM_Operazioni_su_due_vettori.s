.global _start
_start:
	
v: .word 3,2,5,6
w: .word 3,5,6,7
z: .word 3,0,0,0

ldr r0,=v
ldr r2,=w
ldr r3,=z

mov r1,#4

ldr r4,[r0]
ldr r5,[r2]
mov r6,#0
mov r7,#0

cmp r4,r5
bne fine

add r7, r4, lsl #2

mov r8,#0

while:
cmp r1,r7
bgt fine
ldr r4,[r0,r1]
ldr r5,[r2,r1]
mul r8,r4,r5
add r6,r6,r8
str r6,[r3,r1]
add r1,r1,#4
b while
fine:
.end