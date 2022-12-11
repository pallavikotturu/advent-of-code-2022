package elves;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.FileReader;
import java.io.IOException;

public class ElfCalorieReaderTest {

    private ElfCalorieReader classUnderTest;

    @BeforeEach
    void testSomething() throws Exception {
        classUnderTest = new ElfCalorieReader(new FileReader("inputfile.txt"));
    }

    @Test
    void testReturnFirstCalories() throws IOException {
        Assertions.assertEquals(new Elf(4601), classUnderTest.readCalories().get(0));
    }

    @Test
    void testReturnSecondCalories() throws IOException {
        Assertions.assertEquals(new Elf(1583), classUnderTest.readCalories().get(1));
    }
}
