using System;
using System.IO;
using System.Linq;


namespace FirstTest
{
    public class Day2
    {

        // public const bool UseTestData = false;
        public readonly string[] InputData = null!;

        public Day2()
        {
            InputData = File.ReadAllLines(@"c:\Users\arvid\repo\csharp\FirstTest\input.txt");
            Console.WriteLine(PartA());
            Console.WriteLine(PartB());
        }

        private bool containsOcc(string word, int number)
        {
            int[] charCount = word.GroupBy(c => c).Select(c => c.Count()).ToArray();
            return charCount.Contains(number);
        }
        static int CountDifferences(string a, string b)
        {
            int count = 0;
            for (int i = 0; i < a.Length; i++)
            {
                if (a[i] != b[i])
                {
                    count++;
                }
            }
            return count;
        }

        private int PartA()
        {
            int noOfDoubles = 0;
            int noOfTriples = 0;

            foreach (string str in InputData)
            {
                noOfDoubles += containsOcc(str, 2) ? 1 : 0;
                noOfTriples += containsOcc(str, 3) ? 1 : 0;
            } 

            return noOfDoubles * noOfTriples;
        }

        private string PartB()
        {
            string returnValue = "";
            string finalWord1 = "";
            string finalWord2 = "";
            
            Parallel.ForEach(InputData, (word1, loopState) =>
            {
                for (int i = 0; i < InputData.Length; i++)
                {
                    if (returnValue != "") return;

                    string word2 = InputData[i];
                    if (word1 == word2) continue;

                    if (CountDifferences(word1, word2) == 1)
                    {
                        returnValue = $"Found a pair: {word1}, {word2}";
                        finalWord1 = word1;
                        finalWord2 = word2;
                        loopState.Stop();
                    }
                }
            });

            string result = new string(finalWord1.Zip(finalWord2, (c1, c2) => c1 == c2 ? c1 : ' ').ToArray());
            result = new string(result.Where(c => c != ' ').ToArray());

            Console.WriteLine(returnValue);
            return result;
        }
    }
}
