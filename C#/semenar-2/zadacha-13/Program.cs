// Напишите программу, которая выводит третью цифру заданного числа или сообщает, 
//что третьей цифры нет. Решить без использования строк
Console.WriteLine("введите число" );
int num = Convert.ToInt32(Console.ReadLine());
if (num < 100)
{
    Console.WriteLine("в числе " + num + " нет третьей цифры");
}
else if(num <= 999)
    {
        Console.Write("третья цифра заданного числа = "+ num % 10);
    }
else while (num >= 999)
{
    {
       num = num / 10;   
    }
       if (num <= 999)
    {
       Console.WriteLine("третьим числом из заданного является " + num % 10);
    } 
}
    
