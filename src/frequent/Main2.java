package frequent;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.Writer;
import java.util.*;

/**
 * Created by admin on 3/25/17.
 */
//spoj FREQUENT
public class Main2 {

    public static void main (final String[] args) throws IOException {

        Scanner in = new Scanner(System.in);
        BufferedWriter out = new BufferedWriter(new PrintWriter(System.out));
        while (true) {
            //get the data
            int size = in.nextInt();
            if (size == 0) break;
            int queries = in.nextInt();
            int[] values = new int[size];
            for (int i = 0; i < size; i++) {
                values[i] = in.nextInt();
            }

            //get all nontrivial (size > 1) intervals of consecutive values
            LinkedList<Interval> intervals = new LinkedList<>();
            int prev = values[0];
            int base = 0;
            for (int i = 1; i < size; i++) {
                int current = values[i];
                if (current != prev) {
                    if (i - base >= 2)
                        intervals.add(new Interval(base, i - 1));
                    prev = current;
                    base = i;
                }
            }
            if (base != values.length) {
                Interval finalInterval = new Interval(base, values.length - 1);
                intervals.add(finalInterval);
            }





        }

    }



    public static class MyTree {
        Node root;

        public MyTree(Interval[] intervals) {
            /*
            LinkedList<Node> bottom = new LinkedList<>();
            LinkedList<Node> nextLevel = new LinkedList<>();
            while(!intervals.isEmpty()) {
                bottom.add(new Node(intervals.remove()));
            }
            Collections.sort(bottom, (Node a, Node b) -> Integer.compare(a.interval.l, b.interval.l));

            while (bottom.size() > 1) {
                while (!bottom.isEmpty()) {
                    if (bottom.size() > 2) {
                        Node lNode = bottom.removeFirst();
                        Node rNode = bottom.removeFirst();
                        nextLevel.addLast(new Node(lNode, rNode));
                    } else {
                        nextLevel.addLast(bottom.remove());
                    }
                }
                bottom = nextLevel;
                nextLevel = new LinkedList<Node>();
            }
            root = bottom.remove();
            */
            //we already know that the array is sorted from low to high
            Node[] nodes = new Node[intervals.length];
            for (int i = 0; i < intervals.length; i++) {
                nodes[i] = new Node(intervals[i]);
            }

            int base = 0;
            int cap = intervals.length;
            while (cap-base > 1) { //while we haven't converged to root
                int read = 0;
                int write = 0;
                while (read < cap) {
                    Node l = nodes[read++];
                    if (read != cap) {
                        Node r = nodes[read++];
                        nodes[write++] = new Node(l, r);
                    }
                    else {
                        nodes[write++] = l;
                    }
                }
                cap = write; //downsize cap
            }
            root = nodes[0];
        }

        int greatestInterval (Interval query) {
            return gir(query, root);
        }
        int gir (Interval query, Node currentNode) {
            if (currentNode != null) {
                if (query.intersects(currentNode.interval)) {
                    if (currentNode.r != null) { //NOT LEAF
                        return Math.max(gir(query, currentNode.r), gir(query, currentNode.l));
                    } else { //LEAF
                        return query.intersection(currentNode.interval).length();
                    }
                }
                else
                    return 1;
            }
            else return 1;
        }

        /*
        LinkedList<Interval> intersectingIntervals(Interval i) {
            LinkedList<Interval> set = new LinkedList<Interval>();
            addIntersectingIntervals(i, set, root);
            return set;
        }
        void addIntersectingIntervals(Interval i, LinkedList<Interval> set, Node str) {
            if (str != null) {
                if (i.containsPoint(str.point)) {
                    set.addAll(str.ltor); //same content as rtol, just a different ordering
                    addIntersectingIntervals(i, set, str.r);
                    addIntersectingIntervals(i, set, str.l);
                }
                else {
                    ListIterator<Interval> it;
                    Node child;
                    if (str.point < i.l) { //interval is to the right of this node
                        it = str.rtol.listIterator();
                        child = str.r;
                    }
                    else { //interval is to the left of this node
                        it = str.ltor.listIterator();
                        child = str.l;
                    }

                    while (it.hasNext()) {
                        Interval temp = it.next();
                        if (i.intersects(temp)) set.add(temp);
                        else break; //nothing after this one will intersect
                    }
                    addIntersectingIntervals(i, set, child);
                }
            }
        }
        */
    }

    public static class Node {
        Interval interval;
        Node r;
        Node l;

        public Node(Interval interval) {
            this.interval = interval;
        }

        public Node(Node l, Node r) {
            this.r=r;
            this.l=l;
            this.interval = Interval.union(l.interval, r.interval);
        }
    }

    static class Interval {
        int l;
        int r;

        public Interval(int left, int right) {
            l = left;
            r = right;
            if (l > r) throw new RuntimeException();
        }

        //assumption: intervals left and right merge to form a contiguous union
        public static Interval union(Interval left, Interval right) {
            return new Interval(left.l, right.r);
        }

        public boolean intersects (Interval other) {
            return !(l > other.r || r < other.l);
        }

        public Interval intersection(Interval other) {
            if (!intersects(other)) throw new RuntimeException();
            return new Interval(Math.max(l, other.l), Math.min(r, other.r));
        }

        public boolean containsPoint(int point) {
            return (point >= l && point <= r);
        }

        public String toString() {
            return "[" + l + ", " + r + "]";
        }

        public int length() {
            return r - l + 1;
        }
    }

}
