import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.*;

/**
 * Created by admin on 3/22/17.
 */
public class Orders {

    public static void main (final String[] args) {
        Scanner in = new Scanner(System.in);
        new Orders().runOn(in);
    }

    void runOn(Scanner in) {
        int tests = in.nextInt();
        for (int t = 0; t < tests; t++) {
            StringBuffer sb = Orders.testCase(in);
            System.out.println(sb.toString());
        }
    }

    void runToFile(File f, Scanner in) {
        try {
            FileWriter writer = new FileWriter(f);
            int tests = in.nextInt();
            for (int t = 0; t < tests; t++) {
                StringBuffer sb = Orders.testCase(in);
                writer.write(sb.toString() + "\n");
            }
            writer.close();
        }
        catch (IOException e) {
            System.out.println();
        }
    }

    static StringBuffer testCase(Scanner in) {
        int numSoldiers = in.nextInt();
        int[] soldiers = new int[numSoldiers];
        LinkedList<Interval> intervalList = new LinkedList<Interval>();
        for (int i = 0; i < numSoldiers; i++) {
            soldiers[i] = in.nextInt();
            if (soldiers[i] > 0) {
                intervalList.add(new Interval(i-soldiers[i], true, i, false));
            }
        }

        Interval[] intervals = intervalList.toArray(new Interval[intervalList.size()]);
        intervalList.clear();

        StringBuffer output = new StringBuffer();
        if (intervals.length == 0) {//just print out the trivial solution
            for (int i = 1; i <= numSoldiers; i++) {
                output.append(i);
                if (i < numSoldiers)
                    output.append(" ");
            }
        }
        else {
            SegmentTree sTree = new SegmentTree(intervals);



            for (int i = 0; i < soldiers.length; i++) {
                //TODO: THE LOGIC BELOW IS WRONG!
                int origPosition = i + 1;
                int leftMoves = soldiers[i];
                List<Interval> destInts = sTree.getIntervalsOverPoint(i-leftMoves);
                int containStart = 0;
                for (Interval interval : destInts) {
                    if (interval.containsPoint(i, true)) {
                        containStart++;
                    }
                }

                int rightMoves = containStart;

                int position = i - soldiers[i];

                soldiers[i] = origPosition - leftMoves + rightMoves;

                output.append(soldiers[i]);
                if (i < soldiers.length - 1)
                    output.append(" ");
            }
        }
        return output;
    }

    static class SegmentTree {
        //binary tree

        //leaves correspond to endpoints of the interval
        //if there are X endpoints among all the intervals, there
        //  are 2X+1 leaves, so that the tree has the following:
        //example: numX = 3: < a x1 b x2 c x3 d >
        //a,b,c,d represent any point that falls between (or outside) these intervals

        //internal nodes correspond to intervals that are a union of elementary intervals
        // simply, a non-leaf node 'n's interval is the union of its children's intervals

        //each node/leaf stores a set of intervals

        //--------------------------------

        public STNode root;
        public Interval[] intervals;

        public SegmentTree(Interval[] intervals) {
            PriorityQueue<Integer> insertionSortQueue = new PriorityQueue<Integer>(intervals.length*2);
            for (Interval i : intervals) {
                insertionSortQueue.add(i.l);
                insertionSortQueue.add(i.r);
            }

            ArrayList<Integer> endPoints = new ArrayList<Integer>();
            endPoints.add(insertionSortQueue.remove());
            while (!insertionSortQueue.isEmpty()) {
                int next = insertionSortQueue.remove();
                if (next != endPoints.get(endPoints.size()-1))
                    endPoints.add(next);
            }
            endPoints.trimToSize();

            //create the tree structure
            LinkedList<STNode> previousLayer;
            LinkedList<STNode> currentLayer = new LinkedList<STNode>();

            //initialize currentLayer with leaves
            for (int i = 0; i < endPoints.size(); i++) {
                currentLayer.addLast(new STNode(new Interval(endPoints.get(i), true, endPoints.get(i), true)));
                if (i + 1 < endPoints.size())
                    currentLayer.addLast(new STNode(new Interval(endPoints.get(i), false, endPoints.get(i+1), false)));
            }

            //generate parents until we converge to root
            while (currentLayer.size() > 1) {
                previousLayer = currentLayer;
                currentLayer = new LinkedList<>();
                //empty previousLayer into currentLayer
                while (!previousLayer.isEmpty()) {
                    if (previousLayer.size() >= 2) {
                        STNode l = previousLayer.remove();
                        STNode r = previousLayer.remove();
                        currentLayer.add(new STNode(l, r));
                    }
                    else {
                        currentLayer.add(previousLayer.remove());
                    }
                }
            }
            //currentLayer's size is 1, containing the root
            this.root = currentLayer.remove();


            //add intervals:
            this.intervals = intervals;
            for (int i = 0; i < intervals.length; i++) {
                addInterval(intervals[i], i, root);
            }
        }

        void buildTree(LinkedList<Interval> sortedIntervals) {

        }

