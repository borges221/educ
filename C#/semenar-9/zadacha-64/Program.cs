// Задайте значение N. 
// Напишите программу, 
// которая выведет все натуральные числа в промежутке от N до 1. 
// Выполнить с помощью рекурсии.

Console.Write("Введите число N больше 0: ");
int n = Convert.ToInt32(Console.ReadLine());

void NaturalNumbersFromNTo1(int num)
{
    if (num == 0) return;
    Console.Write($"{num} ");
    NaturalNumbersFromNTo1(num - 1);
}
NaturalNumbersFromNTo1(n);