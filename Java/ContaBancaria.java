package Projetos.Java;
public class ContaBancaria {
    private int NumConta;
    private String NomeTitular;
    private double Saldo = 0;

    public int getNumConta() {
        return NumConta;
    }
    public void setNumConta(int numConta) {
        NumConta = numConta;
    }
    public String getNomeTitular() {
        return NomeTitular;
    }
    public void setNomeTitular(String nomeTitular) {
        NomeTitular = nomeTitular;
    }
    
    public void Depositar(double Dinheiro){
        Saldo += Dinheiro;
        System.out.println(Dinheiro + "R$ Foi colocado com sucesso");
    }

    public void Saque(double Dinheiro){
        if (Dinheiro < Saldo) {
            Saldo -= Dinheiro;
            System.out.println(Dinheiro + "R$ Foi retirado com sucesso");
            }
        else {
            System.out.println("Você não tem dinheiro suficiente");
            }
    }
    
}
