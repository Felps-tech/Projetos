package Projetos.Java;
import java.util.List;

public class Paciente {
    private String nome;
    private int idade;
    private List<String> historicoConsultas;

    public void adicionarConsulta(String consulta) {
        historicoConsultas.add(consulta);
    }

    public void exibirConsultas() {
        if (historicoConsultas.isEmpty()) {
            System.out.println("Nenhuma consulta realizada.");
        } else {
            System.out.println("Histórico de Consultas:");
            for (String consulta : historicoConsultas) {
                System.out.println("- " + consulta);
            }
        }
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public List<String> getHistoricoConsultas() {
        return historicoConsultas;
    }

    public void setHistoricoConsultas(List<String> historicoConsultas) {
        this.historicoConsultas = historicoConsultas;
    }
}