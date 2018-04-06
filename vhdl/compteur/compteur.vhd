library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity compteur is
  generic(N : natural := 27);
  port(
    reset_n : in  std_logic;
    clk     : in  std_logic;
    enable  : in std_logic;
    msb     : out std_logic
    );
end entity;


architecture top of compteur is
  signal value : unsigned(N-1 downto 0);
begin

  counter : process(reset_n, clk)
  begin
    if reset_n = '0' then
      value <= to_unsigned(0,N);
    elsif rising_edge(clk) then
      if enable = '1' then
        value <= value+1;
      end if;
    end if;
  end process;

  MSB <= value(N-1);

end top;
