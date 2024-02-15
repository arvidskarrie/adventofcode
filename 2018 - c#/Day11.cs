using System;
using System.Formats.Asn1;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text.RegularExpressions;

namespace FirstTest
{
    public class Day11
    {

        // public readonly string[] InputData = null!;
        public int Input = 9798; //9798
        public int Limit = 300; //9798


        public Day11()
        {
            // InputData = File.ReadAllLines(@"c:\Users\arvid\repo\csharp\FirstTest\input.txt");
            
            Console.WriteLine(PartA());
            // Console.WriteLine(PartB());
        }

        public int CalculatePowerLevel(int serial, int x, int y)
        {
            // Find the fuel cell's rack ID, which is its X coordinate plus 10.
            int rackId = x + 10;
            // Begin with a power level of the rack ID times the Y coordinate.
            int powerLevel = rackId * y;
            // Increase the power level by the value of the grid serial number (your puzzle input).
            powerLevel += serial;
            // Set the power level to itself multiplied by the rack ID.
            powerLevel *= rackId;
            // Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
            powerLevel = (powerLevel % 1000) / 100;
            // Subtract 5 from the power level.
            powerLevel -= 5;
            return powerLevel;
        }

        public List<List<int>> CalculateGrid(int serial)
        {
            List<List<int>> grid = new();
            foreach (int y in Enumerable.Range(0, Limit))
            {
                List<int> line = new();
                foreach (int x in Enumerable.Range(0, Limit))
                {
                    line.Add(CalculatePowerLevel(serial, x, y));
                }
                grid.Add(line);
            }
            return grid;
        }

        public List<List<int>> CalculateSumGrid(List<List<int>> grid)
        {
            List<List<int>> sumGrid = new();
            
            foreach (int y in Enumerable.Range(0, Limit))
            {
                int lineSumSoFar = 0;
                List<int> line = new();
                foreach (int x in Enumerable.Range(0, Limit))
                {
                    lineSumSoFar += grid[y][x];
                    line.Add(lineSumSoFar + (y == 0 ? 0 : sumGrid[y-1][x]));
                }
                sumGrid.Add(line);
            }

            return sumGrid;
        }

        public void FindHighest(List<List<int>> sumGrid)
        {
            int highestValue = int.MinValue;

            foreach (int y in Enumerable.Range(0, Limit))
            {
                foreach (int x in Enumerable.Range(0, Limit))
                {
                    foreach (int size in Enumerable.Range(0, Limit))
                    {   
                        if (Math.Max(x, y) + size >= Limit) break;

                        int bottomRight = sumGrid[y+size][x+size];
                        int topRight = y == 0 ? 0 : sumGrid[y-1][x+size];
                        int bottomLeft = x == 0 ? 0 : sumGrid[y+size][x-1];
                        int topLeft = Math.Min(x, y) == 0 ? 0 : sumGrid[y-1][x-1];

                        int cellSquareSum = bottomRight + topLeft - topRight - bottomLeft;

                        if (cellSquareSum > highestValue)
                        {
                            highestValue = cellSquareSum;
                            Console.WriteLine("" + highestValue + " " + x + " " + y + " " + size);
                        }
                    }
                }
            }
        }

        private int PartA() 
        {
            // loop over all possible 3x3 areas and calculate their power
            int serial = 9798;

            List<List<int>> grid = CalculateGrid(serial);
            List<List<int>> sumGrid = CalculateSumGrid(grid);

            FindHighest(sumGrid);

            return 0;
        }

        private int PartB()
        {
            return 0;
        }
    }
}
