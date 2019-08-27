import ifm_contrib as ifm
from ifm import Enum
import matplotlib.pyplot as plt

doc = ifm.loadDocument("../../data/dam_seepage.fem")

doc.c.plot.faces()
#doc.c.plot.edges()
doc.c.plot.fringes(par=Enum.P_HEAD)
plt.axis("equal")