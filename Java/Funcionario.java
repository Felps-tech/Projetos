package Projetos.Java;

public class Funcionario {
    private String nome;
    private double salarioBruto;
    private String cargo;
    
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getSalarioBruto() {
        return salarioBruto;
    }

    public void setSalarioBruto(double salarioBruto) {
        this.salarioBruto = salarioBruto;
    }

    public String getCargo() {
        return cargo;
    }

    public void setCargo(String cargo) {
        this.cargo = cargo;
    }

    public double calcularSalarioLiquido(double descontos, double beneficios) {
        double salarioLiquido = salarioBruto - descontos + beneficios;
        return salarioLiquido;
    }

    public double calcularDescontoImposto(double taxaImposto) {
        return salarioBruto * taxaImposto;
    }
}
