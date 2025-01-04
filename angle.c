#include <stdio.h>

int main()
{
  int a1,a2,a3;
  scanf("%d,%d,%d",&a1,&a2,&a3);
  if(a1+a2+a3==180){
    printf("Valid");
  }
  else{
    printf("Not Valid");
  }
  return 0;
}