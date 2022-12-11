package elves;

import lombok.Getter;
import lombok.Setter;

import java.util.Arrays;

@Getter
@Setter
public class Elf {

    private Integer[] calories;

    public Elf(Integer... calories){
        this.calories = calories;
    }

    @Override
    public boolean equals(Object obj) {
        return super.equals(obj);
    }

    public int getTotalCalories(){
        int total = 0;
        for (Integer calorie : calories) {
            total += calorie.intValue();
        }
        return total;
    }

    @Override
    public String toString() {
        return "Elf{" +
                "calories=" + Arrays.toString(calories) +
                '}';
    }


}
