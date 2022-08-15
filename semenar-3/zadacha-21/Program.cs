// Напишите программу, 
// которая принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве.
Console.WriteLine("Введите координату X для точки 1");
int x1 = int.Parse(Console.ReadLine()); 
Console.WriteLine("Введите координату Y для точки 1");
int y1 = int.Parse(Console.ReadLine()); 
Console.WriteLine("Введите координату Z для точки 1");
int z1 = int.Parse(Console.ReadLine()); 
Console.WriteLine("Введите координату X для точки 2");
int x2 = int.Parse(Console.ReadLine()); 
Console.WriteLine("Введите координату Y для точки 2");
int y2 = int.Parse(Console.ReadLine()); 
Console.WriteLine("Введите координату Z для точки 2");
int z2 = int.Parse(Console.ReadLine()); 
double res = Math.Sqrt((x2-x1)*(x2-x1)+(y1-y2)*(y1-y2)+(z2-z1)*(z2-z1));
Console.WriteLine("Растояние между точками {0: #.##}", res);