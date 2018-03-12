library ieee;
use ieee.std_logic_1164.all;

entity bascule is
generic(NB_BITS : natural := 8);
port(
	clk : in std_logic;
	input : in std_logic_vector(NB_BITS - 1 downto 0);
	output : out std_logic_vector(NB_BITS - 1 downto 0);
	reset : in std_logic
	);
end bascule;

architecture using_rising_edge of bascule is
begin

process(reset, clk)
begin
if reset = '0' then
		output <= (others => '0');

	elsif rising_edge(clk) then
		output <= input;
	end if;
end process;


end using_rising_edge;
