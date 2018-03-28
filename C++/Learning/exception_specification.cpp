// compile with:/EHs

#include<stdio.h>

void handler()
{
    printf("in handler\n");
}

void f1(void) throw(int)
{
    printf("About to throw 1\n");
    if(1)
    {
        throw 1;
    }
}

void f5(void) throw()
{
    try
    {
        f1();
    }
    catch(...)
    {
        handler();
    }
}

// invalid, doesn't handle the int exception thrown from f1()  
// void f3(void) throw() {  
//   f1();  
// }  

// nothrow:说明f2函数没有异常抛出，如果有异常抛出，程序会强制终结
// This application has requested the Runtime to terminate it in an unusual way.
// Please contact the application's support team for more information.
// About to throw 1
// terminate called after throwing an instance of 'int'
void __declspec(nothrow) f2(void) {  
   try {  
      f1();  
   }  
   catch(int) {  
      handler();
      //throw 1;  
    }  
}  
  
// only valid if compiled without /EHc   
// /EHc means assume extern "C" functions don't throw exceptions  
extern "C" void f4(void);  
void f4(void) {  
   f1();  
}  
  
int main() {  
    
    f2();

   try {  
      f4();  
   }  
   catch(...) {  
      printf("Caught exception from f4\n");  
   }  
   f5();  
}  
