#include<iostream>
#include<list>
#include<algorithm>
#include<functional>

using namespace std;

int main(int argc, char const *argv[])
{
    int iArray[] = {1,2,3,4,5,6,7,8,9,0};
    list<int> iList(iArray, iArray + 10);

    // std::bind1st
    // std::bind2nd
    int k = count_if(iList.begin(), iList.end(), bind1st(greater<int>(), 8));

    cout << "Number elements < 8 = " << k << endl;

    // typedef 别名
    typedef int INT_ARRAY_10[10];
    INT_ARRAY_10 a;
    cout << sizeof(a) << endl;

    system("pause");

    return 0;
}
