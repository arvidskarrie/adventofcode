using System;
using System.Formats.Asn1;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text.RegularExpressions;

namespace FirstTest
{
    public class Day8
    {

        public struct Node {

            public Node ()
            {
            }
            public int noOfTotalEntries {get; set; }
            public List<int> metaEntries {get; set; } = new List<int>();
            public List<Node> children {get; set; } = new List<Node>();

            public void AddChild (Node node)
            {
                children.Add(node);
            }

            public int MetaEntrySumA()
            {
                int sum = metaEntries.Sum();
                foreach (Node child in children)
                {
                    sum += child.MetaEntrySum();
                }
                return sum;
            }
            public int MetaEntrySum()
            {
                int childCount = this.children.Count;
                if (childCount == 0) return this.MetaEntrySumA();

                int sum = 0;
                foreach (int childIdx in metaEntries)
                {
                    if (childCount >= childIdx)
                        sum += this.children[childIdx - 1].MetaEntrySum();
                }
                return sum;
            }
        }

        public readonly string[] InputData = null!;
        public readonly int[] Data = null!;
        public Day8()
        {
            InputData = File.ReadAllLines(@"c:\Users\arvid\repo\csharp\FirstTest\input.txt");
            Data = InputData[0].Split().Select(s => int.Parse(s)).ToArray();
            Console.WriteLine(PartA());
            // Console.WriteLine(PartB());
        }

        public Node CreateNode(int startIndex)
        {
            Node node = new();
            int noOfChildren = Data[startIndex];
            int noOfMetaEntries = Data[startIndex + 1];
            int noOfTotalEntries = 2 + noOfMetaEntries;
            
            int childStartIndex = startIndex + 2;
            foreach (int _i in Enumerable.Range(0, noOfChildren).ToList())
            {
                Node child = CreateNode(childStartIndex);
                node.AddChild(child);
                childStartIndex += child.noOfTotalEntries;
                noOfTotalEntries += child.noOfTotalEntries;
            }

            int[] subarray = new int[noOfMetaEntries];
            Array.Copy(Data, childStartIndex, subarray, 0, noOfMetaEntries);
            node.metaEntries = subarray.ToList();

            node.noOfTotalEntries = noOfTotalEntries;
            Console.WriteLine(node.noOfTotalEntries);
            return node;
        }

        private int PartA()
        {
            // Process the int list and add nodes continuously
            // Use an index integer to know where to start reading the list
            Node baseNode = CreateNode(0);
            return baseNode.MetaEntrySum();
        }

        private int PartB()
        {
            return 0;
        }
    }
}
