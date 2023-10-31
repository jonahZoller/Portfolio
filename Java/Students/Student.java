public class Student {
    
    String name = "name";
    int grade = 0;

    public Student(String newName, int newGrade){
        this.name = newName;
        this.grade = newGrade;
    }

    //getters and setters
    public void setName(String newName){
        this.name = newName;
    }

    public String getName(){
        return this.name;
    }

    public void setGrade(int newGrade){
        this.grade = newGrade;
    }

    public int getGrade(){
        return this.grade;
    }

    //toString
    @Override
    public String toString(){
        String out = "";
        out+=("name:\t"+this.name+"\n");
        out+=("grade:\t"+this.grade+"\n");

        return out;
    }

}
