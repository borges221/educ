// Напишите программу, которая на вход принимает два числа и выдаёт, какое число большее, а какое меньшее.
 Console.WriteLine("Введите первое число: ");
            int num1 = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Введите второе число: ");
            int num2 = Convert.ToInt32(Console.ReadLine());
 
            if(num1 > num2)
            {
                Console.Write($"число {num1} больше числа {num2}") ;
            }
            else if (num1 < num2)
            {
                 Console.Write($"число {num1} меньше числа {num2}") ;
            }
            else
            {
                Console.WriteLine("Оба числа равны");
            }