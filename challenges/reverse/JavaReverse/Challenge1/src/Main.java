import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.sql.SQLOutput;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        System.out.println("Enter the serial number: ");
        readSomething();
    }

    public static void readSomething(){
        secretFunction();
    }
    public static void readAnotherThing(){
        System.out.println("Enter the password");
        Scanner scanner = new Scanner(System.in);
        validatePassword(scanner.nextLine());
    }

    public static void secretFunction(){
        whatEvenIsBase64();
        readAnotherThing();
    }

    public static void whatEvenIsBase64(){
        ZmxhZy1Eb250UHJpbnRUaGVTdGFja1RyYWNl();
    }
    public static void validatePassword(String pwd) {
        throw new RuntimeException("This software is outdated. Current version is 0.0.1\nMost recent version is 2.2.0");
    }

    public static String ZmxhZy1Eb250UHJpbnRUaGVTdGFja1RyYWNl(){
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        return String.valueOf(a);
    }


}