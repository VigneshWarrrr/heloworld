#include <stdio.h>

int main()
{
  int num1,num2,result;
  char oper;
  scanf("%d%c%d",&num1, &oper, &num2);
  switch(oper)
  {
    case'+':
     result=num1+num2;
     break;
    case'-':
     result=num1-num2;
     break;
    case'*':
     result=num1*num2;
     break;
    case '/':
     if (num2!=0){
       result=num1/num2;
     }
     else{
       printf("Division by zero not allowed\n");
       return 1;
     }
     break;
    default:
     printf("Invalid\n");
     return 1;
  }
  printf("%d",result);
  return 0;
}