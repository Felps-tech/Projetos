package Projetos.Java;
public class Retangulo {
    private double Largura;
    private double Comprimento;
    public double getLargura() {
        return Largura;
    }
    public void setLargura(double largura) {
        Largura = largura;
    }
    public double getComprimento() {
        return Comprimento;
    }
    public void setComprimento(double comprimento) {
        Comprimento = comprimento;
    }
    public double CalcularArea(){
        return Largura * Comprimento;
    }   
    public double CalculaPerimetro(){
        return 2 * (Largura + Comprimento);
    }

    
}
