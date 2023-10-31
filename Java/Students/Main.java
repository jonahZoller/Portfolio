import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        // Create an array list of students called classroom
        ArrayList<Student> classroom = new ArrayList<Student>(); 
        // add at least 8 students
        classroom.add(new Student("ty", 9));
        classroom.add(new Student("zander",0));
        classroom.add(new Student("blake", 10));
        classroom.add(new Student("ben", 7));
        classroom.add(new Student("Pohl",5));
        classroom.add(new Student("steckler", 107));
        classroom.add(new Student("owen", 50));
        classroom.add(new Student("sam",1));
        classroom.add(new Student("landon", 82));
        classroom.add(new Student("steckler", 107));

        // System.out.println(classroom);
        printClass(classroom);
        // minimum grade - print out the person's name
        System.out.println(minGrade(classroom));
        // max grade - print out the person's name
        System.out.println(maxGrade(classroom));

        // average grade percentage and letter grade
        System.out.println(averagePercent(classroom));
        System.out.println(averageGrade(classroom));
        // count of students
        System.out.println(classroom.size());

        // modifiy our name print outs to make sure they are Title Case
        titleCase(classroom);
        // find standard deviation in the scores
        System.out.println(stDeviation(classroom));
        // find duplicate students
        duplicate(classroom);
        // find mode of the scores (appeard the most)
    }

    public static String minGrade(ArrayList<Student> arr){
        int mingrade = Integer.MAX_VALUE;
        String minname = "";
        for(int i =0;i<arr.size();i++){
            String curname = arr.get(i).getName();
            int curgrade = arr.get(i).getGrade();
            if(curgrade<mingrade){
                mingrade = curgrade;
                minname = curname;
            }
        }
        return minname;
    }

    public static String maxGrade(ArrayList<Student> arr){
        int mingrade = Integer.MIN_VALUE;
        String minname = "";
        for(int i =0;i<arr.size();i++){
            String curname = arr.get(i).getName();
            int curgrade = arr.get(i).getGrade();
            if(curgrade>mingrade){
                mingrade = curgrade;
                minname = curname;
            }
        }
        return minname;
    }

    public static int averagePercent(ArrayList<Student> arr){
        int totalGrade = 0;
        for(int i =0;i<arr.size();i++){
            totalGrade += arr.get(i).getGrade();
        }
        int average = totalGrade/arr.size();
        return average;
    }

    public static String averageGrade(ArrayList<Student> arr){
        int totalGrade = 0;
        for(int i =0;i<arr.size();i++){
            totalGrade += arr.get(i).getGrade();
        }
        int average = totalGrade/arr.size();

        if(average>=90){
            return "A";
        } else if(average>=80){
            return "B";
        } else if(average>=70){
            return "C";
        } else if(average>=60){
            return "D";
        } else{
            return "F";
        }
    }

    public static void titleCase(ArrayList<Student> arr){
        for(int i =0;i<arr.size();i++){
            String curName = arr.get(i).getName();
            String firstLetter = curName.substring(0,1).toUpperCase(); 
            String restWord = curName.substring(1, curName.length());

            arr.get(i).setName(firstLetter+restWord);
        }
    }

    public static double stDeviation(ArrayList<Student> arr){
        double mean = Double.valueOf(averagePercent(arr));
        double totalDev = 0;
        for(int i =0;i<arr.size();i++){
            totalDev = Math.pow(arr.get(i).getGrade()-mean, 2);
        }
        return Math.sqrt(totalDev/arr.size());
    } 

   
    public static void duplicate(ArrayList<Student> arr){
        for(int i =0;i<arr.size();i++){
            String curName = arr.get(i).getName();
            for(int w =0;w<arr.size();w++){
                String compName = arr.get(w).getName();
                if(curName.equals(compName) && (w!=i)){
                    System.out.println("There was a duplicate of "+compName);
                    arr.remove(w);
                }
            }
        }
    }

//     public static int mode(ArrayList<Integer> temp){
//         //finding the most frequent number
//         //find the unique values....
//         ArrayList<Integer> uniqueList = new ArrayList<Integer>();
//         uniqueList=removeDuplicates(temp);

//         //create a list of 0's that will count the amount of items in unique list
//         ArrayList<Integer> countList = new ArrayList<Integer>();
//         // countList=createArrayList(new int[uniqueList.size()]);
//         //for each for loop
//         for(int n: uniqueList){            //for(item in uniqueList)
//              countList.add(0);
//         }

//         //iterate through the uniqueList and count the frequency...
//         for(int n:uniqueList){
//              int c = count(temp,n);
//              countList.set(uniqueList.indexOf(n),c);
//         }

//         //find the max value in the countList
//         int modeValue = maxIntAL(countList);

//         //set mode to the index of uniqueList[countList]
//         int mode = uniqueList.get(countList.get(modeValue));

//         return mode;
//    }

    public static void printClass(ArrayList<Student> arr){
        for(int i =0;i<arr.size();i++){
            System.out.println(arr.get(i));
        }
    }
}
