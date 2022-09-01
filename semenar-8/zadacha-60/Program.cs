// Сформируйте трёхмерный массив из неповторяющихся двузначных чисел. 
// Напишите программу, которая будет построчно выводить массив, 
// добавляя индексы каждого элемента.

// Console.WriteLine($"Задача 60: Сформируйте трёхмерный массив из неповторяющихся двузначных чисел. Напишите программу, которая будет построчно выводить массив, добавляя индексы каждого элемента.");
Console.WriteLine($"\nВведите размер массива X x Y x Z:");
int x = InputNumbers("Введите X: ");
int y = InputNumbers("Введите Y: ");
int z = InputNumbers("Введите Z: ");
Console.WriteLine($"");

int[,,] matrix3d = new int[x, y, z];
Creatematrix3d(matrix3d);
Printmatrix3d(matrix3d);

int InputNumbers(string input)
{
  Console.Write(input);
  int output = Convert.ToInt32(Console.ReadLine());
  return output;
}

void Printmatrix3d (int[,,] matrix3d)
{
  for (int i = 0; i < matrix3d.GetLength(0); i++)
  {
    for (int j = 0; j < matrix3d.GetLength(1); j++)
    {
      Console.Write($"X({i}) Y({j}) ");
      for (int k = 0; k < matrix3d.GetLength(2); k++)
      {
        Console.Write( $"Z({k})={matrix3d[i,j,k]}; ");
      }
      Console.WriteLine();
    }
    Console.WriteLine();
  }
}

void Creatematrix3d(int[,,] matrix3d)
{
  int[] temp = new int[matrix3d.GetLength(0) * matrix3d.GetLength(1) * matrix3d.GetLength(2)];
  int  number;
  for (int i = 0; i < temp.GetLength(0); i++)
  {
    temp[i] = new Random().Next(10, 100);
    number = temp[i];
    if (i >= 1)
    {
      for (int j = 0; j < i; j++)
      {
        while (temp[i] == temp[j])
        {
          temp[i] = new Random().Next(10, 100);
          j = 0;
          number = temp[i];
        }
          number = temp[i];
      }
    }
  }
  int count = 0; 
  for (int x = 0; x < matrix3d.GetLength(0); x++)
  {
    for (int y = 0; y < matrix3d.GetLength(1); y++)
    {
      for (int z = 0; z < matrix3d.GetLength(2); z++)
      {
        matrix3d[x, y, z] = temp[count];
        count++;
      }
    }
  }
}
Printmatrix3d(matrix3d);