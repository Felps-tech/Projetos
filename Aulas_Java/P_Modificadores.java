package Aulas_Java;

public class P_Modificadores {
    public static void main(String[] args) {
        /*-Aula 19 Modificadores-
        
        public: A classe/código é acessivel para qualquer outra classe
        default: A classe/código é apenas acessivel para classes no mesmo pacote
        private: O código só é acessivel para a classe declarada
        protected: O código é acessivel no mesmo pacote e subclasses
        
        -Modificadores Sem Acesso-
        
        final:A classe/método não pode ser alterada
        abstract:A classe/método não pode ser usada como objeto
        static: Métodos pertencem para a classe ao inves de um objeto
        transient: Métodos são pulados quando serializar objetos que ele contem
        synchronized: Métodos só podem ser acessados um de cada vez
        volatile: Variáveis podem ser alteradas por mais de uma thread
        simultaneamente
        
        -Final-
        public class Main {
        final int x = 10;
        final double PI = 3.14;
        
        public static void main(String[] args) {
        Main myObj = new Main();
        myObj.x = 50; // will generate an error: cannot assign a value to a final
        variable
        myObj.PI = 25; // will generate an error: cannot assign a value to a final
        variable
        System.out.println(myObj.x);
        }
        }
        
        -Static-
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
        public static void main(String[ ] args) {
        myStaticMethod(); // Call the static method
        // myPublicMethod(); This would output an error
        
        Main myObj = new Main(); // Create an object of Main
        myObj.myPublicMethod(); // Call the public method
        }
        }
        
        -Abstract-
        // Code from filename: Main.java
        // abstract class
        abstract class Main {
        public String fname = "John";
        public int age = 24;
        public abstract void study(); // abstract method
        }
        
        // Subclass (inherit from Main)
        class Student extends Main {
        public int graduationYear = 2018;
        public void study() { // the body of the abstract method is provided here
        System.out.println("Studying all day long");
        }
        }
        // End code from filename: Main.java
        
        // Code from filename: Second.java
        class Second {
        public static void main(String[] args) {
        // create an object of the Student class (which inherits attributes and
        methods from Main)
        Student myObj = new Student();
        
        System.out.println("Name: " + myObj.fname);
        System.out.println("Age: " + myObj.age);
        System.out.println("Graduation Year: " + myObj.graduationYear);
        myObj.study(); // call abstract method
        }
        }
         */
    }
}
