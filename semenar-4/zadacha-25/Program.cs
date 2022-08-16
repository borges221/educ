//  Задача 25: Напишите цикл,
//  который принимает на вход два числа (A и B) 
//  и возводит число A в натуральную степень B.


 Console.WriteLine("Введите число 1");
  int a = Convert.ToInt32(Console.ReadLine());
  Console.WriteLine("Введите число 2");
  int b =Convert.ToInt32(Console.ReadLine());
  int r=1;
  for(int i=0; i<b; i++)
  {
   r*=a;
  }
  Console.WriteLine($"{a} в {b} степени равно {r}");
  