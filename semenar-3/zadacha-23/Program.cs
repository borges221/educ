// Напишите программу, которая принимает на вход число (N) и выдаёт таблицу кубов чисел от 1 до N.
Console.WriteLine("Введите значение!");
int n = Convert.ToInt32(Console.ReadLine());
int i = 1;
if (n>0)
{
    while (i<=n)
    {
        int q = i*i*i;
        Console.WriteLine($"{i}|{q}");
        i++;
    }
    
}
else
    {
        Console.WriteLine($"Число должно быть больше 0");
    }
