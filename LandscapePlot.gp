#GNUPLOT script to plot SI figure comparing the old and new construct
#Steven Large
#October 26th 2017
set term pdfcairo color size 10cm, 10cm
set output "Landscapes.pdf"
set border lw 0.5
set style circle radius graph 0.015

unset key
set key off

POS = "at graph 0.15,0.85 font 'Helvetica'"

MARGIN_11 = "set tmargin at screen 0.9500; set bmargin at screen 0.6832; set lmargin at screen 0.1500; set rmargin at screen 0.4170"
MARGIN_12 = "set tmargin at screen 0.9500; set bmargin at screen 0.6832; set lmargin at screen 0.4170; set rmargin at screen 0.6832"
MARGIN_13 = "set tmargin at screen 0.9500; set bmargin at screen 0.6832; set lmargin at screen 0.6832; set rmargin at screen 0.9500"

MARGIN_21 = "set tmargin at screen 0.6832; set bmargin at screen 0.4170; set lmargin at screen 0.1500; set rmargin at screen 0.4170"
MARGIN_22 = "set tmargin at screen 0.6832; set bmargin at screen 0.4170; set lmargin at screen 0.4170; set rmargin at screen 0.6832"
MARGIN_23 = "set tmargin at screen 0.6832; set bmargin at screen 0.4170; set lmargin at screen 0.6832; set rmargin at screen 0.9500"

MARGIN_31 = "set tmargin at screen 0.4170; set bmargin at screen 0.1500; set lmargin at screen 0.1500; set rmargin at screen 0.4170"
MARGIN_32 = "set tmargin at screen 0.4170; set bmargin at screen 0.1500; set lmargin at screen 0.4170; set rmargin at screen 0.6832"
MARGIN_33 = "set tmargin at screen 0.4170; set bmargin at screen 0.1500; set lmargin at screen 0.6832; set rmargin at screen 0.9500"

#--------------------- FRICTION PLOT LABELS -------------------------

#set label 11 "Separation {/Times-New-Roman-Italic X - X}_{1/2}, nm" at screen 0.550,0.55 center font "Times-New-Roman, 16"
#set label 12 "Extension {/Times-New-Roman-Italic X - X}_{1/2}, nm" at screen 0.7875,0.55 center font "Times-New-Roman, 15"

#set label 13 "τ_{relax}, ms" at screen 0.070,0.7688 center rotate by 90 font "Times-New-Roman,13"
#set label 14 "⟨δ{/Times-New-Roman-Italic F}^2⟩, pN^2" at screen 0.070,0.8813 center rotate by 90 font "Times-New-Roman,13"
#set label 15 "Friction, {/Times-New-Roman-Italic k}_B{/Times-New-Roman-Italic T} ms/nm^2" at screen 0.070,0.6563 center rotate by 90 font "Times-New-Roman,11" 

#set label 13 "τ_{relax}," at screen 0.040,0.7688 center rotate by 90 font "Times-New-Roman,16"
#set label 14 "ms" at screen 0.080,0.7688 center rotate by 90 font "Times-New-Roman,16"

#set label 15 "⟨δ{/Times-New-Roman-Italic F}^2⟩," at screen 0.040,0.8813 center rotate by 90 font "Times-New-Roman,16"
#set label 16 "pN^2" at screen 0.080,0.8813 center rotate by 90 font "Times-New-Roman,16"

#set label 17 "Friction," at screen 0.040,0.6563 center rotate by 90 font "Times-New-Roman,16"
#set label 18 "{/Times-New-Roman-Italic k}_B{/Times-New-Roman-Italic T} ms/nm^2" at screen 0.080,0.6563 center rotate by 90 font "Times-New-Roman,16"

#--------------------- PROTOCOL PLOT LABELS -------------------------

#set label 21 "Separation {/Times-New-Roman-Italic X - X}_{1/2}, nm" at screen 0.550,0.30 center font "Times-New-Roman, 16"
#set label 22 "Time {/Times-New-Roman-Italic t}/τ" at screen 0.550,0.066 center font "Times-New-Roman, 16"
#set label 23 "Separation {/Times-New-Roman-Italic X - X}_{1/2}, nm" at screen 0.070,0.1813 center rotate by 90 font "Times-New-Roman, 16"
#set label 24 "Velocity, nm/s" at screen 0.070,0.4188 center rotate by 90 font "Times-New-Roman, 16"

#OLD XDist = 0.070


#set label 25 "Rapidly relaxing hairpin" at screen 0.3375,0.970 center font "Times-New-Roman, 16"
#set label 26 "Slowly relaxing hairpin" at screen 0.7625,0.970 center font "Times-New-Roman, 16"

#------------------------ SUBPLOT LABELS ----------------------------

#set label 31 "({/Times-New-Roman-Bold A})" at screen 0.175,0.9300 center font "Times-New-Roman, 15"
#set label 32 "({/Times-New-Roman-Bold B})" at screen 0.175,0.8050 center font "Times-New-Roman, 15"
#set label 33 "({/Times-New-Roman-Bold C})" at screen 0.175,0.6925 center font "Times-New-Roman, 15"
#set label 34 "(d)" at screen 0.650,0.9300 center font "Times-New-Roman, 13"
#set label 35 "(e)" at screen 0.650,0.8050 center font "Times-New-Roman, 13"
#set label 36 "(f)" at screen 0.650,0.6925 center font "Times-New-Roman, 13"

#set label 37 "({/Times-New-Roman-Bold D})" at screen 0.175,0.4800 center font "Times-New-Roman, 15"
#set label 38 "({/Times-New-Roman-Bold E})" at screen 0.175,0.2425 center font "Times-New-Roman, 15"


set multiplot layout 3,3 rowsfirst

