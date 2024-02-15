using System;
using System.IO;
using System.Linq;
using System.Numerics;

namespace FirstTest
{
    public class Day13
    {

        public enum Turn
        {
            LEFT,
            STRAIGHT,
            RIGHT,
        }

        public enum Curve
        {
            UPLEFT, // \
            UPRIGHT, // /
            INTERSECTION // +
        }

        public static Dictionary<char, Curve> toCurve = new() {
            {'\\', Curve.UPLEFT},
            {'/', Curve.UPRIGHT},
            {'+', Curve.INTERSECTION}
        };

        public static Complex dirLeft = new(-1, 0);
        public static Complex dirUp = new(0, -1);
        public static Complex dirRight = new(1, 0);
        public static Complex dirDown = new(0, 1);

        public static Complex leftTurn = new(0, -1);
        public static Complex rightTurn = new(0, 1);

        public static Dictionary<char, Complex> toDir = new() {
            {'<',  dirLeft},
            {'^',  dirUp},
            {'>',  dirRight},
            {'v',  dirDown},
        };

        public class Cart
        {
            public Complex pos { get; set; }
            public Complex dir {get; set; }
            Complex nextTurn = new(0, -1);
            public Cart(Complex pos, Complex dir)
            {
                this.pos = pos;
                this.dir = dir;
            }

            public void Step()
            {
                this.pos += this.dir;

                // if the new coordinate has a curve or intersection, make sure to act on it.
                char c = Day13.InputData[(int)this.pos.Imaginary][(int)this.pos.Real];
                if (toCurve.TryGetValue(c, out Curve curve))
                {
                    if (curve == Curve.UPLEFT)
                    {
                        // Turn right and flip real axis
                        this.dir *= rightTurn;
                        this.dir = new(-this.dir.Real, this.dir.Imaginary);
                        
                    }
                    else if (curve == Curve.UPRIGHT)
                    {
                        // Turn left and flip real axis
                        this.dir *= leftTurn;
                        this.dir = new(-this.dir.Real, this.dir.Imaginary);
                    }
                    else if (curve == Curve.INTERSECTION)
                    {
                        Intersect();
                    }
                }
            }

            private void Intersect()
            {
                this.dir *= this.nextTurn;

                this.nextTurn *= rightTurn;
                if (this.nextTurn == dirLeft)
                    this.nextTurn = dirUp;
            }
        }

        public static readonly string[] InputData = File.ReadAllLines(@"c:\Users\arvid\repo\csharp\FirstTest\input.txt");
        LinkedList<Cart> cartList = new();

        public Day13()
        {
            bool doPartB = false;
            Console.WriteLine(PartA(doPartB));
        }

        public void Populate(LinkedList<Cart> cartList)
        {
            foreach (int lineIdx in Enumerable.Range(0, InputData.Length))
            {
                var line = InputData[lineIdx];
                foreach (int charIdx in Enumerable.Range(0, line.Length))
                {
                    if (toDir.TryGetValue(InputData[lineIdx][charIdx], out Complex dir))
                    {
                        cartList.AddLast(new Cart(new Complex(charIdx, lineIdx), dir));
                    }
                }

            }
        }

        public LinkedList<Cart> SortCarts(LinkedList<Cart> cartList)
        {
            List<Cart> list =  cartList.ToList();
            list.Sort((c1, c2) =>
            {
                if (c1.pos.Imaginary == c2.pos.Imaginary)
                    return c1.pos.Real.CompareTo(c2.pos.Real);
                return c1.pos.Imaginary.CompareTo(c2.pos.Imaginary);
            });
            return new LinkedList<Cart>(list);
        }

        private int PartA(bool doPartB)
        {   
            // Scan the input to find carts, turns and intersection
            Populate(cartList);

            while (cartList.Count > 1)
            {
                // Sort the carts based on coordinates
                cartList = SortCarts(cartList);
                var nextNode = cartList.First;

                while (nextNode != null)
                {
                    var currentNode = nextNode;
                    Cart cart = currentNode.Value;
                    nextNode = currentNode.Next;
                    cart.Step();

                    foreach (var otherCart in cartList.Where(c => c != cart))
                    {
                        if (cart.pos.Real == otherCart.pos.Real && cart.pos.Imaginary == otherCart.pos.Imaginary)
                        {
                            if (doPartB)
                            {
                                // Delete both nodes
                                cartList.Remove(currentNode);
                                cartList.Remove(otherCart);
                                break;
                            } else {
                                Console.WriteLine(cart.pos.Real + "," + cart.pos.Imaginary);
                                return 0;
                            }
                        }
                    }

                }
            }
            Console.WriteLine(cartList.First.Value.pos.Real + " " + cartList.First.Value.pos.Imaginary);
            return 0;
        }

        private int PartB()
        {
            return 0;
        }
    }
}
