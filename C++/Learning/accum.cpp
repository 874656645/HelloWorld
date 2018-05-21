#include<iostream>
#include<vector>
#include<numeric>
#include<functional>

using namespace std;

#define MAX 10

int main(int argc, char const *argv[])
{
    vector<long> v(MAX);

    for(size_t i = 0; i < MAX; i++)
    {
        v.push_back(i+1);
    }

    long sum = accumulate(v.begin(), v.end(), 0);
    cout << "v sum = " << sum << '\n';

    long product = accumulate(v.begin(), v.end(), 1l, multiplies<long>());
    cout << "product = " << product << '\n';

    system("pause");

    return 0;
}
