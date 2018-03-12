library ieee;
use ieee.std_logic_1164.all;

entity counter is
	generic( NB_BITS : natural :=8);
	port(
		reset_n : in std_logic;
		clk : in std_logic;
		sreset : in std_logic;
		input : in std_logic_vector(NB_BITS-1 downto 0);
		output : in std_logic_vector(NB_BITS-1 downto 0)
	);
end counter;

architecture rtl of counter is
	signal value : signed(NB_BTS - 1 downto 0);
begin

	process(reset_n, clk)
	begin
		if reset_n = '0' then
			value <= to_signed(0, NB_BTS);
		elsif rising_edge(clk) then
			if cnt_up = '1' then
				value <= value + 1;
			elsif cnt_down = '1' then
				value <= value - 1;
			end if;
		end if;
	end process;
end rtl;
