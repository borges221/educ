//  Задайте прямоугольный двумерный массив. 
//  Напишите программу,
//  которая будет находить строку с наименьшей суммой элементов.
//  Программа считает сумму элементов в каждой строке 
//  и выдаёт номер строки с наименьшей суммой элементов: 1 строка

Console.WriteLine("Программа считает сумму элементов в каждой строке и выдаёт номер строки с наименьшей суммой элементов ");
Console.WriteLine();

int[,] CreateMatrixRndInt(int row, int col, int min, int max)
{
    int[,] matrix = new int[row, col];
    Random rnd = new Random();

    for (int i = 0; i < matrix.GetLength(0); i++) // строки - row
    {
        for (int j = 0; j < matrix.GetLength(1); j++) // столбцы- col
        {
            matrix[i, j] = rnd.Next(min, max + 1);
        }
    }
    return matrix;
}

void PrintMatrix(int[,] matrix)
{
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        Console.Write("[");
        for (int j = 0; j < matrix.GetLength(1); j++)

        {
            if (j < matrix.GetLength(1) - 1) Console.Write($"{matrix[i, j],2}||");
            else Console.Write($"{matrix[i, j],3}");
        }
        Console.WriteLine("]");
    }
}

int RowWithSmallestSum(int[,] matrix)
{
    int sum =0;
    int summin =0;
    int minval=0;
    for (int a = 0; a < matrix.GetLength(0); a++)
    {
        for (int b = 0; b < matrix.GetLength(1); b++)
        {
            if(a==0)
            {
                sum+=matrix[a,b];
                summin+=matrix[a,b];
            }
            else sum+=matrix[a,b];
        }
      if (sum<summin)
    {
        summin=sum;
        minval=a;
    }
    sum=0;
    }
    return minval;
}

int[,] arrmatrix = CreateMatrixRndInt(4, 3, 1, 9);
Console.WriteLine("Исходный массив");
Console.WriteLine();
PrintMatrix(arrmatrix);
Console.WriteLine();
RowWithSmallestSum(arrmatrix);
Console.WriteLine();
Console.WriteLine("Строка матрицы с наименьшей суммой элементов "+RowWithSmallestSum(arrmatrix));
