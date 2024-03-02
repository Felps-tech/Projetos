package Aulas_Java;

public class L_Métodos {
    public static void main(String[] args) {
        /*-Aula 15 Métodos-
        
        //-Criação de um método-
        public class Main {
        static void myMethod() {
        // code to be executed
        }
        }
        
        //-Chamar o método-
        public class Main {
        static void myMethod() {
        System.out.println("I just got executed!");
        }
        
        public static void main(String[] args) {
        myMethod();
        }
        }
        
        // Outputs "I just got executed!"
        
        -Métodos com parâmetros-
        
        public class Main {
        static void myMethod(String fname) {
        System.out.println(fname + " Refsnes");
        }
        
        public static void main(String[] args) {
        myMethod("Liam");
        myMethod("Jenny");
        myMethod("Anja");
        }
        }
        // Liam Refsnes
        // Jenny Refsnes
        // Anja Refsnes
        
        -Parâmetros multiplos-
        
        public class Main {
        static void myMethod(String fname, int age) {
        System.out.println(fname + " is " + age);
        }
        
        public static void main(String[] args) {
        myMethod("Liam", 5);
        myMethod("Jenny", 8);
        myMethod("Anja", 31);
        }
        }
        
        // Liam is 5
        // Jenny is 8
        // Anja is 31
        
        -Retornar valores-
        
        public class Main {
        static int myMethod(int x) {
        return 5 + x;
        }
        
        public static void main(String[] args) {
        System.out.println(myMethod(3));
        }
        }
        // Outputs 8 (5 + 3)
        
        -Método com if else-
        
        public class Main {
        
        // Create a checkAge() method with an integer variable called age
        static void checkAge(int age) {
        
        // If age is less than 18, print "access denied"
        if (age < 18) {
        System.out.println("Access denied - You are not old enough!");
        
        // If age is greater than, or equal to, 18, print "access granted"
        } else {
        System.out.println("Access granted - You are old enough!");
        }
        
        }
        
        public static void main(String[] args) {
        checkAge(20); // Call the checkAge method and pass along an age of 20
        }
        }
        
        // Outputs "Access granted - You are old enough!"
        
        -Método Overloading-
        
        static int plusMethodInt(int x, int y) {
        return x + y;
        }
        
        static double plusMethodDouble(double x, double y) {
        return x + y;
        }
        
        public static void main(String[] args) {
        int myNum1 = plusMethodInt(8, 5);
        double myNum2 = plusMethodDouble(4.3, 6.26);
        System.out.println("int: " + myNum1);
        System.out.println("double: " + myNum2);
        }
        */
    }
}
