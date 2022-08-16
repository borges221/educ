// Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе
Console.WriteLine("Ведите число!");
int a = Convert.ToInt32(Console.ReadLine());
            int s = 0;
            while (a > 0)
            {
 
                s = s + a % 10;
                a = a /10 ;
 
            }
 Console.WriteLine($"Сумма цифр в введеном числе {s}");