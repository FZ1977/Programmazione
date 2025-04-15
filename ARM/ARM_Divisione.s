.global _start
	.data
		.equ x, 5 //valore del dividendo
		.equ y, 2 //valore del divisore
		.equ c, 0 //contatore
	.text
_start:
		MOV R0, #x
		MOV R1, #y
		MOV R2, #c
while:	CMP R1, #0
		BLE fine
		CMP R0, R1
		BLT fine
		SUB R0, R0, R1
		ADD R2, R2, #1
		B while
fine:	.end