        /*
        void recurseConstruct(ArrayList<Integer> points, STNode str, int start, int end) {
            int numElements = end - start;

            //alloc children
            str.r = new STNode(str);
            str.l = new STNode(str);

            //fill children
            if (numElements == 1) { //base case
                if (end == points.size()) {
                    //SPECIAL CASE: positive infinity to the right
                    str.r.interval = new Interval(points.get(start), false, Integer.MAX_VALUE, false);

                    str.l.r = new STNode(str);
                    str.l.l = new STNode(str);

                    str.l.r.interval = new Interval(points.get(start), true, points.get(start), true);
                    str.l.l.interval = new Interval(points.get(start-1), false, points.get(start), false);

                    str.l.interval = Interval.union(str.l.l.interval, str.l.r.interval);
                }
                else if (start == 0) {
                    //SPECIAL CASE: negative infinity to the left
                    str.r.interval = new Interval(points.get(start), true, points.get(start), true);
                    str.l.interval = new Interval(Integer.MIN_VALUE, false, points.get(start), false);
                }
                else {
                    str.r.interval = new Interval(points.get(start), true, points.get(start), true);
                    str.l.interval = new Interval(points.get(start-1), false, points.get(start), false);
                }
            }
            else {
                int mid = numElements/2 + start;
                recurseConstruct(points, str.r, start, mid);
                recurseConstruct(points, str.l, mid, end);
            }

            //Finally, union children's intervals to generate your own:
            str.interval = Interval.union(str.l.interval, str.r.interval);
        }
        */

        void addInterval(Interval interval, int index, STNode current) {
            if (interval.contains(current.interval)) {
                current.addIndex(index);
            }
            else {
                if (interval.intersects(current.r.interval)) {
                    addInterval(interval, index, current.r);
                }
                if (interval.intersects(current.l.interval)) {
                    addInterval(interval, index, current.l);
                }
            }
        }

        public List<Interval> getIntervalsOverPoint(int point) {
            List<Interval> list = new LinkedList<Interval>();
            intervalsOverPoint(point, root, list);
            return list;
        }

        private void intervalsOverPoint(int point, STNode current, List<Interval> list) {
            for (Integer i : current.indexes)
                list.add(intervals[i]);
            if (!current.isLeaf()) {
                for (STNode child : new STNode[]{current.r, current.l}) {
                    if (child.interval.containsPoint(point, true)) {
                        intervalsOverPoint(point, child, list);
                    }
                }
            }
        }

        public String toString() {
            StringBuffer sb = new StringBuffer();
            int layers = numLayers(1, root);
            sb.append("layers " + layers + "\n");

            for (int i = 1; i <= layers; i++) {
                sb.append(layerString(i, root) + "\n");
            }

            return sb.toString();
        }
        private int numLayers(int currentLayer, STNode current) {
            if (current.isLeaf()) return currentLayer;
            else return Math.max(numLayers(currentLayer+1, current.r), numLayers(currentLayer+1, current.l));
        }
        private String layerString(int layer, STNode current) {
            if (layer == 1) return current.interval.toString();
            else {
                if (current.isLeaf())
                    return "<>";
                else
                    return layerString(layer-1, root.l) + " | " + layerString(layer-1, root.r);
            }
        }
    }

    static class Interval {
        int l;
        boolean hardL;
        int r;
        boolean hardR;

        //assumption: intervals left and right merge to form a contiguous union
        public static Interval union(Interval left, Interval right) {
            return new Interval(left.l, left.hardL, right.r, right.hardR);
        }

        public Interval(int left, boolean hardLeft, int right, boolean hardRight) {
            l = left;
            r = right;
            hardL = hardLeft;
            hardR = hardRight;
        }

        public boolean contains (Interval other) {
            if (other.l < l || other.r > r) {
                return false;
            }
            if (other.l == l && other.hardL && !hardL) {
                return false;
            }
            if (other.r == r && other.hardR && !hardR) {
                return false;
            }
            return true;
        }

        public boolean intersects (Interval other) {
            return other.containsPoint(r, hardR) ||
                    other.containsPoint(l, hardL) ||
                    this.containsPoint(other.r, other.hardR) ||
                    this.containsPoint(other.l, other.hardL);
        }

        public boolean containsPoint(int point, boolean hard) {
            if (point < l || point > r) return false; //falls outside interval
            if (point == l)
                return hardL && hard;
            if (point == r)
                return hardR && hard;
            return true; //inside interval
        }

        public String toString() {
            return (hardL ? "[" : "(") + l + "," + r + (hardR ? "]" : ")");
        }
    }

    static class STNode {
        public STNode r;
        public STNode l;

        public Interval interval;

        public HashSet<Integer> indexes = new HashSet<Integer>();

        public STNode(STNode l, STNode r) {
            this.interval = Interval.union(l.interval, r.interval);
            this.l = l;
            this.r = r;
        }
        public STNode(Interval i) {
            interval = i;
        }

        public boolean isLeaf() {
            return r == null && l == null;
        }

        public void addIndex(int i) {
            indexes = new HashSet<Integer>();
            indexes.add(i);
        }
    }
}
