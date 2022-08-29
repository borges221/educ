// Задайте двумерный массив из целых чисел.
//  Найдите среднее арифметическое элементов в каждом столбце.

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
            if (j<matrix.GetLength(1)-1) Console.Write($"{matrix[i,j],2}||");
            else Console.Write($"{matrix[i,j],3}");
        }
        Console.WriteLine("]");
    }
}

double[] ColAverage (int[,]array)
{
    double[] averageArray = new double [array.GetLength(1)];
     
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
           averageArray[i] += array[j, i]; 
        if (j == array.GetLength(1)-1) 
        Console.Write($"  {Math.Round(averageArray[i]/array.GetLength(1), 1)}");
        }
    }
    return averageArray;  
}

int[,] arrmatrix = CreateMatrixRndInt(5,5, 1,10);
PrintMatrix(arrmatrix);
Console.WriteLine("Среднее арифметическое каждого столбца:");
ColAverage (arrmatrix);
Console.WriteLine();