import sys
import numpy
import numpy.linalg
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pyplot
import fileinput


_, filename = sys.argv

""" 1. form a data matrix """

phrase_id_files = [
    't_sne.output.top100'
]
phrase_dict = {}
for line in fileinput.input(phrase_id_files):
    fields = line.split()
    phrase = fields[:-1]
    phrase_id = fields[-1].strip()
    phrase_dict[phrase_id] = ' '.join(phrase)

xs = []
ys = []
phrase_table = []
for line in open(filename):
    phrase_id, x, y = line.split('\t')
    phrase_id = phrase_id.strip()
    x = float(x)
    y = float(y)
    xs.append(x)
    ys.append(y)
    #phrase_table.append(phrase_dict[phrase_id])
    phrase_table.append(phrase_id)

png = '{}.viz.png'.format(filename)
print 'Saving the plot to:', png

fig, ax = pyplot.subplots(figsize=(70, 70))
ax.scatter(xs, ys, color='w')
for i, phrase in enumerate(phrase_table):
    ax.annotate(phrase.decode('utf-8'), (float(xs[i]), float(ys[i])), fontsize='xx-small')

ax.set_xlabel('t-sne 1', fontsize='xx-small')
ax.set_ylabel('t-sne 2', fontsize='xx-small')
ax.set_xticks([])
ax.set_yticks([])
ax.set_title(filename, fontsize='xx-small')
fig.savefig(png)
