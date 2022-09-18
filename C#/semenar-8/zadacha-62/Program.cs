// Напишите программу, которая заполнит спирально массив 4 на 4.




int[] numPos = new int[] { 21, 22, 12, 11, 10, 20, 30, 31, 32, 33, 23, 13, 03, 02, 01, 00 };
int[,] resultmatrix = new int[4, 4];
int j = 16;
for (int i = 0; i < numPos.Length; i++)
{
    int x = numPos[i] / 10;
    int y = numPos[i] % 10;

    resultmatrix[x, y] = j--;
}

void PrintMatrix(int[,] matrix)
{
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
            Console.Write($"{matrix[i, j]}".PadLeft(2, '0') + " ");
        Console.WriteLine();
    }
    Console.WriteLine();
}

PrintMatrix(resultmatrix);

