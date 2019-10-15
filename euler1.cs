// Find the sum of all the multiples of 3 or 5 below 1000.
using System;

class App{
  public static void Main(string[] args)
  {
    int limit = 1000;
    int sum = 0;

    for(var i = 1; i < limit; i++) {
      if(i % 3 == 0 || i % 5 == 0) {
        sum += i;
      }
    }

    Console.WriteLine($"Sum of all multiples of 3 and 5 bellow 1000 is {sum}");
  }
}
