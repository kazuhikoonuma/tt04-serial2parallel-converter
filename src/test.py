import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, RisingEdge, FallingEdge


def oscillate_clock(signal):
    cocotb.start_soon(Clock(signal, 125, 'ns').start())  # 8MHz


async def evaluate():
    await Timer(20, units="ns")


async def rise_and_fall(signal):
    await RisingEdge(signal)
    await FallingEdge(signal)


async def send_bit(dut, bit):
    dut.serial_data.value = bit
    await evaluate()  # evaluate combinatorial logic before rising edge
    await rise_and_fall(dut.serial_clock)


@cocotb.test()
async def test_shift_register(dut):
    oscillate_clock(dut.serial_clock)  # 8MHz

    # Reset
    dut.serial_clock.value = 0
    dut.rst_n.value = 1
    dut.serial_data.value = 0
    await evaluate()
    dut.rst_n.value = 0
    await evaluate()  # initialize module
    dut.rst_n.value = 1

    # Check all reg cleared
    assert dut.tt_um_kazuhikoonuma_top.shift_register.data_out.value == 0
    assert dut.tt_um_kazuhikoonuma_top.shift_register.shift_reg.value == 0
    assert dut.tt_um_kazuhikoonuma_top.shift_register.data_ready.value == 0
    assert dut.tt_um_kazuhikoonuma_top.shift_register.bit_count.value == 0

    # Write 0x55AA
    await send_bit(dut, 0)  # MSB
    await send_bit(dut, 1)
    await send_bit(dut, 0)
    await send_bit(dut, 1)
    await send_bit(dut, 0)
    await send_bit(dut, 1)
    await send_bit(dut, 0)
    await send_bit(dut, 1)
    await send_bit(dut, 1)
    await send_bit(dut, 0)
    await send_bit(dut, 1)
    await send_bit(dut, 0)
    await send_bit(dut, 1)
    await send_bit(dut, 0)
    await send_bit(dut, 1)
    assert dut.parallel_data_out.value == 0
    assert dut.data_ready.value == 0
    await send_bit(dut, 0)  # LSB (complete 16bit)
    assert dut.tt_um_kazuhikoonuma_top.shift_register.data_out.value == 0x55AA
    assert dut.parallel_data_out.value == 0x55AA
    assert dut.data_ready.value == 1

    # Write 0xAA55
    await send_bit(dut, 1)  # MSB
    await send_bit(dut, 0)
    await send_bit(dut, 1)
    await send_bit(dut, 0)
    await send_bit(dut, 1)
    await send_bit(dut, 0)
    await send_bit(dut, 1)
    await send_bit(dut, 0)
    await send_bit(dut, 0)
    await send_bit(dut, 1)
    await send_bit(dut, 0)
    await send_bit(dut, 1)
    await send_bit(dut, 0)
    await send_bit(dut, 1)
    await send_bit(dut, 0)
    assert dut.parallel_data_out.value == 0x55AA
    assert dut.data_ready.value == 0
    await send_bit(dut, 1)  # LSB (complete 16bit)
    assert dut.parallel_data_out.value == 0x2A55
    assert dut.data_ready.value == 1
