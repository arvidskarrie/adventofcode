using System;
using System.Formats.Asn1;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;

namespace FirstTest
{
    public class Day6
    {


        public struct Coordinate
        {
            public Coordinate(int x, int y)
            {
                X = x;
                Y = y;
            }
            public int X { get; set; }
            public int Y { get; set; }

            public static bool operator ==(Coordinate left, Coordinate right)
            {
                return left.X == right.X && left.Y == right.Y;
            }

            public static bool operator !=(Coordinate left, Coordinate right)
            {
                return !(left == right);
            }
            public override int GetHashCode()
            {
                return HashCode.Combine(X, Y);
            }
        }
        public readonly string[] InputData = null!;
        public List<Coordinate> m_coordinates = new();
        public int topLimit = int.MinValue;
        public int bottomLimit = int.MaxValue;
        public int rightLimit = int.MinValue;
        public int leftLimit = int.MaxValue;
        public string RegexString = @"(?<x>\d+), (?<y>\d+)";
        public Day6()
        {
            InputData = File.ReadAllLines(@"c:\Users\arvid\repo\csharp\FirstTest\input.txt");
            extractCoords();
            Console.WriteLine(PartA());
            // Console.WriteLine(PartB());
        }

        private void extractCoords()
        {
            foreach (var line in InputData)
            {
                Match match = Regex.Match(line, RegexString);
                int x = int.Parse(match.Groups["x"].Value);
                int y = int.Parse(match.Groups["y"].Value);

                topLimit = Math.Max(topLimit, y + 1);
                rightLimit = Math.Max(rightLimit, x + 1);
                bottomLimit = Math.Min(bottomLimit, y - 1);
                leftLimit = Math.Min(leftLimit, x - 1);        

                Coordinate coordinate = new Coordinate(x, y);
                m_coordinates.Add(coordinate);
            }
        }

        public int getDist(Coordinate coordA, Coordinate coordB)
        {
            return Math.Abs(coordA.X - coordB.X) + Math.Abs(coordA.Y - coordB.Y);
        }

        private bool isInfinite(Coordinate coord)
        {
            if (coord.X == rightLimit || coord.X == leftLimit) return true;
            if (coord.Y == bottomLimit || coord.Y == topLimit) return true;            
            return false;
        }

        private List<Coordinate> getNeighbours(Coordinate coord)
        {
            List<Coordinate> neighbours = new()
            {
                new Coordinate(coord.X + 1, coord.Y),
                new Coordinate(coord.X - 1, coord.Y),
                new Coordinate(coord.X, coord.Y + 1),
                new Coordinate(coord.X, coord.Y - 1)
            };
            return neighbours;

        }

        private bool isClosest(Coordinate origin, Coordinate test)
        {
            int originDist = getDist(origin, test);
            foreach (Coordinate c in m_coordinates)
            {
                if (c == origin) continue;
                if (getDist(c, test) <= originDist) return false;
            }
            return true;
        }

        private int countArea2(Coordinate origin)
        {
            // Try each direction, and if it is closest to our coordinate, add it to a list and recurse from there.
            // Console.WriteLine("Testing " + test.X + " " + test.Y);

            Stack<Coordinate> stackToTest = new();
            stackToTest.Push(origin);

            HashSet<Coordinate> visited = new();


            while ( stackToTest.Count > 0)
            {
                var c = stackToTest.Pop();

                // If not closest to origin, continue
                if (!isClosest(origin, c)) continue;
                // If touching outer box, it is infinite and should be disqualified
                if (isInfinite(c)) return 0;
                // If new and closest to origin, add to visited and add its neighbours
                visited.Add(c);

                // Add any coordinate that have not yet been accepted to the test stack.
                foreach (Coordinate c_n in getNeighbours(c).Where(c_n => !visited.Contains(c_n)))
                {
                    stackToTest.Push(c_n);
                }
            }

            return visited.Count;
        }


        private int PartA()
        {
            // For every coordinate, circle around it and count the number of coordinates that are closest to it.
            int maxArea = 0;
            foreach (Coordinate coord in m_coordinates)
            {
                maxArea = Math.Max(maxArea, countArea2(coord));
            }
            return maxArea;
            // If we reach infinity, stop
        }

        private void mapArea(Coordinate test, HashSet<Coordinate> set)
        {
            if (set.Contains(test)) return;

            if (!isAcceptable(test)) return;
            set.Add(test);

            foreach (Coordinate c in getNeighbours(test))
            {
                mapArea(c, set);
            }
            return;
        }

        private int calculateArea(Coordinate origin)
        {

            Stack<Coordinate> coordinatesToTest = new();
            coordinatesToTest.Push(origin);
            HashSet<Coordinate> set = new HashSet<Coordinate>();

            while (coordinatesToTest.Count > 0)
            {
                // Test the first coordinate in the queue
                var c = coordinatesToTest.Pop();

                if (!isAcceptable(c)) continue;
                if (set.Contains(c)) continue;
                
                set.Add(c);


                // Add all its neighbours for testing
                foreach (Coordinate c_n in getNeighbours(c))
                {
                    coordinatesToTest.Push(c_n);
                }
            }
            return set.Count;
        }


        private bool isAcceptable(Coordinate coord)
        {
            const int limit = 10000;
            int totalDistance = 0;
            foreach (Coordinate c in m_coordinates)
            {
                totalDistance += getDist(coord, c);
            }
            return totalDistance < limit;
        }

        private int PartB()
        {

            // jump around inside rectangle to find a starting seed

            Coordinate testCoord;

            while (true)
            {
                Random rnd = new Random();
                int x_rand = rnd.Next(leftLimit, rightLimit);
                int y_rand = rnd.Next(bottomLimit, topLimit);

                testCoord = new(x_rand, y_rand);

                if (isAcceptable(testCoord)) break;
            }
            Console.WriteLine("Found seed " + testCoord.X + " " + testCoord.Y);

            HashSet<Coordinate> set = new();
            return calculateArea(testCoord);
        }
    }
}
