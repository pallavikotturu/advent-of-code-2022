package elves;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.Reader;
import java.util.ArrayList;
import java.util.List;

public class ElfCalorieReader {

    private final Reader reader;

    public ElfCalorieReader(Reader reader){
        this.reader = reader;
    }

    public List<Elf> readCalories() throws IOException {

        //BufferedReader = stream of lines of text
        BufferedReader bufferedReader = new BufferedReader(reader);

        List<Elf> elfList = new ArrayList<>();

        for ( String nextLine = bufferedReader.readLine();
              nextLine != null && !"".equals(nextLine);
              nextLine = bufferedReader.readLine()) {

            elfList.add(new Elf(Integer.parseInt(nextLine)));
        }

        return elfList;
    }
}
