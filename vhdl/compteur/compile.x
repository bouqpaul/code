rm -rf *.o
rm -rf *.ghw
ghdl -a compteur.vhd
ghdl -a compteur_tb.vhd
ghdl -a ual.vhd
ghdl -a ual_tb.vhd
ghdl -e ual_tb
ghdl -r ual_tb --wave=ual_tb.ghw
gtkwave ual_tb.ghw ual_tb.sav
