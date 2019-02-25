package candlebox;



/**
 * Created by admin on 4/1/17.
 */
import java.util.Scanner;
//https://open.kattis.com/contests/naipc17-p10/problems/candlebox
public class Main {
    public static void main (final String[] args) {
        Scanner in = new Scanner(System.in);
        int D = in.nextInt();
        int Ract = in.nextInt();
        int Tact = in.nextInt();

        int C = Ract + Tact;

        //quadratic formula
        int a = 2;
        int b = 2 + 2*D;
        int c = D*D + D - 2*(C+9);

        double radicand = Math.sqrt(b*b - 4*a*c);
        int Tage = (int)Math.round((-b + radicand) / (2*a));

        int TshouldHave = (Tage*(Tage+1))/2 - 3;

        System.out.println(TshouldHave - Tact);
    }
}
