// Напишите программу, которая принимает на вход трёхзначное число 
//и на выходе показывает вторую цифру этого числа. Решить без использования строк.
Console.WriteLine("введите число");
int num1 = Convert.ToInt32(Console.ReadLine());
if (num1<=99 && num1>=-99 || num1 % 1000 == 0)
{
    Console.WriteLine("Число не трехзначное!!!");
}
else
{
    int num2 = num1 / 10;
    int num3 = num2 % 10;
        if (num3<0)
        {
        num3=num3*-1;
        Console.WriteLine(num3);
        }
        else
        {
         Console.WriteLine(num3);
        }
}
