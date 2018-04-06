-----------------------------------------------------------------
-- This file was generated automatically by tb_gen Ruby utility
-- date : (d/m/y) 08/03/2018 12:37
-- Author : Jean-Christophe Le Lann - 2014
-----------------------------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity compteur_tb is
end entity;

architecture bhv of compteur_tb is

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

  signal  enable : std_logic;
  signal     msb : std_logic;

begin
  -------------------------------------------------------------------
  -- clock and reset
  -------------------------------------------------------------------
  reset_n <= '0','1' after 666 ns;

  clk <= not(clk) after HALF_PERIOD when running else clk;

  --------------------------------------------------------------------
  -- Design Under Test
  --------------------------------------------------------------------
  dut : entity work.compteur(rtl)
         port map (
  	   reset_n => reset_n,
	   clk     => clk,
	   enable  => enable,
	   msb     => msb);

  --------------------------------------------------------------------
  -- sequential stimuli
  --------------------------------------------------------------------
  stim : process
   begin
     report "running testbench for compteur(rtl)";
     report "waiting for asynchronous reset";
     wait until reset_n='1';
     wait_cycles(100);
     report "applying stimuli...";
     wait_cycles(100);
     report "end of simulation";
     running <=false;
     wait;
   end process;

end bhv;
