using System;

namespace FirstTest
{
    class Utilities
    {
    public static List<(int x, int y)> GetNeighbours((int x, int y) coord, bool includeDiagonals)
    {
        int x = coord.x;
        int y = coord.y;

        var neighbours = new List<(int x, int y)>
        {
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1)
        };

        if (includeDiagonals)
        {
            neighbours.AddRange(new List<(int x, int y)>
            {
                (x + 1, y + 1),
                (x + 1, y - 1),
                (x - 1, y + 1),
                (x - 1, y - 1)
            });
        }

        return neighbours;
    }
    }
}
