// Напишите программу, 
// которая на вход принимает позиции элемента в двумерном массиве, 
// и возвращает значение этого элемента или же указание, 
// что такого элемента нет.

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

Console.Write("Введите номер строки ");
int numberrow = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите номер столбца ");
int numbercol = Convert.ToInt32(Console.ReadLine());

void PositionSearch(int[,] matrix)
{
{
    if (numberrow <= matrix.GetLength(0) && numbercol<= matrix.GetLength(1))
    Console.WriteLine($"Значением элемента в строке {numberrow} столбце {numbercol} является {matrix[numberrow-1, numbercol-1]}");
    else    
    Console.WriteLine("Такого элемента в массиве нет");
}

    
}

int[,] arrmatrix = CreateMatrixRndInt(10,10, 1,100);
PrintMatrix(arrmatrix);
PositionSearch(arrmatrix);