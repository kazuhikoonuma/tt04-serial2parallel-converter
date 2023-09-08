`default_nettype none

module tt_um_kazuhikoonuma_top #( parameter MAX_COUNT = 24'd10_000_000 ) (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Bidirectional Input path
    output wire [7:0] uio_out,  // IOs: Bidirectional Output path
    output wire [7:0] uio_oe,   // IOs: Bidirectional Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // will go high when the design is enabled
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

    wire reset = ! rst_n;

    // use bidirectionals as outputs
    assign uio_oe = 8'b11111111;

    wire [14:0] parallel_data_out;
    wire data_ready;
    assign uo_out[0] = parallel_data_out[0];
    assign uo_out[1] = parallel_data_out[1];
    assign uo_out[2] = parallel_data_out[2];
    assign uo_out[3] = parallel_data_out[3];
    assign uo_out[4] = parallel_data_out[4];
    assign uo_out[5] = parallel_data_out[5];
    assign uo_out[6] = parallel_data_out[6];
    assign uo_out[7] = parallel_data_out[7];
    assign uio_out[0] = parallel_data_out[8];
    assign uio_out[1] = parallel_data_out[9];
    assign uio_out[2] = parallel_data_out[10];
    assign uio_out[3] = parallel_data_out[11];
    assign uio_out[4] = parallel_data_out[12];
    assign uio_out[5] = parallel_data_out[13];
    assign uio_out[6] = parallel_data_out[14];
    assign uio_out[7] = data_ready;

    shift_register shift_register(
        .reset(reset),
        .serial_clock(ui_in[0]),
        .serial_data(ui_in[1]),
        .data_out(parallel_data_out),
        .data_ready(data_ready)
    );

endmodule // tt_um_kazuhikoonuma_top
