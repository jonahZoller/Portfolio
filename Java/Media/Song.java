public class Song {

    String title, artist;
    double rating, duration;


    public Song(){

    }

    public Song(String newTitle){
        this.title = newTitle;
    }

    public Song(String newTitle, String newArtist){
        this.title = newTitle;
        this.artist = newArtist;
    }

    public Song(String newTitle, String newArtist, double newRating){
        this.title = newTitle;
        this.artist = newArtist;
        this.rating = newRating;
    }

    public Song(String newTitle,String newArtist, double newRating, double newDuration){
        this.title = newTitle;
        this.artist = newArtist;
        this.rating = newRating;
        this.duration = newDuration;
    }
    
    //getters and setters
    // accessors and mutators
    // will hvae a getter and setter for each field variable

    public void setTitle(String newTitle){
        this.title = newTitle;
    }

    public String getTitle(){
        return this.title;
    }

    public void setArtist(String newArtist){
        this.artist = newArtist;
    }

    public String getArtist(){
        return this.artist;
    }

    public void setRating(double newRating){
        this.rating = newRating;
    }

    public double getRating(){
        return this.rating;
    }

    public void setDuration(double newDuration){
        this.duration = newDuration;
    }

    public double getDuration(){
        return this.duration;
    }
    


    @Override
    public String toString(){
        String out = "";
        out +="Title: "+this.title;
        out +="\nArtist: "+this.artist;
        out +="\nRating: "+this.rating;
        out +="\nDuration: "+this.duration;
        
        out += "\n";    

        return out;
    }


}