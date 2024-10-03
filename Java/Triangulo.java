package Projetos.Java;
public class Triangulo {
    private int cateto1;
    private int cateto2;
    private int hipotenusa;

    public int getCateto1() {
        return cateto1;
    }
    public void setCateto1(int cateto1) {
        this.cateto1 = cateto1;
    }
    public int getCateto2() {
        return cateto2;
    }
    public void setCateto2(int cateto2) {
        this.cateto2 = cateto2;
    }
    public int getHipotenusa() {
        return hipotenusa;
    }
    public void setHipotenusa(int hipotenusa) {
        this.hipotenusa = hipotenusa;
    }
    public void VerificarTriangulo(){
        if(Math.pow(hipotenusa, 2) == Math.pow(cateto1, 2) + Math.pow(cateto2, 2)){
            System.out.println("Válido");
        }else{
            System.out.println("Inválido");
        }
    }
}
