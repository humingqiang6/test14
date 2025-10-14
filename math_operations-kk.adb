-- math_operations-kk.adb
-- Пакет Ada для базовых математических операций

package Math_Operations is
   -- Функция для сложения двух целых чисел
   function Add(A, B: Integer) return Integer;

   -- Функция для вычитания двух целых чисел
   function Subtract(A, B: Integer) return Integer;

   -- Функция для умножения двух целых чисел
   function Multiply(A, B: Integer) return Integer;

   -- Функция для деления двух целых чисел (с проверкой деления на ноль)
   function Divide(A, B: Integer) return Float;

   -- Процедура для печати результата
   procedure Print_Result(S: String; R: Float);
end Math_Operations;

package body Math_Operations is
   function Add(A, B: Integer) return Integer is
   begin
      return A + B;
   end Add;

   function Subtract(A, B: Integer) return Integer is
   begin
      return A - B;
   end Subtract;

   function Multiply(A, B: Integer) return Integer is
   begin
      return A * B;
   end Multiply;

   function Divide(A, B: Integer) return Float is
   begin
      if B = 0 then
         raise Constraint_Error with "Division by zero";
      end if;
      return Float(A) / Float(B);
   end Divide;

   procedure Print_Result(S: String; R: Float) is
   begin
      Put_Line(S & Float'Image(R));
   end Print_Result;

end Math_Operations;