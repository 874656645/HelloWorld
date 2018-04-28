#include<stdio.h>

typedef struct X
{
    char a;
    double b;
    int c;
}x;

void change(int* a, int &b, int c)
{
    c = *a;
    b = 3;
    *a = 2;
}

int main()
{
    int d[] = {1,2,3,4,5};
    int *ptr;
    ptr = (int*)(&d + 1);
    printf("%5d%5d\n", *(d + 1), *(ptr - 1));

    int a = 1, b = 2, c = 3;
    change(a, b, c);
    printf("%5d%5d%5d\n", a, b, c);
    printf("%5d%5d%5d\n", sizeof(d), sizeof(d[1]), sizeof(X));
    
    // printf("Hello World");

    char r;
    cin >> r;
    return 0;
}