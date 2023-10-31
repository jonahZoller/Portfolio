import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;

public class Inventory{
    public static void main(String[] args) {
        // Program that keeps track of the animals at the vet
        // add,insert,remove,replace,clear the db
        // if the user types in quit -> the program ends
        Scanner ui = new Scanner(System.in);

        ArrayList<String> petList = new ArrayList<String>();
        String userInput = "";
        String pet = "";

        while(!userInput.equals("q")){

            System.out.println("What would you like to do? (a)dd, (i)nsert, (r)emove, re(p)lace, (c)lear, (v)iew, or (q)uit");            
            userInput = ui.nextLine();

            if(userInput.equals("a")){
                System.out.println("Enter pet: ");
                pet = ui.nextLine();
                petList.add(pet);
            }
            else if(userInput.equals("i")){
                System.out.println("Enter pet: ");
                pet = ui.nextLine();
                System.out.println("Where do you want to insert it?");
                int place = ui.nextInt();
                petList.add(place-1,pet);

            }
            else if(userInput.equals("r")){
                System.out.println("Enter pet: ");
                pet = ui.nextLine();
                petList.remove(pet);

            }
            else if(userInput.equals("p")){
                System.out.println("What pet do you want to remove: ");
                pet = ui.nextLine();
                int spot = petList.indexOf(pet);
                petList.remove(pet);

                System.out.println("What is the new pet: ");
                pet = ui.nextLine();
                petList.add(spot,pet);
            }
            else if(userInput.equals("c")){
                System.out.println("cleared");
                petList.clear();
            }
            else if(userInput.equals("v")){
                System.out.println(petList);
            }
            else if(userInput.equals("q")){
                System.out.println("bye bye");
            }


        }
        


    }
}