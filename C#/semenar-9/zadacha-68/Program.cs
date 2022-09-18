// Напишите программу вычисления функции Аккермана с помощью рекурсии. 
// Даны два неотрицательных числа m и n.

Console.Write("Введите число М: ");
int m = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите число N: ");
int n = Convert.ToInt32(Console.ReadLine());

int AckermanCalculation(int m, int n)
{
  if (m == 0) return n + 1;
  else if (n == 0) return AckermanCalculation(m - 1, 1);
  else return AckermanCalculation(m - 1, AckermanCalculation(m, n - 1));
}
int funcAkkerman = AckermanCalculation(m, n);

Console.Write($"Функция Аккермана = {funcAkkerman} ");

