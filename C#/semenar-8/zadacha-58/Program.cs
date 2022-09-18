// Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.

Console.WriteLine("Находим произведение двух матриц");
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

int[,] ResultMatrixMultiplication(int[,] matrix1, int[,] matrix2)
{
    int[,] newMatrix = new int[matrix1.GetLength(0), matrix2.GetLength(1)];
    for (int i = 0; i < matrix1.GetLength(0); i++)
    {
        for (int j = 0; j < matrix1.GetLength(0); j++)
        {
            for (int m = 0; m < matrix2.GetLength(1); m++)
            {
                newMatrix[i, m] += matrix1[i, j] * matrix2[j, m];
            }
        }

    }
    return newMatrix;
}
int[,] matrixA = CreateMatrixRndInt(4, 4, 1, 100);
Console.WriteLine("Матрица 1 ");
Console.WriteLine();
PrintMatrix(matrixA);
int[,] matrixB = CreateMatrixRndInt(4, 4, 1, 100);
Console.WriteLine("Матрица 2 ");
Console.WriteLine();
PrintMatrix(matrixB);
int[,] matrixC = ResultMatrixMultiplication(matrixA, matrixB);
Console.WriteLine("Матрица 1 умноженная на матрицу 2 ");
Console.WriteLine();
PrintMatrix(matrixC);
