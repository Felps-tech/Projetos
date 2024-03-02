package Aulas_Java;

public class G_If_Else {
    public static void main(String[] args){
        //-Aula 8 if else-
        
        //-IF-
        //if (condition) {
        // block of code to be executed if the condition is true
        //}
        
        int x = 20;
        int y = 18;
        if (x > y) {
        System.out.println("x is greater than y");
        }
        
        //-ELSE-
        
        //if (condition) {
        // block of code to be executed if the condition is true
        //} else {
        // block of code to be executed if the condition is false
        //}
        
        int time = 20;
        if (time < 18) {
        System.out.println("Good day.");
        } else {
        System.out.println("Good evening.");
        }
        // Outputs "Good evening.
        
        //-ELSE IF-
        
        //if (condition1) {
        // block of code to be executed if condition1 is true
        //} else if (condition2) {
        // block of code to be executed if the condition1 is false and condition2 is
        //true
        //} else {
        // block of code to be executed if the condition1 is false and condition2 is
        //false
        //}
        
        //-IF ELSE ENCURTADO-
        
        //variable = (condition) ? expressionTrue : expressionFalse;
        
        int time1 = 20;
        String result = (time1 < 18) ? "Good day." : "Good evening.";
        System.out.println(result);
    }
}
