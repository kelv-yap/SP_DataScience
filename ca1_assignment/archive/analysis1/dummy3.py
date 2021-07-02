import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)

x = np.random.rand(5)
y = np.random.rand(5)
names = np.array(list("ABCDE"))
# c = np.random.randint(1,5,size=5)

# norm = plt.Normalize(1,4)
# cmap = plt.cm.RdYlGn

fig,ax = plt.subplots()
sc = plt.scatter(x,y, s=100)

annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def update_annot(ind):
    pos = sc.get_offsets()[ind["ind"][0]]
    annot.xy = pos
    text = "{}, {}".format(" ".join(list(map(str,ind["ind"]))),
                           " ".join([names[n] for n in ind["ind"]]))
    annot.set_text(text)
    # annot.get_bbox_patch().set_facecolor(cmap(norm(c[ind["ind"][0]])))
    annot.get_bbox_patch().set_alpha(0.4)


def hover(event):
    print("Event: {}".format(event))
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = sc.contains(event)
        if cont:
            print("cont: {}".format(cont))
            print("ind: {}".format(ind))
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()

fig.canvas.mpl_connect("motion_notify_event", hover)

plt.show()