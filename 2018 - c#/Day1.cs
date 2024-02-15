using System;
using System.IO;
using System.Linq;


namespace FirstTest
{
    public class Day1
    {

        // public const bool UseTestData = false;
        public readonly string[] InputData = null!;

        public Day1()
        {
            InputData = File.ReadAllLines(@"c:\Users\arvid\repo\csharp\FirstTest\input.txt");
            Console.WriteLine(PartA());
            Console.WriteLine(PartB());
        }

        private int PartA()
        {
            int[] intArray = InputData.Select(int.Parse).ToArray();
            return intArray.Sum();
        }

        private int PartB()
        {
            // int[] intArray = new int[] {1, -1};
            int[] intArray = InputData.Select(int.Parse).ToArray();
            List<int> intSumArray = new List<int> {0};
            int sumSoFar = 0;
            int i = 0;
            while (true)
            {
                Console.WriteLine("" + i + " " + sumSoFar);
                sumSoFar += intArray[i % intArray.Length];
                // Check if sumSoFar already exists in intSumArray
                if (intSumArray.Contains(sumSoFar))
                {
                    return sumSoFar;
                }

                intSumArray.Add(sumSoFar);
                i++;
            }
        }
    }
}
