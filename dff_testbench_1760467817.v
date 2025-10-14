// Testbench for D Flip-Flop
module dff_testbench;
  reg clk;
  reg reset;
  reg d;
  wire q, q_not;

  // Instantiate the D Flip-Flop module (assuming module name is 'dff')
  dff uut (
    .clk(clk),
    .reset(reset),
    .d(d),
    .q(q),
    .q_not(q_not)
  );

  // Generate clock
  initial begin
    clk = 0;
    forever #5 clk = ~clk; // Clock period of 10 time units
  end

  // Apply test vectors
  initial begin
    // Initialize signals
    reset = 1;
    d = 0;
    #10;

    // Release reset and test
    reset = 0;
    #10;
    d = 1;
    #20;
    d = 0;
    #20;
    d = 1;
    #20;

    // Test reset
    reset = 1;
    #20;

    // Release reset again
    reset = 0;
    #20;

    $finish; // End simulation
  end

  // Monitor outputs
  initial begin
    $monitor("Time: %0t, CLK: %b, RESET: %b, D: %b, Q: %b, Q_NOT: %b", $time, clk, reset, d, q, q_not);
  end

endmodule