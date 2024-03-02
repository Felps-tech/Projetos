package Aulas_Java;

public class K_Array {
    public static void main(String[] args) {
        //-Aula 14 Array-
        
        //-Array-
    
        String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
        System.out.println(cars);
        
        int[] myNum = {10, 20, 30, 40};
        System.out.println(myNum);
        
        String[] cars2 = {"Volvo", "BMW", "Ford", "Mazda"};
        System.out.println(cars2[0]);
        // Outputs Volvo
        
        //-Mudar Array-
        
        String[] cars3 = {"Volvo", "BMW", "Ford", "Mazda"};
        cars3[0] = "Opel";
        System.out.println(cars3[0]);
        // Now outputs Opel instead of Volvo
        
        //-Length-
        
        String[] cars4 = {"Volvo", "BMW", "Ford", "Mazda"};
        System.out.println(cars4.length);
        // Outputs 4
        
        //-Loopar uma Array-
        
        //for (type variable : arrayname) {
        //...
        //}
        
        String[] cars5 = {"Volvo", "BMW", "Ford", "Mazda"};
        for (String i : cars5) {
        System.out.println(i);
        }
        
        //-Array Multidimensional-
        
        int[][] myNumbers = { {1, 2, 3, 4}, {5, 6, 7} };

        System.out.println(myNumbers[1][2]); // Outputs 7
        
        //-Mudar elementos da Array-
        
        int[][] myNumbers2 = { {1, 2, 3, 4}, {5, 6, 7} };
        myNumbers2[1][2] = 9;
        System.out.println(myNumbers2[1][2]); // Outputs 9 instead of 7
        
        //-Loopar atravez da arrey multidimensional-
        
        int[][] myNumbers3 = { {1, 2, 3, 4}, {5, 6, 7} };
        for (int i = 0; i < myNumbers3.length; ++i) {
        for(int j = 0; j < myNumbers3[i].length; ++j) {
        System.out.println(myNumbers3[i][j]);
            }
        }
    }
}
