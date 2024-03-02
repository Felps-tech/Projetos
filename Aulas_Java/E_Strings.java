package Aulas_Java;

public class E_Strings {
    public static void main(String[] args){
        //-Aula 6 Strings-
        
        //-lenght()-
        String txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        System.out.print("Tamanho: " + txt.length());
        
        //-toUpperCase() e toLowerCase()-
        String txt2 = "Hello World";
        System.out.println(txt2.toUpperCase()); //Outputs "HELLO WORLD";
        System.out.println(txt2.toLowerCase()); //Outputs "hello world";
        
        //-indexOf()-
        String txt3 = "Please locate where 'locate' occurs!";
        System.out.println(txt3.indexOf("locate")); // Outputs 7
        
        //-concat()-
        String firstName = "John ";
        String lastName = "Doe";
        System.out.println(firstName.concat(lastName));
        
        //-Número e String-
        int a = 20;
        int b = 10;
        int c = a + b; // 30 (como numero inteiro)
        System.out.println(c);

        String d = "20";
        String e = "10";
        String f = d + e; // "2010" (como string)
        System.out.println(f);

        String g = "10";
        int h = 20;
        String i = g + h; // 1020 (como string)
        System.out.println(i);

        
        // -Caracteres especiais
        // \' ' Single quote
        // \"	" Double quote
        // \\ \ Backslash
        // \n New Line
        // \r Carriage Return
        // \t Tab
        // \b Backspace
        // \f Form Feed
        
        String txt4 = "We are the so-called \"Vikings\" from the north.";
        System.out.println(txt4);
    }
}
