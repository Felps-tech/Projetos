package Projetos.Java;
public class Aluno {
        private String nome;
        private int matricula;
        private float nota1;
        private float nota2;
        private float nota3;

        public String getNome() {
                return nome;
        }
        public void setNome(String nome) {
                this.nome = nome;
        }
        public int getMatricula() {
                return matricula;
        }
        public void setMatricula(int matricula) {
                this.matricula = matricula;
        }
        public float getNota1() {
                return nota1;
        }
        public void setNota1(float nota1) {
                this.nota1 = nota1;
        }
        public float getNota2() {
                return nota2;
        }
        public void setNota2(float nota2) {
                this.nota2 = nota2;
        }
        public float getNota3() {
                return nota3;
        }
        public void setNota3(float nota3) {
                this.nota3 = nota3;
        }

        public float Media(){
                return (nota1 + nota2 + nota3) / 3;
        }
        
        public String Situacao(){
                if (Media() >= 7) {
                return "Aprovado";
                } else {
                return "Reprovado";
                }
        }
}
