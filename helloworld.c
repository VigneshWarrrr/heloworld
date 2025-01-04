#include <stdio.h>

int main()
{
    int a;
    printf("Enter the number");
    scanf("%d",&a);
    if (a%3==0 && a%5==0){
        printf("Hello");
    }
    else if (a%3==0 && a%5!=0)
    {
        printf("HiHello");
    }
    else if(a%3!=0 && a%5==0){
        printf("Hi");
    }x`
    return 0;
}       