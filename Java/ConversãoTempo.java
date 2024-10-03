package Projetos.Java;

import java.util.*;

public class ConversãoTempo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tempo, hora, minuto;
        hora = minuto = 0;
        tempo = sc.nextInt();
        while (tempo >= 3600) {
            tempo -= 3600;
            hora++;
        }
        while (tempo >= 60) {
            tempo -= 60;
            minuto++;
        }
        System.out.printf("%d:%d:%d\n",hora,minuto,tempo);
        sc.close();
    }
}
