// Напишите программу, 
// которая найдёт точку пересечения двух прямых, 
// заданных уравнениями y = k1 * x + b1, y = k2 * x + b2; 
// значения b1, k1, b2 и k2 задаются пользователем.

Console.WriteLine("Пересекутся ли прямы заданые уровненями y = k1 * x + b1, y = k2 * x + b2??? ");
Console.WriteLine("Ввелите значение b1:");
int b1 = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Ввелите значение k1:");
int k1 = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Ввелите значение b2:");
int b2 = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Ввелите значение k2:");
int k2 = Convert.ToInt32(Console.ReadLine());

void MeetingPoint(double b1, double k1, double b2, double k2)
{
    double[] dot = new double[2];
    dot[0] = (b2 - b1) / (k1 - k2);
    dot[1] = k1 * dot[0] + b1;

    if ((k1 * dot[0] + b1) == (k2 * dot[0] + b2)) 
    {


        Console.Write("Пряммые пересекаются в точке: ");
        Console.Write($"[{String.Join(", ", dot)}]");
    }
    else
    {
    Console.WriteLine("Прямые не пересекаются.");
    }
}
MeetingPoint(b1,k1,b2,k2);