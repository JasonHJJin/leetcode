import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class Xorpractice {
    public static void main(String[] args) {


        // File file = new File("./p059_cipher.txt");
        // try (BufferedReader bf = new BufferedReader(new FileReader(file))) {
        //     String f = bf.readLine();
        //     String correct[] = f.split(",");
        //     int nums[] = new int[correct.length];
        //     for (int i = 0; i < correct.length; i++) {
        //         nums[i] = Integer.parseInt(correct[i]);
        //     }

        File file = new File("./p059_cipher.txt");
        try {
            
            BufferedReader in = new BufferedReader(new FileReader(file));
            String str;
            int output = 0;

            while ((str = in.readLine())!= null) {
                String[] arr = str.split(",");

                for (int i = 0; i < arr.length; i++) {
                    output = output ^ Integer.parseInt(arr[i]);
                }
                
            }
            System.out.println(output);
            in.close();
        } catch (IOException e) {
            System.out.println("File Read Error");
        }

    }
}
