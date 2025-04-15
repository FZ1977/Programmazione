.data
	.equ n, 10
	.equ i, 0
.text
.global main
main:
		MOV R0, #n
		MOV R1, #i
while:	CMP R0, #0
		BLT fine
		ADD R1, R1, R0
		SUB R0, R0, #1
		B while
fine: .end	