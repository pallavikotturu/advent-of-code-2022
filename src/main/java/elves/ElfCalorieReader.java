package elves;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.Reader;
import java.util.*;

public class ElfCalorieReader {

    private final Reader reader;

    public ElfCalorieReader(Reader reader){
        this.reader = reader;
    }

    private String nextLine = "";

    public List<Elf> readElves() throws IOException {
        BufferedReader bufferedReader = new BufferedReader(reader);
        List<Elf> elfList = new ArrayList<>();

        while (hasMoreElves(bufferedReader)) {
            elfList.add(readNextElf(bufferedReader));
        }
        return elfList;
    }


    private boolean hasMoreElves(BufferedReader bufferedReader) throws IOException {
        nextLine = bufferedReader.readLine();
        return nextLine != null && !"".equals(nextLine);
    }

    private Elf readNextElf(BufferedReader bufferedReader) throws IOException {
        List<Integer> listOfCalories = new ArrayList<>();
        readAllCaloriesForOneElf(bufferedReader, listOfCalories);
        return new Elf(listOfCalories.toArray(new Integer[0]));
    }

    private void readAllCaloriesForOneElf(BufferedReader bufferedReader, List<Integer> listOfCalories) throws IOException {
        for (; nextLine != null && !nextLine.equals(""); //has calorie value
             nextLine = bufferedReader.readLine()) {
            listOfCalories.add(Integer.parseInt(nextLine));
        }
    }


    public int getOrderedCalories() throws IOException {
        List<Elf> elfList = readElves();
        TreeMap<Integer, Elf> ranking = new TreeMap<>();
        int totalCalories = 0;
        for(Elf elf: elfList){
            totalCalories = elf.getTotalCalories();
            ranking.put(totalCalories, elf);
        }
        int sum = 0;
        List<Integer> calorieList = new ArrayList<>();
        for (Integer calorieCount : ranking.descendingKeySet()) {
            sum += calorieCount;
            calorieList.add(calorieCount);
        }
        return calorieList.get(0) + calorieList.get(1) + calorieList.get(2);
    }
}
