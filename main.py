

from lcapy import Circuit
one= Circuit("""
V1 1 0 5; down
R1 2 0 10; down
R2 2 1 2; right
L1 3 2 1; right
C1 0 3 2; right
;autoground= true""")

two= Circuit("""
V1 0 2 10;right
R1 3 2 2;right
L1 4 3 1;right
C1 1 4 4;right 
C2 1 0 3;down
D1 3 1;down
; autoground= true""")

three= Circuit("""
V1 1 0 25; right
R1 1 3 12; right
Q1 1 2 3; right
Q2 3 2 0; right
; autoground= true""")

four = Circuit("""
V1 1 0 20; down
R1 2 1 15; right
R2 0 2 25; right
; autoground= true""")

cct = Circuit("""
V1 1 0 {u(t)}; down
R1 1 2; right
L1 2 0; down
;autoground= true""")

DcAnalysis= Circuit("""
V1 1 0 step 10
R1 1 2 1
C1 2 0 2""")
one.draw()


"""


print(DcAnalysis.is_dc)
print(DcAnalysis.dc())
DcAnalysis.describe()
DcAnalysis.analyse()
DcAnalysis.mesh_analysis()
print(DcAnalysis.describe())
print(DcAnalysis.analyse())
print(DcAnalysis.mesh_analysis().mesh_equations_list())
"""
