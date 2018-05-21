#include<iostream>
#include<vector>

using namespace std;

char * strCpy(char * strDest, const char* strSrc){
    
    if (strDest == NULL || strSrc == NULL) {
        return NULL;
    }
    
    char * strDestCopy = strDest;
    while((*strDest++ = *strSrc++) != '\0');
    *strDest = '\0';

    return strDestCopy; 
}

int main(int argc, char const *argv[])
{
    string strSrc = "abc123";

    char strDest[20];
    char * strCopy = strCpy(strDest, strSrc.c_str());
   
    cout << strCopy << endl;

    char a;
    cin >> a;
    
    return 0;
}


