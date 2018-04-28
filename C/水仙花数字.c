#include <stdio.h>
int main()
{
    int num, hd, td, sd;
    for(num = 100; num < 1000; num++)
    {
        hd = num / 100;
        td = (num % 100) / 10;
        sd = num % 10;
        if(num == hd * hd * hd + td * td * td + sd * sd * sd)
        {
            printf("水仙花数字：%d\n", num);
        }
    }

    return 0;
}