import java.util.*;
class Pos{
    int x;
    int y;
    int level;
    Pos(int x, int y, int level){
        this.x = x;
        this.y = y;
        this.level = level;
    }
}
class Solution {
    static int[] dx = {-1,0,1,0};
    static int[] dy = {0,1,0,-1};
    static boolean[][] visited;
    static char[][] map;

    public int bfs(int startx, int starty,int H, int W, int endx, int endy){
        Queue<Pos> q = new LinkedList<>();
        q.add(new Pos(startx, starty, 0));
        visited[startx][starty] = true;
        while(!q.isEmpty()){
            Pos now = q.poll();
            int x = now.x;
            int y = now.y;
            int level = now.level;
            if(x == endx && y == endy){
                return level;
            }
            for(int i = 0; i < 4; i++){
                int nowX = x+dx[i];
                int nowY = y+dy[i];
                if(nowX < 0 || nowX >= H || nowY < 0 || nowY >= W){
                    continue;
                }
                if(!visited[nowX][nowY] && map[nowX][nowY] != 'X'){
                    q.add(new Pos(nowX,nowY, level+1));
                    visited[nowX][nowY] = true;                    
                }
            }
        }
        return -1;
    }
    public int solution(String[] maps) {
        int answer = 0;
        map = new char[maps.length][maps[0].length()];
        visited = new boolean[map.length][map[0].length];
        Pos startPos = null;
        Pos endPos = null;
        Pos leverPos = null;
        for(int i = 0; i < maps.length; i++){
            for(int j = 0; j < maps[i].length(); j++){
                if(maps[i].charAt(j) == 'S'){
                    startPos = new Pos(i,j,0);
                }
                if(maps[i].charAt(j) == 'L'){
                    leverPos = new Pos(i,j,0);
                }
                if(maps[i].charAt(j) == 'E'){
                    endPos = new Pos(i,j,0);
                }
                map[i][j] = maps[i].charAt(j);
            }
        }
        answer = bfs(startPos.x, startPos.y, maps.length, maps[0].length(), leverPos.x, leverPos.y);
        if(answer > -1){
            visited = new boolean[map.length][map[0].length];
            int t = bfs(leverPos.x, leverPos.y, maps.length, maps[0].length(),endPos.x, endPos.y);
            if(t == -1){
                return -1;
            }
            else{
                return answer+t;
            }
        }
        return answer;
    }
}