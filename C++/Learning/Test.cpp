#include<iostream>
#include<iterator>
#include<vector>
#include<list>
#include<string.h>
#include<iomanip>
#include<algorithm>
#include"Display.h"

using namespace std;

#define SIZE_NUM 100

int iArray[] = {1,2,3,4,5,6,7,8,9,0};


int main(int argc, char const *argv[])
{
    // cout << "Hello World!" << endl;
    // cout << setw(10) << setfill('*') << 'a' << endl;
    // cout << setw(10) << setfill('*') << '\n';
    // cout << "Hello World!" << endl;
    
    // char buf[10];
    // size_t i = sizeof(buf);
    // cout << i << endl;
    // memset(buf, 0, i);
    // strncat(buf, "123456789abc", 8);
    // cout << buf << endl;

    // vector<int> myVet(SIZE_NUM);
    // myVet[20] = 50;
    // vector<int>::iterator res = find(myVet.begin(), myVet.end(), 50);
    // if (res != myVet.end()) {
    //     cout << *res << " were finded." << endl;
    //     *res = 100;
    //     cout << *res << endl;
    // }


    /* vector copy*/
    // vector<int> myVet;
    // vector<int>::iterator out_it = myVet.begin();
    // copy(iArray, iArray + 10, out_it);
    // while(out_it != myVet.end()){
    //     cout << *out_it << endl;
    //     ++out_it;
    // }

    /* vector reverse */
    // reverse(myVet.begin(), myVet.end());
    // out_it = myVet.begin();
    // while(out_it != myVet.end()){
    //     cout << *out_it << endl;
    //     ++out_it;
    // }

    /*random_shuffle*/
    // Display(myVet, "before shuffle");
    // random_shuffle(myVet.begin(), myVet.end());
    // Display(myVet, "after shuffle");

    // vector<double> dMyVet = {1.1, 2.2, 3.3, 4.4, 5.5};
    // Display(dMyVet, "double Vector");

    /* list */
    // list<int> iList;
    // copy(iArray, iArray + sizeof(iArray) / sizeof(int), front_inserter(iList));
    // Display(iList, "List");

    // list<int>::iterator p = find(iList.begin(), iList.end(), 9);
    // cout << "before: p = " << *p << endl;
    // list<int>::iterator p1 = p;
    // advance(p1, 3);
    // cout << "after: p = " << *p1 << endl;

    // int k = distance(p, p1);
    // cout << "distance = " << k << endl;

    long int result = 1;
    for(int i = 1; i < 11; i++){
        result *= i;
    }
    cout << result;


    system("pause");

    return 0;
}


