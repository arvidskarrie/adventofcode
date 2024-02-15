using System;
using System.Formats.Asn1;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text.RegularExpressions;

namespace FirstTest
{
    public class Day14
    {

        public class CLLN<T>
        {
            public LinkedListNode<T> Node { get; private set; }
            public LinkedList<T> List => Node.List;

            public CLLN(LinkedListNode<T> node)
            {
                Node = node;
            }

            public void Previous(int i = 1)
            {
                foreach (int _i in Enumerable.Range(0, i))
                    this.Node = Node.Previous ?? Node.List.Last;
            }

            public void Next(int i = 1)
            {
                foreach (int _i in Enumerable.Range(0, i))
                    this.Node = Node.Next ?? Node.List.First;
            }
        }

        public const int NoOfRecipies = 554401; // 554401
        public const string GoalString = "554401";
        public List<int> GoalList = new List<int>(GoalString.Select(c => (int)(c - '0')));
        public Day14()
        {
            // Console.WriteLine(PartA());
            Console.WriteLine(PartB());
        }
        private string PartA()
        {
            LinkedList<int> recipes = new();
            CLLN<int> firstElfNode = new CLLN<int>(recipes.AddLast(3));
            CLLN<int> secondElfNode = new CLLN<int>(recipes.AddLast(7));

            while (recipes.Count < NoOfRecipies + 10)
            {
                int newRecipe = firstElfNode.Node.Value + secondElfNode.Node.Value;

                if (newRecipe >= 10) recipes.AddLast(newRecipe / 10);
                recipes.AddLast(newRecipe % 10);

                firstElfNode.Next(firstElfNode.Node.Value + 1);
                secondElfNode.Next(secondElfNode.Node.Value + 1);
            }

            return string.Join("", recipes.ToList())[NoOfRecipies..(NoOfRecipies+10)];
        }

        public bool CheckGoal(List<int> recipes)
        {
            if (recipes.Count < GoalList.Count) return false;
            List<int> list = recipes.GetRange(recipes.Count-GoalList.Count, GoalList.Count);
            return list.SequenceEqual(GoalList);
        }

        private int PartB()
        {
            List<int> recipes = new() {3, 7};

            int firstElfIdx = 0;
            int secondElfIdx = 1;
            
            while (true)
            {
                int newRecipe = recipes[firstElfIdx] + recipes[secondElfIdx];

                if (newRecipe >= 10)
                {
                    recipes.Add(newRecipe / 10);
                    if (CheckGoal(recipes)) return recipes.Count - GoalList.Count;
                }

                recipes.Add(newRecipe % 10);
                if (CheckGoal(recipes)) return recipes.Count - GoalList.Count;
                
                firstElfIdx = (firstElfIdx + recipes[firstElfIdx] + 1) % recipes.Count;
                secondElfIdx = (secondElfIdx + recipes[secondElfIdx] + 1) % recipes.Count;
            }
        }
    }
}
