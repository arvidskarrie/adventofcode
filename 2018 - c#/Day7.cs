using System;
using System.Formats.Asn1;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;

namespace FirstTest
{
    public class Day7
    {


        public readonly string[] InputData = null!;
        public Day7()
        {
            InputData = File.ReadAllLines(@"c:\Users\arvid\repo\csharp\FirstTest\input.txt");
            // Console.WriteLine(PartA());
            Console.WriteLine(PartB());
        }

        private bool RequirementsFulfilled(List<char> cList, string fulfilled)
        {
            foreach (char c in cList.Where(c => !fulfilled.Contains(c)))
            {
                return false;
            }
            return true;
        }

        private string PartA()
        {
            SortedDictionary<char, List<char>> requirements = new();

            foreach (string input in InputData)
            {
                char req = input[5];
                char target = input[36];
                if (!requirements.ContainsKey(req)) requirements[req] = new List<char>();
                if (!requirements.ContainsKey(target)) requirements[target] = new List<char>();
                requirements[target].Add(req);
            }

            string fulfilled = "";

            while (requirements.Count > 0)
            {
                // Go through the dictionary alphabetically and find the first target with no requirement
                foreach (char c in requirements.Keys)
                {
                    if (RequirementsFulfilled(requirements[c], fulfilled))
                    {
                        fulfilled += c;
                        requirements.Remove(c);
                        break;
                    }
                }
            }

            return fulfilled;
        }

        private int GetNextFinishTime(int currentTime, List<(int, char)> assignments)
        {
            // Find the lowest time larger than currentTime
            var timeList = assignments.Select(t => t.Item1).Where(t => t != currentTime).ToList();
            if (timeList.Count > 0) return timeList.Min();
            else return -1;
                        
        }

        private int PartB()
        {
            SortedDictionary<char, List<char>> requirements = new();

            foreach (string input in InputData)
            {
                char req = input[5];
                char target = input[36];
                if (!requirements.ContainsKey(req)) requirements[req] = new List<char>();
                if (!requirements.ContainsKey(target)) requirements[target] = new List<char>();
                requirements[target].Add(req);
            }

            string fulfilled = "";
            int finishingTime = 0;
            List<(int, char)> assignments = Enumerable.Repeat((0, '0'), 5).ToList();

            while (assignments.Count > 0)
            {
                // Finish all jobs that have the same minimum finishing time
                int currentTime = assignments.Select(t => t.Item1).Where(i => i != -1).ToList().Min();
                foreach (var ass in assignments.Where(x => x.Item1 == currentTime && x.Item2 != '0'))
                {
                    char c = ass.Item2;
                    fulfilled += c;
                }

                // Look for a new job for every elf that just finished
                var reverseIndices = Enumerable.Range(0, assignments.Count).ToList();
                reverseIndices.Reverse();

                foreach (int idx in reverseIndices)
                {
                    // Only work on the elves that finishes
                    if (assignments[idx].Item1 != currentTime) continue;

                    // If there are no requirements left, delete the elf and continue
                    if (requirements.Count == 0)
                    {
                        finishingTime = currentTime;
                        assignments.RemoveAt(idx);
                        continue;
                    }

                    // Go through the dictionary alphabetically and find the first target with no unfulfilled requirement
                    foreach (char c in requirements.Keys)
                    {
                        if (RequirementsFulfilled(requirements[c], fulfilled))
                        {
                            int processingTime = 61 + c - 'A';
                            assignments[idx] = (assignments[idx].Item1 + processingTime, c);
                            requirements.Remove(c);
                            break;
                        }
                    }

                    // If an elf did not get an assignment, make it wait until the next assignment finishes
                    if (assignments[idx].Item1 == currentTime)
                    {
                        assignments[idx] = (GetNextFinishTime(currentTime, assignments), '0');
                    }
                }
            }

            return finishingTime;
        }
    }
}
