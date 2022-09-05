// Задайте значения M и N.
//  Напишите программу, 
//  которая найдёт сумму натуральных элементов в промежутке от M до N

Console.Write("Введите значение М: ");
int m = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите значение N: ");
int n = Convert.ToInt32(Console.ReadLine());
int sum = 0;
int tmp = m;
if (m > n)
{
    m = n;
    n = tmp;
}

void ElementSumm(int numberm, int numbern, int numbersum)
{
    numbersum = numbersum + numbern;
    if (numbern <= numberm)
    {
        Console.WriteLine($"Сумма элементом между введенными значениями равна {numbersum}.");
        return;
    }
    ElementSumm(numberm, numbern - 1, numbersum);
}

ElementSumm(m, n, sum);