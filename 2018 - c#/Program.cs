using System;
using System.Linq;

namespace FirstTest
{
    class Program
    {
        static void Main(string[] args)
        {
            // _ = new Day14();
            TestLinq();
        }

        private static void TestLinq()
        {
            // {
            //     var list = new List<string> {"hello", "world"};
            //     var linq = list.Select(s => new string((char)(s[0] + 'A' - 'a') + s[1..]));
            //     Console.WriteLine(string.Join(", ", linq));
            // }
            // {
            //     var list = new List<string> {"apple", "banana", "cherry"};
            //     string linq = list.Aggregate("", (acc, s) => acc += s[0]);
            //     Console.WriteLine(linq);
            // }
            // {
            //     var list = new List<string> {"John", "Jane", "Doe"};
            //     string linq = list.Skip(1).Aggregate(list[0], (acc, s) => acc += ("," + s));
            //     Console.WriteLine(linq);
            // }
            // {
            //     var list = new List<string> {"3", "5", "1"};
            //     List<int> linq = list.Select(s => int.Parse(s)).OrderBy( i => -i).ToList();
            //     Console.WriteLine(string.Join(", ", linq));
            // }
            // {
            //     var list = new List<int> {1, 2, 3, 4, 5};
            //     int linq = list.Where(i => i % 2 == 0).Sum();
            //     Console.WriteLine(linq);
            // }
            // {
            //     var list = new List<int> {1, 2, 3, 4, 5};
            //     double linq = list.Where(i => i % 2 == 1).Average(n => n*n);
            //     Console.WriteLine(linq);
            // }
            // {
            //     var list = new List<int> {1, 2, 3, 4, 5};
            //     IEnumerable<int> linq = list.Select(n => n*n);
            //     Console.WriteLine(string.Join(", ", linq));
            // }
            // {
            //     IEnumerable<int> list = Enumerable.Range(0, 100);
            //     IEnumerable<int> linq = list.Where(n => n % 7 == 0);
            //     Console.WriteLine(string.Join(", ", linq));
            // }
            // {
            //     List<string> list = new() {"aaa", "bb", "c", "dddd"};
            //     string linq = list.OrderBy(s => s.Length).Last();
            //     Console.WriteLine(linq);
            //     // Console.WriteLine(string.Join(", ", linq));
            // }
            // {
            //     List<int> list = new() {2, 3, 4, 5, 6, 7, 8, 9, 10};
            //     IEnumerable<int> linq = list.Where(s => !list.Where(t => s != t).Any(t => s % t == 0));
            //     // Console.WriteLine(linq);
            //     Console.WriteLine(string.Join(", ", linq));
            // }
            // {
            //     List<int> list = new() {1, 2, 3, 4, 5, 16, 17, 18, 19, 20};
            //     IEnumerable<int> linq = list.Where(s => float.IsInteger(float.Sqrt((float)s)));
            //     // Console.WriteLine(linq);
            //     Console.WriteLine(string.Join(", ", linq));
            // }
            // {
            //     List<int> list = Enumerable.Range(0, 999).ToList();
            //     // IEnumerable<int> linq = list.Where(s => s.ToString().Sum(c => int.Parse(c.ToString())) % 2 == 0);

            //     var linq3 = list.Select(i => i.ToString());
            //     var linq2 = linq3.Select(c => int.Parse(c.ToString()));
            //     var linq = linq2.Where(i => int.IsEvenInteger(i));

            //     IEnumerable<int> linq4 = list.Where(i => int.IsEvenInteger(i.ToString().Sum(c => int.Parse(c.ToString()))));
            //     Console.WriteLine(string.Join(", ", linq4));
            // }
            // {
            //     List<int> list = new() {1, 2, 3, 1, 2, 4, 4, 4};
            //     var linq = list.GroupBy(i => i).Select(group => group.Key + " " + group.Count());

            //     Console.WriteLine(string.Join(", ", linq));
            // }
            // {
            //     List<int> list = new() {1, 2, 3, 1, 2, 4, 4, 4};
            //     var linq = list.GroupBy(i => i).OrderByDescending(group => group.Count()).First().Key;

            //     Console.WriteLine(string.Join(", ", linq));
            // }
            // {
            //     List<string> list = new() {"a", "aa", "aaa", "aabaa", "abbba", "bbbbbba"};
            //     var linq = list.OrderByDescending(str => str.ToCharArray().Where(c => c == 'a').Count()).First();
                
            //     Console.WriteLine(string.Join(", ", linq));
            // }
            // {
            //     List<string> list = new() {"a", "aa", "aaa", "aabaa", "abbba", "bbbbbba"};
            //     var linq = list.OrderByDescending(str => str.ToCharArray().Where(c => c == 'a').Count());
                
            //     Console.WriteLine(string.Join(", ", linq));
            // }
            {
                List<string> list = new() {"apple", "banana", "cherry", "date", "elderberry"};
                var linq = list.GroupBy(f => f.Length);
                var linq2 = linq.Select(g => "" + g.Key + " " + string.Join(" ", g.ToList()));
                Console.WriteLine(string.Join(", ", linq2));
            }
            {
                List<string> list = new List<string> { "file1.txt", "file2.jpg", "file3.txt", "file4.png", "file5.jpg" };
                var linq = list.GroupBy(f => f.Split('.').Last()).ToDictionary(g => g.Key, g => g.ToList());

                foreach (var group in linq)
                    Console.WriteLine($"Group {group.Key}: {string.Join(", ", group.Value)}");
            }
        }
    }
}
