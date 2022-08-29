// Задайте двумерный массив размером m×n, заполненный случайными вещественными числами.

double[,] CreateMatrixRndbouble (int row, int col, double max, double min)
{
    double[,] matrix = new double[row, col];
    Random rnddouble = new Random();

    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            matrix[i,j] = rnddouble.NextDouble()*100;
            matrix[i,j] = Math.Round(matrix[i,j],1);
        }
    }
    return matrix;
}

void PrintMatrix(double[,] matrix)
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

double[,] arrmatrix = CreateMatrixRndbouble(4,4, -9,-8);
PrintMatrix(arrmatrix);