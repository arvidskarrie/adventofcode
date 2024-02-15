using System;
using System.Formats.Asn1;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text.RegularExpressions;

namespace FirstTest
{
    public class Day9
    {

        public readonly string[] InputData = null!;
        public const int noOfPlayers = 458; // 458
        public const int lastMarble = 7201900; // 72019

        public class CLLN<T>
        {
            public LinkedListNode<T> Node { get; private set; }
            public LinkedList<T> List => Node.List;

            public CLLN(LinkedListNode<T> node)
            {
                Node = node;
            }

            public CLLN<T> Previous()
            {
                return new CLLN<T>(Node.Previous ?? Node.List.Last);
            }

            public CLLN<T> Next()
            {
                return new CLLN<T>(Node.Next ?? Node.List.First);
            }
}

        public Day9()
        {
            // InputData = File.ReadAllLines(@"c:\Users\arvid\repo\csharp\FirstTest\input.txt");
            
            Console.WriteLine(PartA());
            // Console.WriteLine(PartB());
        }
        private long PartA()
        {
            List<long> scores = Enumerable.Repeat(0L, noOfPlayers).ToList();
            LinkedList<int> marbles = new();
            CLLN<int> currentNode = new CLLN<int>(marbles.AddFirst(0));

            for (int turn = 1; turn <= lastMarble; turn++)
            {

                if (turn % 23 == 0)
                {
                    int currentPlayer = (turn - 1) % noOfPlayers;
                    scores[currentPlayer] += turn;

                    foreach (int _i in Enumerable.Range(0, 6)) currentNode = currentNode.Previous();
                    var nodeToBeRemoved = currentNode.Previous();
                    scores[currentPlayer] += nodeToBeRemoved.Node.Value;
                    marbles.Remove(nodeToBeRemoved.Node);
                } else {
                    currentNode = currentNode.Next();
                    currentNode = new CLLN<int>(marbles.AddAfter(currentNode.Node, turn));
                }
                // Console.WriteLine(string.Join(" ", marbles));
            }

            // Console.WriteLine("Score: " + string.Join(',', scores));
            return scores.Max();
        }

        private int PartB()
        {
            return 0;
        }
    }
}
