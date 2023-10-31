import java.util.ArrayList;
public class NewLibrary {
    public static void main(String[] args) {
        ArrayList<Song> myPlaylist = new ArrayList<Song>();

        myPlaylist.add(new Song("Hold Up","Pohl",10,5));
        myPlaylist.add(new Song("Hmm Hmm Hmm", "TyMan",6,8));
        myPlaylist.add(new Song("Blake Blucken", "Chick-Filled-A",1,1.5));
        myPlaylist.add(new Song("Star Wars Last Jedi","Georgy Porgy",1,3+36/60.0));
        myPlaylist.add(new Song("Red","Spinning Chair",9.9,3+47/60.0));

        System.out.println(myPlaylist);

        //The length of our playlist
        double durationOfPlaylist = 0.0;
        for(int i = 0; i < myPlaylist.size();i++){
            durationOfPlaylist += myPlaylist.get(i).getDuration();
        }

        int secondsOfPlaylist =(int) Math.round((durationOfPlaylist - (int)(durationOfPlaylist))* 60) ;
        System.out.println((int)(durationOfPlaylist)+" minutes and "+ secondsOfPlaylist + " seconds of playlist");

        // The average of our playlist
        int seconds = (int) Math.round((durationOfPlaylist/myPlaylist.size() - (int)(durationOfPlaylist/myPlaylist.size()))* 60) ;
        System.out.println((int)(durationOfPlaylist/myPlaylist.size())+" minutes and "+ seconds +" seconds average length of songs");
    } 
}
