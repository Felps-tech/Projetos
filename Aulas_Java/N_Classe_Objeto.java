package Aulas_Java;

public class N_Classe_Objeto {
    public static void main(String[] args){
        /*-Aula 17 Classe e Objeto-
        
        Classe : Fruta
        
        Objetos : Banana, Laranja, Manga
        
        -Criar Classe-
        
        public class Main {
        int x = 5;
        }
    
        //-Criar Objeto-
        
        public class Main {
        int x = 5;
        
        public static void main(String[] args) {
        Main myObj = new Main(); 
        System.out.println(myObj.x);
        }
        }
        
        public class Main {
        int x = 5;
        
        public static void main(String[] args) {
        Main myObj1 = new Main(); // Object 1
        Main myObj2 = new Main(); // Object 2
        System.out.println(myObj1.x);
        System.out.println(myObj2.x);
        }
        }
        
        -Atributos de Classe-
        
        public class Main {
        int x = 5;
        int y = 3;
        }
        
        public class Main {
        int x = 10;
        
        public static void main(String[] args) {
        Main myObj = new Main();
        myObj.x = 25; // x is now 25
        System.out.println(myObj.x);
        }
        }
        
        -Métodos de Classe-
        
        -Estática e Publica-
        
        public class Main {
        // Static method
        static void myStaticMethod() {
        System.out.println("Static methods can be called without creating objects");
        }
        
        // Public method
        public void myPublicMethod() {
        System.out.println("Public methods must be called by creating objects");
        }
        
        // Main method
        public static void main(String[] args) {
        myStaticMethod(); // Call the static method
        // myPublicMethod(); This would compile an error
        
        Main myObj = new Main(); // Create an object of Main
        myObj.myPublicMethod(); // Call the public method on the object
        }
        }
        
        -Métodos com objetos-
        
        // Create a Main class
        public class Main {
        
        // Create a fullThrottle() method
        public void fullThrottle() {
        System.out.println("The car is going as fast as it can!");
        }
        
        // Create a speed() method and add a parameter
        public void speed(int maxSpeed) {
        System.out.println("Max speed is: " + maxSpeed);
        }
        
        // Inside main, call the methods on the myCar object
        public static void main(String[] args) {
        Main myCar = new Main(); // Create a myCar object
        myCar.fullThrottle(); // Call the fullThrottle() method
        myCar.speed(200); // Call the speed() method
        }
        }
        
        // The car is going as fast as it can!
        // Max speed is: 200
        */
    }
}
