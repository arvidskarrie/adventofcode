using System;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;

namespace FirstTest
{
    public enum MessageType
    {
        NewGuard,
        Asleep,
        Wakes,
    }
    public class Day4
    {

        // public const bool UseTestData = false;
        public readonly string[] InputData = null!;
        public string NewGuardRegex = @"\[1518-(?<month>\d+)-(?<day>\d+) (?<hour>\d+):(?<minute>\d+)\] Guard #(?<guard_id>\d+) begins shift";
        public string FallsAsleepRegex = @"\[1518-(?<month>\d+)-(?<day>\d+) (?<hour>\d+):(?<minute>\d+)\] falls asleep";
        public string WakesUpRegex = @"\[1518-(?<month>\d+)-(?<day>\d+) (?<hour>\d+):(?<minute>\d+)\] wakes up";

        public Day4()
        {
            InputData = File.ReadAllLines(@"c:\Users\arvid\repo\csharp\FirstTest\input.txt");
            // Console.WriteLine(PartA());
            Console.WriteLine(PartB());
        }

        private (MessageType msg, List<int> data) ExtractData(string claim)
        {
            {
                Match match = Regex.Match(claim, NewGuardRegex);
                if (match.Success)
                {
                    List<int> values = match.Groups
                                        .Cast<Group>()
                                        .Skip(1) // Skip the full match
                                        .Select(g => int.Parse(g.Value))
                                        .ToList();
                    // Console.WriteLine("New shift:\t" + string.Join('\t', values));
                    return (MessageType.NewGuard, values);
                }
            }
            {
                Match match = Regex.Match(claim, FallsAsleepRegex);
                if (match.Success)
                {
                    List<int> values = match.Groups
                                        .Cast<Group>()
                                        .Skip(1) // Skip the full match
                                        .Select(g => int.Parse(g.Value))
                                        .ToList();
                    // Console.WriteLine("Falls asleep:\t" + string.Join('\t', values));
                    return (MessageType.Asleep, values);
                }
            }
            {
                Match match = Regex.Match(claim, WakesUpRegex);
                if (match.Success)
                {
                    List<int> values = match.Groups
                                        .Cast<Group>()
                                        .Skip(1) // Skip the full match
                                        .Select(g => int.Parse(g.Value))
                                        .ToList();
                    // Console.WriteLine("Wakes up:\t" + string.Join('\t', values));
                    return (MessageType.Wakes, values);
                }
            }

            return (MessageType.NewGuard, data: new List<int>());
            
        }

        private int PartA()
        {
            int guard = -1;
            int asleepMinute = 0;
            Dictionary<int, Dictionary<int, int>> sleepDict = new();

            foreach (var input in InputData)
            {
                var data = ExtractData(input);
                if (data.msg == MessageType.NewGuard)
                {
                    guard = data.data[4];
                    if (!sleepDict.ContainsKey(guard)) sleepDict[guard] = new Dictionary<int, int>();
                    
                    continue;
                }
                if (data.msg == MessageType.Asleep)
                {
                    asleepMinute = data.data[3];
                    continue;
                }
                if (data.msg == MessageType.Wakes)
                {
                    int wakeMinute = data.data[3];
                    for (int minute = asleepMinute; minute < wakeMinute; minute++)
                    {
                        sleepDict[guard][minute] = sleepDict[guard].GetValueOrDefault(minute, 0) + 1;
                    }
                    continue;
                }
            }
            
            // Iterate over all guards
            int topGuard = -1;
            int topsleep = -1;
            foreach (int guardId in sleepDict.Keys)
            {
                // calculate how much it sleeps
                var guardDict = sleepDict[guardId];
                int sleepMinutes = guardDict.Values.Sum();
                // Console.WriteLine("" + guardId + "" + sleepMinutes);


                // If it sleeps more than the previous, save new top
                if (sleepMinutes > topsleep)
                {
                    topGuard = guardId;
                    topsleep = sleepMinutes;
                }
            }

            // Find the most sleepy minute for the topguard
            int topSleepMinute = sleepDict[topGuard].Aggregate((x, y) => x.Value > y.Value ? x : y).Key;
            
            return topGuard * topSleepMinute;
        }

        private int PartB()
        {
            int guard = -1;
            int asleepMinute = 0;
            Dictionary<int, Dictionary<int, int>> sleepDict = new();

            foreach (var input in InputData)
            {
                var data = ExtractData(input);
                if (data.msg == MessageType.NewGuard)
                {
                    guard = data.data[4];
                    if (!sleepDict.ContainsKey(guard)) sleepDict[guard] = new Dictionary<int, int>();
                    
                    continue;
                }
                if (data.msg == MessageType.Asleep)
                {
                    asleepMinute = data.data[3];
                    continue;
                }
                if (data.msg == MessageType.Wakes)
                {
                    int wakeMinute = data.data[3];
                    for (int minute = asleepMinute; minute < wakeMinute; minute++)
                    {
                        sleepDict[guard][minute] = sleepDict[guard].GetValueOrDefault(minute, 0) + 1;
                    }
                    continue;
                }
            }
            
            // Iterate over all guards
            int topGuard = -1;
            int topSleepAmount = -1;
            int topSleepMinute = -1;
            foreach (int guardId in sleepDict.Keys)
            {
                // calculate how much it sleeps
                var guardSleepDict = sleepDict[guardId];
                if (guardSleepDict.Count == 0) continue;
                int sleepMinute = guardSleepDict.Aggregate((x, y) => x.Value > y.Value ? x : y).Key;
                int sleepAmount = guardSleepDict[sleepMinute];


                // If it sleeps more than the previous, save new top
                if (sleepAmount > topSleepAmount)
                {
                    topGuard = guardId;
                    topSleepAmount = sleepAmount;
                    topSleepMinute = sleepMinute;
                }
            }

            // Find the most sleepy minute for the topguard
            
            return topGuard * topSleepMinute;
        }
    }
}
