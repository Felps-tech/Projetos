package Projetos.Java;
public class Produto {
    private String nome;
    private float preco;
    private int quantEstoque;

    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public float getPreco() {
        return preco;
    }
    public void setPreco(int preco) {
        this.preco = preco;
    }
    public int getQuantEstoque() {
        return quantEstoque;
    }
    public void setQuantEstoque(int quantEstoque) {
        this.quantEstoque = quantEstoque;
    }

    public float CalcularValor(){
        return preco * quantEstoque;
    }

    public void Verificação(){
        if(quantEstoque == 0){
            System.out.println("Sem produtos no estoque");
        }
        else{
            System.out.println("Quantidade de produtos no estoque: " + quantEstoque);
        }
    }
}
