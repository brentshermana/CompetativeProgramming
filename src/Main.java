import java.util.*;
import java.util.stream.IntStream;

/**
 * Created by admin on 3/2/17.
 */
//As Easy As CAB
public class Main {

    static int offset = Character.valueOf('a');
    static int index(char character) {
        return Character.valueOf(character) - offset;
    }


    public static void main (final String[] args) {
        Scanner in = new Scanner(System.in);
        char lastChar = in.next().charAt(0);

        char[] bank = new char[index(lastChar) + 1];

        char tempC = 'a';
        for (int i = 0; i < bank.length; i++) {
            bank[i] = tempC++;
        }

        String[] words = new String[Integer.parseInt(in.next())];
        for (int i = 0; i < words.length; i++) {
            words[i] = in.next();
        }

        //n strings can give us at most n-1 x:-y comparisons,
        // and we need at least bank.length - 1 comparisons to produce
        // a complete ordering

        // - we can't act on this information, because we don't yet know
        // whether the data set in ambiguous or unsatisfiable

        Hashtable<Character, BitSet> gt = new Hashtable<>(bank.length);
        Hashtable<Character, BitSet> lt = new Hashtable<>(bank.length);
        for (Character c : bank) {
            gt.put(c, new BitSet(bank.length));
            lt.put(c, new BitSet(bank.length));
        }

        //get all of the individual x>y comparisons:
        for (int i = 0; i < words.length-1; i++) {
            String first = words[i];
            String second = words[i+1];
            int len = Math.min(first.length(), second.length());
            for (int j = 0; j < len; j++) {
                if (first.charAt(j) != second.charAt(j)) {
                    char gtC = first.charAt(j);
                    char ltC = second.charAt(j);
                    gt.get(ltC).set(index(gtC), true);
                    lt.get(gtC).set(index(ltC), true);

                    break;
                }
                else if (j == len-1 && second.length() < first.length()) {
                    //all the chars that both strings have are equal,
                    // the given examples specifically say that this is bad
                    // ... not sure I agree that makes sense
                    System.out.println("IMPOSSIBLE");
                    System.exit(0);
                }
            }
        }



        /*
        System.out.println("got all comparisons:");
        for (int i = 0; i < bank.length; i++) {
            char c = bank[i];
            System.out.println("Char: " + c);

            BitSet g = gt.get(c);
            BitSet l = lt.get(c);

            IntStream git = g.stream();
            System.out.print("gt: ");
            git.forEach((int gti) -> {
                System.out.print(bank[gti]);
            });
            System.out.println();
            System.out.print("lt: ");
            IntStream lit = l.stream();
            lit.forEach((int lti) -> {
                System.out.print(bank[lti]);
            });
            System.out.println("\n============");
        }
        */


        // One of the chars should have absolutely nothing after (less than) it. Find it
        int charWithoutLt = -1;
        for (int i = 0; i < bank.length; i++) {
            char current = bank[i];
            BitSet currentLt = lt.get(current);
            if (currentLt.cardinality() == 0) {
                charWithoutLt = i;
                break;
            }
            else if (i == bank.length-1) { // all chars have a 'predecessor', so the data is inconsistent
                System.out.println("IMPOSSIBLE");
                System.exit(0);
            }
        }


        //each set in 'gt' and 'lt', ideally, is of size one, where that one element is the letter
        //immediately before/after the key for that set
        int base = charWithoutLt;
        BitSet baseSet = new BitSet(bank.length);
        List<Integer> orderedList = new ArrayList<Integer>(bank.length);
        for (int i = 0; i < bank.length-1; i++) { // last char won't have successors
            orderedList.add(base);

            baseSet.set(base, true); //add base to the set of currently inspected bases

            BitSet succSet = gt.get(bank[base]);
            IntStream successors = succSet.stream();

            successors.forEach( (int succ) -> {
                removeRedundantSuccessors(bank, gt, succSet, bank[succ], baseSet, new BitSet(bank.length));
                /*
                BitSet succSucc = gt.get(bank[succ]);

                //if base has successors whose successors overlap with the base's successors,
                // remove them from base's successors
                BitSet redundant = new BitSet(bank.length);
                redundant.or(succSet);//copy of succSet
                redundant.and(succSucc); //intersection
                succSet.xor(redundant); //removes redundancy

                //check to make sure that succ doesn't loop back to anything in baseSet
                BitSet loopBack = new BitSet(bank.length);
                loopBack.or(succSucc);
                loopBack.and(baseSet);
                if (loopBack.cardinality() > 0) {
                    System.out.println("IMPOSSIBLE");
                    System.exit(0);
                }
                */

            });


            //there should be one element in succSet remaining - the immediate successor
            if (succSet.cardinality() == 0) {
                System.out.println("AMBIGUOUS");
                System.exit(0);
            }
            else if (succSet.cardinality() == 1) {
                int newBase = succSet.stream().iterator().next();
                if (baseSet.get(newBase) == true) {
                    System.out.println("AMBIGUOUS");
                    System.exit(0);
                }
                base = newBase;
            }
            else {
                System.out.println("AMBIGUOUS");
                System.exit(0);
            }
        }
        orderedList.add(base);
        Collections.reverse(orderedList);
        for (Integer ci : orderedList) {
            System.out.print(bank[ci]);
        }
        System.out.println();


    }

    static void removeRedundantSuccessors(char[] bank, Hashtable<Character, BitSet> gt, BitSet baseSuccesssors, char tempSucc, BitSet bases, BitSet examinedSuccs) {
        examinedSuccs.set(index(tempSucc), true); //we have now examined this char

        BitSet tempSuccessors = gt.get(tempSucc);

        BitSet redundant = new BitSet(baseSuccesssors.length());
        redundant.or(tempSuccessors);
        redundant.and(baseSuccesssors);

        baseSuccesssors.xor(redundant);

        BitSet loopBack = new BitSet(baseSuccesssors.length());
        loopBack.or(bases);
        loopBack.and(tempSuccessors);

        if (loopBack.cardinality() > 0) {
            System.out.println("IMPOSSIBLE");
            System.exit(0);
        }

        //recursively call on all successors of temp:
        IntStream stream = tempSuccessors.stream();
        stream.forEach((int tempSuccSucc) -> {
            if (examinedSuccs.get(tempSuccSucc) == false)
                removeRedundantSuccessors(bank, gt, baseSuccesssors, bank[tempSuccSucc], bases, examinedSuccs);
        });
    }
}
