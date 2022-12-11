package elves;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.FileReader;
import java.io.IOException;
import java.io.StringReader;
import java.util.List;

public class ElfCalorieReaderTest {

    private ElfCalorieReader classUnderTest;

    @Test
    void testReturnFirstCalories() throws IOException {
        String inputFileContents = "4601";
        classUnderTest = new ElfCalorieReader(new StringReader(inputFileContents));
        Assertions.assertEquals(new Elf(4601).getTotalCalories(), classUnderTest.readElves().get(0).getTotalCalories());
    }

    @Test
    void testMultipleCaloriesFromOneElf() throws IOException {
        String inputFileContents = "4601\r\n1583";

        classUnderTest = new ElfCalorieReader(new StringReader(inputFileContents));

        Assertions.assertEquals(6184, classUnderTest.readElves().get(0).getTotalCalories());
    }

    @Test
    void testReturnSecondCalories() throws IOException {
        String inputFileContents = "4601\n1583\n\n5928";
        classUnderTest = new ElfCalorieReader(new StringReader(inputFileContents));
        Assertions.assertEquals(new Elf(5928).getTotalCalories(), classUnderTest.readElves().get(1).getTotalCalories());
    }

    @Test
    void testElfCalorieSummation(){
        Assertions.assertEquals(49333, new Elf(2345, 45654,1334).getTotalCalories());
    }

    @Test
    void testTotalNumberOfElvesInTheRealInputFile() throws Exception {
        classUnderTest = new ElfCalorieReader(new FileReader("inputFile.txt"));
        List<Elf> result = classUnderTest.readElves();
        Assertions.assertEquals(257, result.size());
    }

    @Test
    void testGetElfWithLargestTotalCalories() throws Exception{
        classUnderTest = new ElfCalorieReader(new FileReader("inputFile.txt"));
        Assertions.assertEquals(68923, classUnderTest.getElfWithLargestTotalCalories());


    }
}
