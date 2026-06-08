.DATA
    A:.WORD 10,20,30,40,50

.TEXT
    LDR R1,=A  //R1 is like a pointer pointing to the first element or first address block
    LDR R0,[R1] //INitiall set first element as the largest element

    MOV R3,#0;

LOOP:
    LDR R2,[R1,#4]! //LOAD THE NXT ELEMNT
    CMP R0,R2 //DO R0-R2 IF IT IS NEGATIVE IT MEANS R2>R0 SO GO TO BRANCH Less

    Blt Less

L1:
    ADD R3,R3,#1
    CMP R3,#4
    bne LOOP
    B EXIT

Less:
    MOV R0,R2
    B L1

EXIT:
    SWI 0X011