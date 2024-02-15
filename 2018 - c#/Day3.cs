using System;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;

namespace FirstTest
{
    public class Day3
    {

        // public const bool UseTestData = false;
        public readonly string[] InputData = null!;
        public string RegexString = @"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)";

        public Day3()
        {
            InputData = File.ReadAllLines(@"c:\Users\arvid\repo\csharp\FirstTest\input.txt");
            // Console.WriteLine(PartA());
            Console.WriteLine(PartB());
        }

        private List<(int, int)>  GetCoordinateList(List<int> data)
        {
            List<(int, int)> coordinates = new();
            int x_0 = data[1];
            int y_0 = data[2];
            int width = data[3];
            int height = data[4];

            var x_coords = Enumerable.Range(x_0, width);
            var all_coords = x_coords.SelectMany(
                x => {
                    // This is what the first lambda does
                    var colNumbers = Enumerable.Range(y_0, height);
                    return colNumbers;
                },
                (x, y) => (x, y))
                .ToList();
            return all_coords;


        }

        private List<int> ExtractData(string claim)
        {
            Match match = Regex.Match(claim, RegexString);

            if (!match.Success) Console.WriteLine("No match found.");

            List<int> values = match.Groups
                                .Cast<Group>()
                                .Skip(1) // Skip the full match
                                .Select(g => int.Parse(g.Value))
                                .ToList();
            return values;
            
        }

        private int PartA()
        {
            HashSet<(int, int)> takenOnce = new();
            HashSet<(int, int)> takenTwice = new();

            foreach (var claim in InputData)
            {
                // Extract relevant information
                List<int> claimData = ExtractData(claim);
                Console.WriteLine(claimData[0]);

                // Calculate a list of all coordinates in claim
                List<(int, int)> coordList = GetCoordinateList(claimData);

                // Add to either takenOnce or takenTwice
                foreach (var coord in coordList)
                {
                    if (takenTwice.Contains(coord)) continue;
                    if (!takenOnce.Add(coord))
                    {
                        // Add returns false if the item is already present, which
                        // means it needs to move to takenTwice
                        takenTwice.Add(coord);
                    }
                }
            }
            // Console.WriteLine(string.Join(',', takenTwice) + '\n');

            return takenTwice.Count;
        }

        private int PartB()
        {
            HashSet<(int, int)> takenOnce = new();
            HashSet<(int, int)> takenTwice = new();

            foreach (var claim in InputData)
            {
                // Extract relevant information
                List<int> claimData = ExtractData(claim);
                Console.WriteLine(claimData[0]);

                // Calculate a list of all coordinates in claim
                List<(int, int)> coordList = GetCoordinateList(claimData);

                // Add to either takenOnce or takenTwice
                foreach (var coord in coordList)
                {
                    if (takenTwice.Contains(coord)) continue;
                    if (!takenOnce.Add(coord))
                    {
                        // Add returns false if the item is already present, which
                        // means it needs to move to takenTwice
                        takenTwice.Add(coord);
                    }
                }
            }            

            foreach (var claim in InputData)
            {
                // Extract relevant information
                List<int> claimData = ExtractData(claim);
                Console.WriteLine(claimData[0]);

                // Calculate a list of all coordinates in claim
                List<(int, int)> coordList = GetCoordinateList(claimData);

                // Add to either takenOnce or takenTwice
                bool uniqueClaim = true;
                foreach (var coord in coordList)
                {
                    if (takenTwice.Contains(coord))
                    {
                        uniqueClaim = false;
                        break;
                    }
                }

                if (uniqueClaim) return claimData[0];
            }

            return 0;
        }
    }
}
