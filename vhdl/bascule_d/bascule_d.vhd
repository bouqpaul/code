library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity bascule_d is
  port(
    reset_n : in  std_logic;
    clk     : in  std_logic;
    datain  : in  std_logic_vector(7 downto 0);
    dataout : out std_logic_vector(7 downto 0)
    );
end entity;


architecture rtl of bascule_d is
  signal data : std_logic_vector(7 downto 0);
begin

  reg : process(reset_n, clk)
  begin
    if reset_n = '0' then
      data <= (others => '0');
    elsif rising_edge(clk) then
      data <= datain;
    end if;
  end process;
  
  dataout <= data;

end rtl;
