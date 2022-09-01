//  Задайте двумерный массив. 
//  Напишите программу, 
//  которая упорядочит по убыванию элементы каждой строки двумерного массива.

Console.WriteLine("Сортировка значениий в строках матрицы от большего к меньшему ");
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

void RowFromLargestToSmallest(int[,] matrix)
{

    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            for (int s = 0; s < matrix.GetLength(1) - j - 1; s++)
            {
                if (matrix[i, s] < matrix[i, s + 1])
                {
                    int tmp = matrix[i, s];
                    matrix[i, s] = matrix[i, s + 1];
                    matrix[i, s + 1] = tmp;

                }
            }

        }

    }
}

int[,] arrmatrix = CreateMatrixRndInt(4, 3, 1, 9);
Console.WriteLine("Исходный массив");
Console.WriteLine();
PrintMatrix(arrmatrix);
Console.WriteLine();
RowFromLargestToSmallest(arrmatrix);
Console.WriteLine();
Console.WriteLine("Упорядоченный массив");
Console.WriteLine();
PrintMatrix(arrmatrix);