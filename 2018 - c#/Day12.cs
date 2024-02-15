using System;
using System.Formats.Asn1;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text.RegularExpressions;

namespace FirstTest
{
    public class Day12
    {

        public readonly string[] InputData = null!;
        public string State = "";
        public long Origin = 0;
        public HashSet<string> Transitions = new();
        // public List<(string str, char c)> Transitions = new();

        public Day12()
        {
            InputData = File.ReadAllLines(@"c:\Users\arvid\repo\csharp\FirstTest\input.txt");

            Populate();
            
            Console.WriteLine(PartA());
            // Console.WriteLine(PartB());
        }

        private void Populate()
        {
            State = "...." + InputData[0][15..] + "....";
            Origin = 4;
            foreach (var str in InputData[2..].Where(x => x.Last() == '#'))
            {
                Transitions.Add(str[0..5]);
            }
            Console.WriteLine(State);
        }

        private void NullPadState()
        {
            // If the plants have grown into the forth pot, we have to add empty pots.
            if (State[0..5] == ".....")
            {
                State = State.Substring(1);
                Origin--;
            }
            if (State[3] == '#')
            {
                State = "." + State;
                Origin++;
            }

            if (State[State.Length - 4] == '#')
            {
                State += ".";
            }
            
        }

        public long PartA() 
        {
            foreach (int gen in Enumerable.Range(0, 120))
            {
                NullPadState();
                Console.WriteLine("Gen " + gen + ": " + Origin + " " + State);
                string newState = "..";

                // First and last 2 characters are not viable for analysis
                foreach (int midIdx in Enumerable.Range(0, State.Length))
                {
                    if (midIdx - 2 < 0 || midIdx + 2 >= State.Length) continue;
                    string substring = State.Substring(midIdx - 2, 5);
                    newState += Transitions.Contains(substring) ? "#" : ".";
                }
                newState += "..";

                State = newState;
            }
            Console.WriteLine("Gen " + 20 + ": " + Origin + " " + State);
            
            // After 120 generations, it reaches a semi-static solution, where the only change is Origin decreasing with every step.
            // For every step not calculated, decrease Origin by one
            Origin -= 50000000000 - 120;

            long sum = 0;
            foreach(int idx in Enumerable.Range(0, State.Length))
            {
                if (State[idx] == '#')
                    sum += idx - Origin;
            }



            return sum;
        }



        public int PartB()
        {
            return 0;
        }
    }
}
