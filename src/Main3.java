import java.util.*;

/**
 * Created by admin on 3/3/17.
 */
public class Main3 {

    //edges point from gt -> lt


    static int offset = Character.valueOf('a');
    static int index(char character) {
        return Character.valueOf(character) - offset;
    }

    public static void main (final String[] args) {
        Scanner in = new Scanner(System.in);
        char lastChar = in.next().charAt(0);
        char[] bank = new char[index(lastChar) + 1];
        {
            char tempC = 'a';
            for (int i = 0; i < bank.length; i++) {
                bank[i] = tempC++;
            }
        }
        boolean[][] graph = new boolean[bank.length][bank.length];
        int[] inCount = new int[bank.length];
        String[] words = new String[Integer.parseInt(in.next())];
        for (int i = 0; i < words.length; i++) {
            words[i] = in.next();
        }

        //acquire comparisons
        for (int i = 0; i < words.length-1; i++) {
            String first = words[i];
            String second = words[i+1];

            int cap = Math.min(first.length(), second.length());

            for (int j = 0; j < cap; j++) {
                char gt = first.charAt(j);
                char lt = second.charAt(j);
                if (gt != lt) {
                    inCount[index(lt)]++;
                    graph[index(gt)][index(lt)] = true;
                    break;
                }
            }
        }


        ArrayList<Character> ordering = new ArrayList<>(bank.length);

        //TOPOLOGICAL SORT
        BitSet zeroIn = new BitSet(bank.length); //initialize
        for (int i = 0; i < bank.length; i++) {
            if (inCount[i] == 0) {
                zeroIn.set(i, true);
            }
        }
        while (ordering.size() < bank.length) {
            switch (zeroIn.cardinality()) {
                case 0:
                    System.out.println("IMPOSSIBLE");
                    System.exit(0);
                    break;
                case 1:
                    //remove all edges going from the str char
                    int chari = zeroIn.stream().iterator().nextInt();
                    char current = bank[chari];
                    ordering.add(current);
                    zeroIn.set(chari, false);
                    for (int to = 0; to < bank.length; to++) {
                        if (graph[chari][to] == true) {
                            graph[chari][to] = false;
                            inCount[to]--;
                            if (inCount[to] == 0)
                                zeroIn.set(to, true);
                        }
                    }
                    break;
                default:
                    System.out.println("AMBIGUOUS");
                    System.exit(0);
            }
        }

        for (int i = 0; i < ordering.size(); i++) {
            System.out.print(ordering.get(i));
        }
        System.out.println();
    }
}
