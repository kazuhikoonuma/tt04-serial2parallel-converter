![](../../workflows/gds/badge.svg) ![](../../workflows/docs/badge.svg) ![](../../workflows/wokwi_test/badge.svg)

## How it works

This project implements a serial to parallel converter tailored for efficient interfacing with systems like microcontrollers using SPI or similar communication protocols. Here's a brief overview of its operation:

1. **Input Reception**:
   - The converter continuously receives serial data, bit by bit, through the `serial_data` input.

2. **Data Conversion**: 
   - As each bit is received, it's stored in a shift register (`shift_reg`).
   - The data is shifted with every clock pulse, making room for the next incoming bit.
   - A counter (`bit_count`) keeps track of the number of bits received.

3. **Parallel Output**: 
   - Once 16 bits are accumulated, the lower 15 bits are outputted as a parallel data word through the `data_out` port. This design choice is intended to enhance compatibility with systems that transmit data in 8-bit chunks, such as SPI on microcontrollers.
   - The `data_ready` signal is asserted to indicate that the parallel data is available for reading.

The design was implemented with the aim of achieving compatibility with byte-oriented communication systems and efficient data conversion.

## How to test

Testing the serial to parallel converter is straightforward. Here's a step-by-step guide:

1. **Setup**:
   - Connect the `serial_data` input to your serial data source, such as an SPI interface of a microcontroller.

2. **Clock Configuration**:
   - Provide a clock signal to the `serial_clock` input.

3. **Resetting the Module**:
   - Initially, or whenever you want to reset the module, assert the `reset` signal high (1'b1). This will clear the internal shift register and reset the bit counter.
   - De-assert the `reset` signal (set to 1'b0) to allow normal operation.

4. **Sending Serial Data**:
   - When transmitting serial data to the module, ensure that the data is stable and ready to be sampled on the rising edge of the `serial_clock`.

5. **Reading Parallel Data**:
   - Monitor the `data_ready` signal. When it's asserted (1'b1), it indicates that a 15-bit parallel data word is available at the `data_out` port.
   - Read the data from the `data_out` port when `data_ready` is high.

6. **Observations**:
   - Ensure that the parallel data on `data_out` matches the expected conversion of the serial input.
   - Monitor the `data_ready` signal to ensure it's asserted only after every 16 bits of serial data are received.

By following these steps, you can effectively test the functionality and performance of the serial to parallel converter module.
