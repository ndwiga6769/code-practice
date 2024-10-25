using System;

namespace myApplication
{
class Program
	{
    static void Main(string[] args)
    	{
        try
        	{
            int[] myArray = {2,3,4,5,6,7,8,9};
            Console.WriteLine(myArray[10]);
            }
        catch (Exception e)
        	{
            Console.WriteLine(e.Message);
            }
        }
    }
}