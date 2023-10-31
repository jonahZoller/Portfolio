public class Movie {
    
    String title;
    String director;
    double rate;

    public Movie(){}

    public Movie(String newTitle){
        this.title = newTitle;
    }

    public Movie(String newTitle, String newDirector){
        this.title = newTitle;
        this.director = newDirector;
    }

    public Movie(String newTitle, String newDirector, double newRate){
        this.title = newTitle;
        this.director = newDirector;
        this.rate = newRate;
    }

    @Override
    public String toString(){
        String out = "";
        out +="Title: "+this.title;
        out +="\nDirector: "+this.director;
        out +="\nRating: "+this.rate+"/10";
        
        out += "\n";    

        return out;
    }
}