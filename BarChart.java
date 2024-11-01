import java.util.Scanner;
  public class BarChart{
       public static void main(String[] args){
       Scanner scanner = new Scanner(System.in);
     
        System.out.print("Enter (5) number between 1 and 30:");
        int number = scanner.nextInt();
       
       for(int count = 1; count <= number ; count++){
       System.out.println("*");
       } 
   }
  }