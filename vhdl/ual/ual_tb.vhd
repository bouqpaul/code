------------------------------------------------------------------------------
-- This file was partially generated automatically by tb_gen Ruby utility
-- date : (d/m/y) 08/03/2018 14:14
-- Author : Jean-Christophe Le Lann - 2014
------------------------------------------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

use work.ual_pkg.all;
use work.print_pkg.all;

entity ual_tb is
end entity;

architecture bhv of ual_tb is

  constant HALF_PERIOD : time := 5 ns;

  signal clk     : std_logic := '0';
  signal reset_n : std_logic := '0';
  signal sreset  : std_logic := '0';
  signal running : boolean   := true;

  procedure wait_cycles(n : natural) is
  begin
    for i in 1 to n loop
      wait until rising_edge(clk);
    end loop;
  end procedure;

  signal a, b : std_logic_vector(15 downto 0);
  signal op   : opcode;
  signal res  : std_logic_vector(15 downto 0);

  type stimulus is record
    a, b : std_logic_vector(15 downto 0);
    op   : opcode;
    res  : std_logic_vector(15 downto 0);
  end record;

  type stimuli_type is array(integer range <>) of stimulus;

  constant stimuli : stimuli_type := (
    0  => (op => OP_ADD, a => x"0000", b => x"0000", res => x"0000"),
    1  => (op => OP_ADD, a => x"0001", b => x"0001", res => x"0002"),
    2  => (op => OP_ADD, a => x"0abc", b => x"0def", res => x"18ab"),
    --
    3  => (op => OP_SUB, a => x"ABCD", b => x"ABCC", res => x"0001"),
    4  => (op => OP_SUB, a => x"AB00", b => x"CD00", res => x"DE00"),
    --
    5  => (op => OP_MUL, a => x"00AB", b => x"00b0", res => x"7590"),
    6  => (op => OP_MUL, a => x"AB00", b => x"CD00", res => x"0000")--strong truncation !
    );

begin
  -------------------------------------------------------------------
  -- clock and reset
  -------------------------------------------------------------------
  reset_n <= '0', '1' after 12 ns;

  clk <= not(clk) after HALF_PERIOD when running else clk;

  --------------------------------------------------------------------
  -- Design Under Test
  --------------------------------------------------------------------
  dut : entity work.ual(rtl)
    port map (
      a   => a,
      b   => b,
      op  => op,
      res => res);

  --------------------------------------------------------------------
  -- sequential stimuli
  --------------------------------------------------------------------
  stim : process
    variable success, failure_nb : natural;
    variable stim                : integer := -1;
  begin
    success    := 0;
    failure_nb := 0;
    a          <= (others=>'0');
    b          <= (others=>'0');
    op         <= OP_ADD;
    report "running testbench for ual(rtl)";
    report "waiting for asynchronous reset";
    wait until reset_n = '1';
    wait_cycles(10);
    report "applying stimuli...";
    for i in stimuli'range loop
      stim := stim+1;
      wait_cycles(1);
      a    <= stimuli(i).a;
      b    <= stimuli(i).b;
      op   <= stimuli(i).op;
      wait until falling_edge(clk);
      if res /= stimuli(i).res then
        failure_nb := failure_nb + 1;
        report("ERROR : for stimuli number " & integer'image(stim) & " (" & hstr(a) & "," & hstr(b) & "," & opcode'image(op) & ")");
        report("        Expecting " & hstr(stimuli(i).res) & ". Got " & hstr(res) & ".");
      else
        success := success+1;
      end if;
    end loop;
    report "end of simulation";
    report "number of success : " & integer'image(success);
    report "number of failure : " & integer'image(failure_nb);
    running <= false;
    wait;
  end process;

end bhv;
