string[] arrString = { "Hello", "2", "world", ":-)","saa","borges" };
int i = 0;

int count = 0;
string[] Array(string[] arr)
{
    for (i = 0; i < arr.Length; i++)
    {
        if (arr[i].Length <= 3)
        {
            count++;

        }
    }
    
    int tmpcount = 0;
    string[] newArr = new string[count];
    for (i = 0; i < arr.Length; i++)
    {
        if (arr[i].Length <= 3)
        {
            newArr[tmpcount] = arr[i];
            tmpcount++;
        }
    }
    return newArr;
}

// Выводим результат
Console.WriteLine();
Console.Write("["+String.Join(", ", arrString)+"] ");
Console.WriteLine(" -> ["+String.Join(", ", Array(arrString))+"]");
Console.WriteLine();