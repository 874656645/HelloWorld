#include<iostream>
#include<stdexcept>

using namespace std;
int main()
{
    int x;
    while(cin >> x)
    {
        if(x == 0)
        {
            throw runtime_error("input a 0...");
            return 1;
        }
    }
    return 0;
}