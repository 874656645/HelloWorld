#include<iostream>

using namespace std;

void swap(int * a, int * b)
{
    // int * temp = a;
    // a = b;
    // b = temp;

    int temp = *a;
    *a = *b;
    *b = temp;
}

void swap(int & a, int & b)
{
    // int * temp = a;
    // a = b;
    // b = temp;

    int temp = a;
    a = b;
    b = temp;
}

int main(int argc, char const *argv[])
{
    /* code */
    int a = 1, b = 2;
    swap(a, b);
    cout << a << '\t' << b << endl;
    
    system("pause");
    //return 0;
}

