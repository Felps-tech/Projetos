package Projetos.Java;

public class projeto {
    public static void main(String[] args) {
        ContaBancaria Felps = new ContaBancaria();
        Felps.setNomeTitular("Felps");
        Felps.setNumConta(123123123);
        Felps.Depositar(1000.0);
        Felps.Saque(900.0);
    }
}
