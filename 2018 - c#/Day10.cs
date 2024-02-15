using System;
using System.Formats.Asn1;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text.RegularExpressions;

namespace FirstTest
{
    public class Day10
    {

        public struct Elf
        {
            public int xc, yc, xv, yv;
            public Elf(Match match)
            {
                var dataAsList = match.Groups;
                this.xc = int.Parse(match.Groups[1].Value);
                this.yc = int.Parse(match.Groups[2].Value);
                this.xv = int.Parse(match.Groups[3].Value);
                this.yv = int.Parse(match.Groups[4].Value);
            }

            public void Step()
            {
                this.xc += this.xv;
                this.yc += this.yv;
            }
        }
        

        public string RegexString = @"position=<\s*(-?\d+),\s*(-?\d+)> velocity=<\s*(-?\d+),\s*(-?\d+)";
        public readonly string[] InputData = null!;
        public List<Elf> elves = new();

        public Day10()
        {
            InputData = File.ReadAllLines(@"c:\Users\arvid\repo\csharp\FirstTest\input.txt");
            
            foreach (var line in InputData)
            {
                elves.Add(new Elf(Regex.Match(line, RegexString)));
            }

            Console.WriteLine(PartA());
            // Console.WriteLine(PartB());
        }

        public void DrawElves()
        {
            int x_max = elves.Select(e => e.xc).Aggregate((max, next) => Math.Max(max, next));
            int y_max = elves.Select(e => e.yc).Aggregate((max, next) => Math.Max(max, next));
            int x_min = elves.Select(e => e.xc).Aggregate((max, next) => Math.Min(max, next));
            int y_min = elves.Select(e => e.yc).Aggregate((max, next) => Math.Min(max, next));

            if (y_max - y_min > 12) return;
            List<List<char>> chars = new List<List<char>>();
            for (int i = 0; i < y_max - y_min + 1; i++)
            {
                chars.Add(new List<char>(Enumerable.Repeat('.', x_max - x_min + 1)));
            }

            foreach(var elf in elves)
            {
                chars[elf.yc - y_min][elf.xc - x_min] = '#';
            }

            foreach (List<char> innerList in chars)
            {
                Console.WriteLine(string.Join("", innerList));
            }
            Console.WriteLine("\n");
            
        }
        private int PartA()
        {
            for (int step = 1; true; step++)
            {
                for (int i = 0; i < elves.Count; i++)
                {
                    var elf = elves[i];
                    elf.Step();
                    elves[i] = elf;
                }
                DrawElves();
            }
            return 0;
        }

        private int PartB()
        {
            return 0;
        }
    }
}
