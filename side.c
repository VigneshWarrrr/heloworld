#include <stdio.h>

int main()
{
  float s1,s2,s3;
  scanf("%f,%f,%f",&s1,&s2,&s3);
  if (s1==s2&&s2==s3){
    printf("Equilateral");
  }
  else if(s1==s2||s2==s3||s1==s3){
    printf("Isosceles");
  }
  else{
    printf("Scalene\n");
  }
  return 0;
}