// This is sample in C# language for
// MCS -> Most Common (Even/Uneven) Sum
// for given list, size and mode(even/uneven)

using System;
using System.Collections.Generic;

namespace mcs_csharp
{

    public class McsProgram
    {
        public void Init()
        {
            GetBiggestSumDependingOnMode(new List<int> { 1, 2, 9, 3, 6, 6, 7, 7, 3 }, 4, "even");
            GetBiggestSumDependingOnMode(new List<int> { 102, 15, 33, 4, 81, 2, 13, 6, 79 }, 4, "even");
            GetBiggestSumDependingOnMode(new List<int> { 4, 32, 15, 1, 6, 2, 8, 6, 9 }, 3, "uneven");
            GetBiggestSumDependingOnMode(new List<int> { 0, 0, 3, 2, 0, 5, 2, 7, 6 }, 7, "uneven");
            GetBiggestSumDependingOnMode(new List<int> { 3, 32, 5 }, 3, "uneven");
            GetBiggestSumDependingOnMode(new List<int> { 3, 32, 5 }, 2, "uneven");
            GetBiggestSumDependingOnMode(new List<int> { 1, 1, 1, 2, 3 }, 3, "uneven");
            GetBiggestSumDependingOnMode(new List<int> { 6, 0, 0, 4, 3 }, 5, "even");
        }

        private void GetBiggestSumDependingOnMode(List<int> numbers, int size, string mode)
        {
            numbers.Sort();
            numbers.Reverse();

            if (size > numbers.Count || size < 2 || (mode != "even" && mode != "uneven"))
            {
                Console.WriteLine("Requirements not met.");
                Console.WriteLine();
                return;
            }

            bool isSumFound = false;
            int startingPos = 0;

            while (true)
            {
                List<int> chosenNumbers = new List<int>();
                int index = startingPos;
                int currentSum = 0;
                int numberCounter = 0;

                while (numberCounter < size - 1 && index < numbers.Count)
                {
                    currentSum += numbers[index];
                    chosenNumbers.Add(numbers[index]);
                    index++;
                    numberCounter++;
                }

                if (numberCounter + 1 != size)
                {
                    Console.WriteLine($"For: [ {ReturnElementsOfList(numbers)} ]");
                    Console.WriteLine($"Couldn't find {size} numbers for mode: {mode}");
                    Console.WriteLine();
                    break;
                }

                while (index < numbers.Count)
                {
                    int number = numbers[index];
                    int testSum = currentSum + number;
                    if ((testSum % 2 == 0 && mode == "even") || (testSum % 2 != 0 && mode == "uneven"))
                    {
                        chosenNumbers.Add(number);
                        int biggestSum = testSum;
                        isSumFound = true;
                        Console.WriteLine($"For: [ {ReturnElementsOfList(numbers)} ], {mode} ({size})");
                        Console.WriteLine($"selected: {ReturnElementsOfList(chosenNumbers)}");
                        Console.WriteLine($"which gives: {biggestSum}");
                        Console.WriteLine();
                        break;
                    }
                    index++;
                }

                if (startingPos >= numbers.Count)
                {
                    Console.WriteLine($"For: [ {ReturnElementsOfList(numbers)} ]");
                    Console.WriteLine($"startingPos reached unexpected position {startingPos}");
                    Console.WriteLine();
                    break;
                }

                if (isSumFound == false)
                {
                    startingPos++;
                }
                else if (isSumFound)
                {
                    break;
                }
            }
        }

        private string ReturnElementsOfList(List<int> list)
        {
            string output = string.Empty;
            int i = 0;
            foreach (int item in list)
            {
                if (i == 0)
                {
                    output += item.ToString();
                }
                else
                {
                    output += $" {item}";
                }
                i++;
            }
            return output;
        }
    }
}