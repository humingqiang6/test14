import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class CalculatorAddTest {

    @Test
    public void testAdd_PositiveNumbers() {
        Calculator calc = new Calculator();
        int result = calc.add(2, 3);
        assertEquals(5, result, "2 + 3 should equal 5");
    }

    @Test
    public void testAdd_Zero() {
        Calculator calc = new Calculator();
        int result = calc.add(0, 5);
        assertEquals(5, result, "0 + 5 should equal 5");
    }

    @Test
    public void testAdd_NegativeNumbers() {
        Calculator calc = new Calculator();
        int result = calc.add(-1, -1);
        assertEquals(-2, result, "-1 + (-1) should equal -2");
    }
}