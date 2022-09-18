// Напишите программу, которая задаёт массив из 8 элементов и выводит их на экран.

void ArrayRandom(int[] array)
{
    for (int i=0; i<array.Length; i++)
    {
        array[i]= new Random().Next(0,401);
    }
}

void ShowArray(int[] array)
{
    Console.Write("[");
    for (int i=0; i<array.Length; i++)
    {
        if (i<array.Length-1) Console.Write(array[i]+",");
        else Console.Write(array[i]);
    }
    Console.Write("]");
}
Console.WriteLine("Вывод массива");
int[] mas = new int[8];
ArrayRandom(mas);
ShowArray(mas);