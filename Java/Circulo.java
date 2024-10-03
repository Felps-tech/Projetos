package Projetos.Java;
public class Circulo {
    private double raio;
    
    private final double pi = 3.1415;
    public double CalcularArea(){
        return (pi * raio * raio);
    }
    public double CaclularPerimetro(){
        return (2 * pi * raio);
    }
    public double getRaio() {
        return raio;
    }
    public void setRaio(double raio) {
        this.raio = raio;
    }
}
