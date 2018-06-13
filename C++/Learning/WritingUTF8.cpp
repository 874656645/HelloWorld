#include<windows.h>

std::string to_utf8(const wchar_t* buffer, int len)
{
    int nChars = ::WideCharToMultiByte(CP_UTF8, 0, buffer, len, NULL, 0, NULL, NULL);
    
    if (nChars == 0) {
        return "";
    }

    string newBuffer;
    
}