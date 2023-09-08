module shift_register(
    input reset, // High(1'b1) indicates a reset condition
    input serial_clock, // MAX 8MHz
    input serial_data,
    output reg [14:0] data_out, // 15bit data
    output reg data_ready
);
    reg [14:0] shift_reg; // Shift register
    reg [3:0] bit_count;  // counter

    wire [14:0] shift_value = {shift_reg[13:0], serial_data};

    always @(posedge serial_clock or posedge reset) begin
        if (reset) begin
            data_out <= 15'd0;
            shift_reg <= 15'd0;
            data_ready <= 1'b0;
            bit_count <= 4'd0;
        end else begin
            shift_reg <= shift_value; // shift

            if (bit_count == 4'd15) begin
                data_out <= shift_value;
                data_ready <= 1'b1;
            end else begin
                data_ready <= 1'b0;
            end
            bit_count <= bit_count + 1'b1;
        end
    end
endmodule // shift_register
