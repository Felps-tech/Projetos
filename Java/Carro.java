package Projetos.Java;
public class Carro {
    public static void main(String[] args) {
    Automóvel jorge = new Automóvel(); 
    jorge.setMarca("Fiat");
    jorge.setModelo("Uno");
    jorge.setPlaca("SAO-4O32");
    jorge.setQuantPorta(6);
    jorge.setQuilometragem(40000);
    System.out.println(jorge.getPlaca());
    System.out.println(jorge.getQuilometragem());
    System.out.println(jorge.getQuantPorta());
    System.out.println(jorge.getMarca());
    System.out.println(jorge.getModelo());
    }

}
