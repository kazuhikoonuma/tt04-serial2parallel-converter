TOPLEVEL = tb
TOPLEVEL_LANG = verilog
ifneq ($(GATES),yes)
VERILOG_SOURCES = $(PWD)/tb.v $(PWD)/tt_um_kazuhikoonuma_top.v $(PWD)/shift_register.v
endif
MODULE = test
SIM=icarus
include $(shell cocotb-config --makefiles)/Makefile.sim
