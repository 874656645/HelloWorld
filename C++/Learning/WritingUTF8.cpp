#include<windows.h>

std::string to_utf8(const wchar_t* buffer, int len)
{
    int nChars = ::WideCharToMultiByte(CP_UTF8, 0, buffer, len, NULL, 0, NULL, NULL);
    
    if (nChars == 0) {
        return "";
    }

    string newBuffer;
    newBuffer.resize(nChars);
    ::WideCharToMultiByte(
        CP_UTF8, 
        0, 
        buffer, 
        len, 
        const_cast<char*>(newBuffer.c_str()),
         nChars, 
         NULL,
         NULL);

    return newBuffer;
}

string to_utf8(const wstring & str)
{
    return to_utf8(str.c_str(), (int)str.size());
}

int main(int argc, char const *argv[])
{
    ofstream outfile;
    outfile.open("D://test.xml", ios::out | ios::binary);
    wstring text =
                L"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
                L"<root description=\"this is a naïve example\">\n</root>";

    string outtext = to_utf8(text);

    outfile << outtext;

    outfile.close();

    system("pause");
    return 1;
}
