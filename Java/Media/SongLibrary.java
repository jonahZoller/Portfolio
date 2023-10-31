import java.util.ArrayList;
import java.util.Scanner;

public class SongLibrary{
    static ArrayList<Song> myPlaylist = new ArrayList<Song>();
    public static void main(String[] args) {
        Scanner ui = new Scanner(System.in);
        System.out.println("Would you like to add a song? (y/n)");
        String userinput = ui.nextLine();

        while(userinput.equals("y")){
            System.out.println("Title: ");
            String songTitle = ui.next();

            System.out.println("Artist: ");
            String songArtist = ui.next();

            System.out.println("Rating: ");
            int songRating = ui.nextInt();

            System.out.println("Duration: ");
            double songDuration = ui.nextDouble();

            myPlaylist.add(new Song(songTitle, songArtist, songRating, songDuration));

            System.out.println("Would you like to add a song? (y/n)");
            userinput = ui.next();

        }

        printPlaylist(myPlaylist);
        

        
    }

    private static void addSong(){
        
    }

    private static void printPlaylist(ArrayList<Song> arr){
        for(int i =0;i<arr.size();i++){
            System.out.println(arr.get(i));
        }
    }
}