#include<iostream>
#include<fstream>
#include<memory.h>

using namespace std;

void file_wr(void)
{
    char data[100];

    // 向文件中写数据
    ofstream outFile;
    outFile.open("D://test.txt");
    
    if (!outFile) {
        cout << "没有打开文件" << endl;
    }

    cout << "write to file" << endl;
    cout << "enter your name:" << endl;
    cin.getline(data, 100);
    outFile << data << endl;
    cout << "enter your age:" << endl;
    cin >> data;
    cin.ignore();
    outFile << data << endl;

    outFile.close();

    // 从文件读取数据
    ifstream infile;
    infile.open("D://test.txt");
    cout << "read from the file" << endl;
    infile >> data;
    cout << data << endl;

    infile.close();
}

void file_copy(void)
{
    char data[100];
    ifstream infile;
    ofstream outfile;
    infile.open("D://test.txt");
    outfile.open("D://ttt.mod");
    cout << "copy from test.txt to ttt.mod" << endl;
    
    // 如果结尾有空行，无法读出数据
    while(!infile.eof()){
        // 置空数组
        memset(data, 0, sizeof(data));
        infile >> data;
        cout << data << endl;
        outfile << data << endl;
    }

    infile.close();
    outfile.close();
    
}

int main(int argc, char const *argv[])
{
    file_wr();
    // file_copy();
    system("pause");
    return 0;
}
