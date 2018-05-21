using System;

namespace C_
{
    class Program
    {
        public static void RefValue(ref int refInt, ref int rInt)
        {
            refInt += 100;
            rInt = 90;
        }

        public static void OutValue(out int outInt, out int i)
        {
            i = 50;
            outInt = i + 100;
        }
        static void Main(string[] args)
        {
            int refInt = 100, refI = 0;

            RefValue(ref refInt, ref refI);

            Console.WriteLine("refInt = {0}, refI = {1}", refInt, refI);

            int outInt = 100, outI = 100;
            OutValue(out outInt, out outI);
            Console.WriteLine("outInt = {0}, outI = {1}", outInt, outI);

            Console.WriteLine("Hello C#!");
        }

        
    }
}
