// Задайте одномерный массив, заполненный случайными числами. Найдите сумму элементов, 
// стоящих на нечётных позициях (индексах).

int[] CreateArrayRndInt(int size, int min, int max)
{
    int[] array = new int[size];
    Random rnd = new Random();

    for (int i = 0; i < size; i++)
    {
        array[i] = rnd.Next(min, max + 1);
    }
    return array;
    }


void PrintArray(int[] array)
{
    Console.Write("[");
    for (int i = 0; i < array.Length; i++)
    {
        if(i<array.Length-1)Console.Write($"{array[i]},");
        else Console.Write(array[i]);
    }
    Console.Write("]");
}

int SumOdd(int[] array)
{
  int sum = 0;
for(int i = 1; i < array.Length; i+=2)
{
    sum += array[i];
}
return sum;
}

int[] array  = CreateArrayRndInt(10000, -10000, 10000); 
PrintArray(array);
Console.WriteLine($"Сумм чисел на нечетных индексах массива = {SumOdd(array)}");

