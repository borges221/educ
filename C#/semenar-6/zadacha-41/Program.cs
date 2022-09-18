// Пользователь вводит с клавиатуры M чисел. 
// Посчитайте, сколько чисел больше 0 ввёл пользователь.

Console.Write("Введите колличество чисел  ");
int m = Convert.ToInt32(Console.ReadLine());
int[] arraynum = new int[m];

void ImputElementArray(int m)
{
    for (int i = 0; i < m; i++)
    {
        Console.Write($"Введите {i+1} число ");
        arraynum[i] = Convert.ToInt32(Console.ReadLine());
    }
}

int CountNotMinusZero(int[] arraynum)
{
    int count = 0;
    for (int i = 0; i < arraynum.Length; i++)
    {
      if(arraynum[i]>0) count+=1;    
    }
    return count;
}
ImputElementArray(m);
Console.WriteLine($"Ввдено чисел больше 0 ---> {CountNotMinusZero(arraynum)}");