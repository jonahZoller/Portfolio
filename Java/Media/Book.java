public class Book {
    
    String title;
    String author;
    double rate;

    public Book(){}

    public Book(String newTitle){
        this.title = newTitle;
    }

    public Book(String newTitle, String newAuthor){
        this.title = newTitle;
        this.author = newAuthor;
    }

    public Book(String newTitle, String newAuthor, double newRate){
        this.title = newTitle;
        this.author = newAuthor;
        this.rate = newRate;
    }

    @Override
    public String toString(){
        String out = "";
        out +="Title: "+this.title;
        out +="\nAuthor: "+this.author;
        out +="\nRating: "+this.rate+"/10";
        
        out += "\n";    

        return out;
    }
}