@MARGIN_11
set xrange[-15:15]
set yrange[-5:40]
set xtics format ""
set ytics format ""
plot "EnergyLandscapes/Landscape_Bistable_kBi_0.625.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#50000000", \
	"EnergyLandscapes/Landscape_Full_kTrap_0.025_kBi_0.625_L-10.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#50FF0000", \
	"EnergyLandscapes/Landscape_Full_kTrap_0.025_kBi_0.625_L0.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#5000FF00", \
	"EnergyLandscapes/Landscape_Full_kTrap_0.025_kBi_0.625_L10.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#500000FF"


@MARGIN_12
#set xrange[-15:15]
#set yrange[0:15]
set xrange[-15:15]
set yrange[-5:40]
set xtics format ""
set ytics format ""
plot "EnergyLandscapes/Landscape_Bistable_kBi_2.5.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#50000000", \
	"EnergyLandscapes/Landscape_Full_kTrap_0.025_kBi_2.5_L-10.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#50FF0000", \
	"EnergyLandscapes/Landscape_Full_kTrap_0.025_kBi_2.5_L0.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#5000FF00", \
	"EnergyLandscapes/Landscape_Full_kTrap_0.025_kBi_2.5_L10.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#500000FF"


@MARGIN_13
#set xrange[-15:15]
#set yrange[0:15]
set xrange[-15:15]
set yrange[-5:40]
set xtics format ""
set ytics format ""
plot "EnergyLandscapes/Landscape_Bistable_kBi_10.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#50000000", \
	"EnergyLandscapes/Landscape_Full_kTrap_0.025_kBi_10_L-10.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#50FF0000", \
	"EnergyLandscapes/Landscape_Full_kTrap_0.025_kBi_10_L0.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#5000FF00", \
	"EnergyLandscapes/Landscape_Full_kTrap_0.025_kBi_10_L10.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#500000FF"


@MARGIN_21
#set xrange[-15:15]
#set yrange[0:15]
set xrange[-15:15]
set yrange[-5:40]
set xtics format ""
set ytics format ""
plot "EnergyLandscapes/Landscape_Bistable_kBi_0.625.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#50000000", \
	"EnergyLandscapes/Landscape_Full_kTrap_0.1_kBi_0.625_L-10.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#50FF0000", \
	"EnergyLandscapes/Landscape_Full_kTrap_0.1_kBi_0.625_L0.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#5000FF00", \
	"EnergyLandscapes/Landscape_Full_kTrap_0.1_kBi_0.625_L10.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#500000FF"


@MARGIN_22
#set xrange[-15:15]
#set yrange[0:15]
set xrange[-15:15]
set yrange[-5:40]
set xtics format ""
set ytics format ""
plot "EnergyLandscapes/Landscape_Bistable_kBi_2.5.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#50000000", \
	"EnergyLandscapes/Landscape_Full_kTrap_0.1_kBi_2.5_L-10.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#50FF0000", \
	"EnergyLandscapes/Landscape_Full_kTrap_0.1_kBi_2.5_L0.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#5000FF00", \
	"EnergyLandscapes/Landscape_Full_kTrap_0.1_kBi_2.5_L10.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#500000FF"


@MARGIN_23
#set xrange[-15:15]
#set yrange[0:15]
set xrange[-15:15]
set yrange[-5:40]
set xtics format ""
set ytics format ""
plot "EnergyLandscapes/Landscape_Bistable_kBi_10.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#50000000", \
	"EnergyLandscapes/Landscape_Full_kTrap_0.1_kBi_10_L-10.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#50FF0000", \
	"EnergyLandscapes/Landscape_Full_kTrap_0.1_kBi_10_L0.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#5000FF00", \
	"EnergyLandscapes/Landscape_Full_kTrap_0.1_kBi_10_L10.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#500000FF"


@MARGIN_31
#set xrange[-15:15]
#set yrange[0:15]
set xrange[-15:15]
set yrange[-5:40]
set xtics format ""
set ytics format ""
plot "EnergyLandscapes/Landscape_Bistable_kBi_0.625.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#50000000", \
	"EnergyLandscapes/Landscape_Full_kTrap_0.4_kBi_0.625_L-10.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#50FF0000", \
	"EnergyLandscapes/Landscape_Full_kTrap_0.4_kBi_0.625_L0.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#5000FF00", \
	"EnergyLandscapes/Landscape_Full_kTrap_0.4_kBi_0.625_L10.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#500000FF"


@MARGIN_32
#set xrange[-15:15]
#set yrange[0:15]
set xrange[-15:15]
set yrange[-5:40]
set xtics format ""
set ytics format ""
plot "EnergyLandscapes/Landscape_Bistable_kBi_2.5.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#50000000", \
	"EnergyLandscapes/Landscape_Full_kTrap_0.4_kBi_2.5_L-10.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#50FF0000", \
	"EnergyLandscapes/Landscape_Full_kTrap_0.4_kBi_2.5_L0.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#5000FF00", \
	"EnergyLandscapes/Landscape_Full_kTrap_0.4_kBi_2.5_L10.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#500000FF"


@MARGIN_33
#set xrange[-15:15]
#set yrange[0:15]
set xrange[-15:15]
set yrange[-5:40]
set xtics format ""
set ytics format ""
plot "EnergyLandscapes/Landscape_Bistable_kBi_10.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#50000000", \
	"EnergyLandscapes/Landscape_Full_kTrap_0.4_kBi_10_L-10.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#50FF0000", \
	"EnergyLandscapes/Landscape_Full_kTrap_0.4_kBi_10_L0.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#5000FF00", \
	"EnergyLandscapes/Landscape_Full_kTrap_0.4_kBi_10_L10.dat" using 1:2 with line ls 1 lw 1.5 lc rgb "#500000FF"



unset multiplot

