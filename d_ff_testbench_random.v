// Тестовая плата для D-триггера
`timescale 1ns / 1ps

module d_ff_testbench;
    reg clk;
    reg reset;
    reg d;
    wire q, q_not;

    // Подключение тестируемого модуля (предполагаем, что он называется d_ff)
    d_ff uut (
        .clk(clk),
        .reset(reset),
        .d(d),
        .q(q),
        .q_not(q_not)
    );

    // Генерация тактового сигнала
    initial begin
        clk = 0;
        forever #5 clk = ~clk; // Тактовый период 10 (изменение каждые 5)
    end

    // Сценарий теста
    initial begin
        // Инициализация
        reset = 1;
        d = 0;
        #10;

        // Сброс
        reset = 0;
        #10;

        // Проверка установки в 1
        d = 1;
        #10;

        // Проверка удержания 1
        d = 1;
        #10;

        // Проверка сброса в 0
        d = 0;
        #10;

        // Проверка удержания 0
        d = 0;
        #10;

        // Проверка быстрого переключения
        d = 1;
        #5;
        d = 0;
        #5;
        d = 1;
        #5;

        // Завершение
        #20;
        $finish;
    end

    // Мониторинг сигналов
    initial begin
        $monitor("Time: %0t, CLK: %b, RESET: %b, D: %b, Q: %b, Q_NOT: %b", $time, clk, reset, d, q, q_not);
    end

endmodule