// Напишите программу, 
// которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.
 int  n, reverse=0, rem;           
       Console.Write("Enter a number: ");      
        n= Convert.ToInt32(Console.ReadLine()); 
    int f=n;      
       while(n!=0)      
       {      
        rem=n%10;        
        reverse=reverse*10+rem;      
        n/=10;      
       }    
       int s = reverse;
if (f==s)
{
Console.WriteLine("Полиндром");   
 }
else
{
    Console.WriteLine("Не полиндром"); 
}       
// работает не только для 5значного числа 
    
    
  
