// Задайте массив вещественных чисел. 
// Найдите разницу между максимальным и минимальным элементами массива.
double[] RealArray(int length, int deviation)
{
    double[] arrayGen = new double[length];
    double arrayGen1 = new double();
    double arrayGen2 = new double();
    for (int i = 0; i < length; i++)
    {
        arrayGen1 = new Random().NextDouble();
        arrayGen2 = new Random().Next(-deviation, deviation + 1);
        arrayGen[i] = arrayGen1 + arrayGen2;
        arrayGen[i] = Math.Round(arrayGen[i], 3);
    }
    return arrayGen;
}

double DifferenceBeetwinMaxMin(double[] array)
{
    double difference = new double();
    double maxNum = array[0];
    double minNum = array[0];
    for (int i = 0; i < array.Length; i++)
    {
        if (maxNum < array[i])
        {
            maxNum = array[i];
        }
        else
        {
            if (minNum > array[i])
            {
                minNum = array[i];
            }
        }
    }
    difference = maxNum - minNum;
    return difference;
}

void PrintArray(double[] array)
{
    Console.Write("[");
    for (int i = 0; i < array.Length - 1; i++)
    {
        Console.Write($"{array[i]}; ");
    }
    Console.Write($"{array[array.Length - 1]}]");
}

Console.WriteLine("Введите длину массива ");
int lengthUser = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите значение диапазона чисел в массиве (при вводе числа 10 диапозон будет от -10.000 до 10.000): ");
int deviationUser = Convert.ToInt32(Console.ReadLine());

double[] arrayUser = RealArray(lengthUser, deviationUser);
double differenceElement = DifferenceBeetwinMaxMin(arrayUser);

Console.Write("Массиd ");
PrintArray(arrayUser);
Console.WriteLine($" разница между максимальным и минимальным элементами массива равна {differenceElement}");
