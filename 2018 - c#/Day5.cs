using System;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;

namespace FirstTest
{
    public class Day5
    {

        // public const bool UseTestData = false;
        public readonly string[] InputData = null!;
        public List<string> m_letterComboList = new();
        public Day5()
        {
            InputData = File.ReadAllLines(@"c:\Users\arvid\repo\csharp\FirstTest\input.txt");
            // Console.WriteLine(PartA());
            // Console.WriteLine(PartB());
            PartB();

        }

        private int PartA()
        {
            var inputWord = InputData[0];
            Stack<char> stack = new Stack<char>();
            int caseDiff = 'a' - 'A';

            foreach (char c in inputWord)
            {
                if (stack.Count > 0 && Math.Abs(stack.Peek() - c) == caseDiff)
                {
                    stack.Pop();
                }
                else
                {
                    stack.Push(c);
                }
            }

            return stack.Count;
        }

        private void PartB()
        {
            var inputWord = InputData[0];
            int caseDiff = 'a' - 'A';

            for (char C = 'A'; C <= 'Z'; C++)
            {
                Stack<char> stack = new Stack<char>();
    
                // Remove all instances of C from inputWord
                string tmpInputWord = new(inputWord.Where(c => (c != C && c != C + caseDiff)).ToArray());

                foreach (char c in tmpInputWord)
                {
                    if (stack.Count > 0 && Math.Abs(stack.Peek() - c) == caseDiff)
                    {
                        stack.Pop();
                    }
                    else
                    {
                        stack.Push(c);
                    }
                }

                Console.WriteLine(C + " " + stack.Count);
            }
        }
    }
}
