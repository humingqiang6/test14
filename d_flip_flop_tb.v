// Testbench for D Flip-Flop
module d_flip_flop_tb;
  // Inputs
  reg clk;
  reg reset;
  reg d;

  // Outputs
  wire q;
  wire q_bar;

  // Instantiate the D Flip-Flop module (assuming its name is d_flip_flop)
  d_flip_flop uut (
    .clk(clk),
    .reset(reset),
    .d(d),
    .q(q),
    .q_bar(q_bar)
  );

  // Clock generation (5 time units period -> 10 time units cycle)
  initial begin
    clk = 0;
    forever #5 clk = ~clk;
  end

  // Test sequence
  initial begin
    // Initialize signals
    reset = 1;
    d = 0;
    #10; // Wait for a bit after reset assertion

    // Release reset
    reset = 0;
    #10;

    // Test data input changes
    $display("Starting D Flip-Flop test...");
    $monitor("Time: %0t, CLK: %b, RESET: %b, D: %b, Q: %b, Q_BAR: %b", $time, clk, reset, d, q, q_bar);

    // Apply test vectors
    d = 1; #20;
    d = 0; #20;
    d = 1; #20;
    d = 0; #20;

    // Apply reset again
    reset = 1; #10;
    reset = 0; #10;

    // Final test vector
    d = 1; #20;

    $display("Test completed.");
    $finish;
  end

endmodule