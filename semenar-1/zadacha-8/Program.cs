// See https://aka.ms/new-console-template for more information
Console.WriteLine("введите число");
int num1 = Convert.ToInt32(Console.ReadLine());
int i =0;
while (i<=num1)
{
    Console.Write($"{i} ") ;
    i+=2;
}