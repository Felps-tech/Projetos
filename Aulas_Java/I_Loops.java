package Aulas_Java;

public class I_Loops {
    public  static void main(String[] args) {
        //-Aula 10 Loop While-
        
        //while (condition) {
        // code block to be executed
        //}
        
        int i = 0;
        while (i < 5) {
        System.out.println(i);
        i++;
        }
        
        //- Do While -
        //do {
        // code block to be executed
        //}
        //while (condition);
        
        int j = 0;
        do {
        System.out.println(i);
        j++;
        }
        while (j < 5);
        
        //-Aula 11 Loop For-
        
        //for (statement 1; statement 2; statement 3) {
        // code block to be executed
        //}
        
        for (int k = 0; k < 5; k++) {
        System.out.println(k);
        }
        
        //-Loop dentro de loop-
        
        // Outer loop
        for (int l = 1; l <= 2; l++) {
        System.out.println("Outer: " + l); // Executes 2 times
        
        // Inner loop
        for (int m = 1; m <= 3; m++) {
        System.out.println(" Inner: " + m); // Executes 6 times (2 * 3)
        }
        }
        
        //-Aula 12 Each loop-
        
        //for (type variableName : arrayName) {
        // code block to be executed
        //}

        String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
        for (String n : cars) {
        System.out.println(n);
        }
    }
}
