#include <iostream>

using namespace std;

typedef struct X
{
    char a;     // 1 byte，7 padding bytes
    double b;   // 8 bytes
    int c;      // 4 bytes， 4 padding bytes
}x;

void change(int* a, int &b, int c)
{
    c = *a;
    b = 3;
    *a = 2;
}

int main()
{
    int d[] = {1,2,3,4,6};
    int *ptr;
    ptr = (int*)(&d + 1);   // 数组名和数组名取地址的区别
    printf("%5d%5d\n", *(d + 1), *(ptr - 1));

    int a = 1, b = 2, c = 3;
    change(&a, b, c);
    printf("%5d%5d%5d\n", a, b, c);
    printf("%5d%5d%5d\n", sizeof(d), sizeof(d[1]), sizeof(X));
    
    // printf("Hello World");

    return 0;
}