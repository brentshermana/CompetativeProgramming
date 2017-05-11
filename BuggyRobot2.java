import java.util.PriorityQueue;
import java.util.Scanner;

/**
 * Created by brentallard on 2/16/17.
 */
public class BuggyRobot2 {

    static class QueueNode implements Comparable<QueueNode> {
        final int changes;
        final int manhattanDistance;

        final Coordinate coordinate;

        final int stringIndex;

        public QueueNode(int changes, Coordinate coordinate, int stringIndex) {
            this.changes = changes;
            this.manhattanDistance = manhattanDistance(coordinate);
            this.coordinate = coordinate;
            this.stringIndex = stringIndex;
        }

        public int compareTo(QueueNode other) {
            //Todo: what's this kind of comparison called?
            if (this.changes != other.changes) {
                return Integer.compare(this.changes, other.changes);
            }
            else {
                return Integer.compare(this.manhattanDistance, other.manhattanDistance);
            }
        }
    }

    static class Coordinate {
        final int x;
        final int y;

        public Coordinate(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object other) {
            //don't anticipate null/non-coordinate objects
            Coordinate otherC = (Coordinate)other;
            return x==otherC.x && y==otherC.y;
        }
    }

    //constants:
    static final char up = 'U';
    static final char down = 'D';
    static final char left = 'L';
    static final char right = 'R';
    static final char obstacle = '#';

    static final char start = 'R';
    static final char goal = 'E';

    //read from stdin:
    static int h;
    static int w;
    static char[][] map;
    static int startX = -1;
    static int startY = -1;
    static int goalX = -1;
    static int goalY = -1;
    static String commands;

    //other:
    static PriorityQueue<QueueNode> queue = new PriorityQueue<>();
    static int[][][] minChangesToGetHere;

    public static void main (final String[] args) {
        //long startTimeMillis = System.currentTimeMillis();

        Scanner in = new Scanner(System.in);

        //map dimensions
        h = in.nextInt();
        w = in.nextInt();
        map = new char[w][h];

        //map
        //Note how I'm setting the first index to be x, and the second to be y
        for (int y = h-1; y >= 0; y--){
            String line = in.next();
            for (int x = 0; x < w; x++) {
                map[x][y] = line.charAt(x);
                if (line.charAt(x) == start) {
                    startX = x;
                    startY = y;
                }
                else if (line.charAt(x) == goal) {
                    goalX = x;
                    goalY = y;
                }
            }
        }

        //starting commands
        commands = in.next();

        minChangesToGetHere = new int[w][h][commands.length() + 1];
        for (int x = 0; x < w; x++) {
            for (int y = 0; y < h; y++) {
                for (int z = 0; z < minChangesToGetHere[0][0].length; z++) {
                    minChangesToGetHere[x][y][z] = Integer.MAX_VALUE;
                }
            }
        }
        minChangesToGetHere[startX][startY][0] = 0;

        queue.add(new QueueNode(0, new Coordinate(startX, startY), 0));
        while (true) {
            QueueNode n = queue.remove();

            //check for success
            if (atGoal(n.coordinate)) {
                System.out.println(n.changes);
                //System.out.println((System.currentTimeMillis() - startTimeMillis) / 1000.0);
                return;
            }

            int currX = n.coordinate.x;
            int currY = n.coordinate.y;
            int currIndex = n.stringIndex;

            //ignore obsolete nodes (a better route has been found since adding to queue)
            if (minChangesToGetHere[currX][currY][currIndex] != n.changes) //CHANGE: <
                continue;

            //POSSIBILITIES:
            if (n.stringIndex < commands.length()) {
                char currentCommand = commands.charAt(n.stringIndex);
                Coordinate afterCommand = coordinateAfter(n.coordinate, currentCommand);
            //1) Make no modification, just execute the current movement
                if (minChangesToGetHere[afterCommand.x][afterCommand.y][currIndex+1] > n.changes) { //CHANGE: >=
                    minChangesToGetHere[afterCommand.x][afterCommand.y][currIndex+1] = n.changes;
                    queue.add(new QueueNode(n.changes, afterCommand, n.stringIndex + 1));
                }
            //2) Modify by removing the current char: don't move
                if (minChangesToGetHere[currX][currY][currIndex+1] > n.changes + 1) { //CHANGE: > n.changes
                    minChangesToGetHere[currX][currY][currIndex+1] = n.changes + 1;
                    queue.add(new QueueNode(n.changes + 1, n.coordinate, n.stringIndex + 1));
                }
            }
            //3) Modify by adding another command between the last one executed and the current one pointed to
            Coordinate above = coordinateAfter(n.coordinate, up);
            Coordinate below = coordinateAfter(n.coordinate, down);
            Coordinate toLeft = coordinateAfter(n.coordinate, left);
            Coordinate toRight = coordinateAfter(n.coordinate, right);
            Coordinate[] coordinatesAfterInsertions = new Coordinate[]{above, below, toLeft, toRight};
            for (int i = 0; i < coordinatesAfterInsertions.length; i++) {
                //if the movement command in consideration will be ignored due
                //  to obstacle, etc, then there's no reason to insert said command
                Coordinate newC = coordinatesAfterInsertions[i];
                //if (!newC.equals(n.coordinate)) {
                    if (minChangesToGetHere[newC.x][newC.y][n.stringIndex] > n.changes + 1) { //CHANGE: > n.changes + 1
                        minChangesToGetHere[newC.x][newC.y][n.stringIndex] = n.changes+1;
                        queue.add(new QueueNode(n.changes+1, newC, n.stringIndex));
                    }
                //}
            }
        }
    }

    static int manhattanDistance(Coordinate coordinate) {
        return Math.abs(coordinate.x-goalX) + Math.abs(coordinate.y-goalY);
    }

    static Coordinate coordinateAfter(Coordinate current, char movement) {
        int x = current.x;
        int y = current.y;
        switch (movement) {
            case up:
                if (y != h-1 && map[x][y+1] != obstacle) {
                    y++;
                }
                break;
            case down:
                if (y != 0 && map[x][y-1] != obstacle) {
                    y--;
                }
                break;
            case left:
                if (x != 0 && map[x-1][y] != obstacle) {
                    x--;
                }
                break;
            case right:
                if (x != w-1 && map[x+1][y] != obstacle) {
                    x++;
                }
                break;
            default:
                throw new RuntimeException("Invalid char " + movement);
        }
        return new Coordinate(x, y);
    }

    static boolean atGoal (Coordinate coordinate) {
        return coordinate.x == goalX && coordinate.y == goalY;
    }
}
