`timescale 1ns / 1ps

module d_flipflop_testbench_1234;

    // Объявление сигналов
    reg clk;
    reg reset;
    reg d;
    wire q;

    // Инициализация D-триггера (предполагается, что модуль d_flipflop уже существует)
    d_flipflop uut (
        .clk(clk),
        .reset(reset),
        .d(d),
        .q(q)
    );

    // Генерация тактового сигнала (период 10 нс)
    initial begin
        clk = 0;
        forever #5 clk = ~clk; // Переключение каждые 5 нс для получения периода 10 нс
    end

    // Стимулы для тестирования
    initial begin
        // Инициализация сигналов
        reset = 1;
        d = 0;
        #10; // Ждем 10 нс

        // Снятие сигнала сброса
        reset = 0;
        #10;

        // Тестирование: подача '1' на вход D
        d = 1;
        #20;

        // Тестирование: подача '0' на вход D
        d = 0;
        #20;

        // Тестирование: снова подача '1' на вход D
        d = 1;
        #20;

        // Сброс и завершение
        reset = 1;
        #10;

        $finish; // Завершить симуляцию
    end

    // Мониторинг сигналов
    initial begin
        $monitor("Time: %0t ns, CLK: %b, RESET: %b, D: %b, Q: %b", $time, clk, reset, d, q);
    end

endmodule