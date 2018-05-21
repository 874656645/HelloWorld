#include<iostream>
#include<vector>
#include<list>

using namespace std;

template <class T>
void Display(vector<T> &v, const char* s)
{
    cout << s << '\n';
    copy(v.begin(), v.end(), ostream_iterator<T>(cout, "\t"));
    cout << endl;
}

template <class T>
void Display(list<T> &lst, const char* s)
{
    cout << s << '\n';
    copy(lst.begin(), lst.end(), ostream_iterator<T>(cout, "\t"));
    cout << endl;
}