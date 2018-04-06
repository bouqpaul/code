library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

use work.ual_pkg.all;

entity ual is
  port(
    a, b : in  std_logic_vector(15 downto 0);
    op   : in  opcode;
    res  : out std_logic_vector(15 downto 0)
    );
end entity;


architecture rtl of ual is
begin
  
  ual_proc : process(a, b, op)
  begin
    res <= (others=>'0');
    case op is
      when OP_ADD =>
        res <= std_logic_vector(signed(a) + signed(b));
      when OP_SUB =>
        res <= std_logic_vector(signed(a) - signed(b));
      when OP_MUL =>
        res <= std_logic_vector(resize(signed(a) * signed(b),16));
      when OP_AND =>
        res <= a and b;
      when OP_OR =>
        res <= a or b;
      when OP_XOR =>
        res <= a xor b;
      when OP_NOTA =>
        res <= not(a);
      when others =>
        null;
    end case;
  end process;

end rtl;
