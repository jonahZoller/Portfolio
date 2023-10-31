import java.util.ArrayList;
import java.util.Scanner;

public class MediaLibrary {

    //set up IP address of your API or a user
    final static String ipAddress = "192.168.1.150";
    //static variable for the class MediaLibrary
    static ArrayList<Song> myPlaylist = new ArrayList<Song>();
    static ArrayList<Book> myBooks = new ArrayList<Book>();
    static ArrayList<Movie> myMovie = new ArrayList<Movie>();

    public static void main(String[] args) {       
        Song song1 = new Song();
        Song song2 = new Song("505","Artic Monkeys");
        Song song3 = new Song("Homecoming","Kanye West");

        myPlaylist.add(song1);myPlaylist.add(song2);myPlaylist.add(song3);

        song1.setTitle("Pride");
        song1.setArtist("Kendrick Lamar");
        song1.setRating(8);

        myPlaylist.get(1).setRating(7);
        myPlaylist.get(2).setRating(9);

        // method that automates the song creation - ask user for info
        addSong();
        addSong();

        // print out
        printPlaylist(myPlaylist);


        // method that print average rating of the playlist
        printAverageRating(myPlaylist);

        // method that finds a song -> user input and if user input is the song title, return it
        System.out.println("\n"+findASong(myPlaylist));







        myBooks.add(new Book("Beowulf",null,8.7));
        myBooks.add(new Book("Frankenstein","Mary Sullan",6.5));
        myBooks.add(new Book("Fahrenheit 451","Ray Bradbury",7.8));

        printBookshelf(myBooks);

        myMovie.add(new Movie("Dark Knight","Steven Spielsburg",9.8));
        myMovie.add(new Movie("Dark Knight","Steven Spielsburg",9.8));
        myMovie.add(new Movie("Dark Knight","Steven Spielsburg",9.8));

        printMovies(myMovie);
    }

    private static void printPlaylist(ArrayList<Song> arr){
        for(int i =0;i<arr.size();i++){
            System.out.println(arr.get(i));
        }
    }
    private static void printBookshelf(ArrayList<Book> arr){
        for(int i =0;i<arr.size();i++){
            System.out.println(arr.get(i));
        }
    }
    private static void printMovies(ArrayList<Movie> arr){
        for(int i =0;i<arr.size();i++){
            System.out.println(arr.get(i));
        }
    }

    private static void addSong(){
        Scanner ui = new Scanner(System.in);

        String titleInput = "";
        String artistInput = "";
        double ratingInput = 0;

        System.out.println("Tile of song: ");
        titleInput = ui.nextLine();
        System.out.println("Name of Artist: ");
        artistInput = ui.nextLine();
        System.out.println("What is the rating: ");
        ratingInput = ui.nextDouble();

        myPlaylist.add(new Song(titleInput, artistInput, ratingInput));


    }

    private static void printAverageRating(ArrayList<Song> arr){
        double mean = 0;
        for(int i = 0; i<arr.size();i++){
            Song son = arr.get(i);
            mean += son.getRating();

        }
        mean = mean/arr.size();

        System.out.println("Average Rating: "+mean);
    }

    private static Song findASong(ArrayList<Song> arr){
        Scanner ui = new Scanner(System.in);

        String titleInput = "";
        String titl = "";
        System.out.println("What song are you looking for? ");
        titleInput = ui.nextLine();

        for(int i = 0; i<arr.size();i++){
            titl = arr.get(i).getTitle();
            if(titl.equals(titleInput)){
                return arr.get(i);
            }
        }

        return new Song();
    }





}
