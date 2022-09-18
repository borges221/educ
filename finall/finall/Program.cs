string[] inArray = { "Hello", "2", "world", ":-)","borges","SAA" };
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
    
    string[] finArrey = new string[count];
    int temp = 0;
    
    for (i = 0; i < arr.Length; i++)
    {
        if (arr[i].Length <= 3)
        {
            finArrey[temp] = arr[i];
            temp++;
        }
    }
    return finArrey;
}


Console.WriteLine();
Console.Write("["+String.Join(", ", inArray)+"] ");
Console.WriteLine(" -> ["+String.Join(", ", Array(inArray))+"]");
Console.WriteLine();