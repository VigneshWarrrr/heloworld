#include <stdio.h>

int main()
{
  int side1,side2,side3;
  scanf("%d,%d,%d",&side1,&side2,&side3);
  if((side1+side2>side3)&&(side1+side3>side2)&&(side2+side3>side1)){
    printf("Valid\n");
  }
  else{
    printf("Not Valid\n");
  }
  return 0;
}