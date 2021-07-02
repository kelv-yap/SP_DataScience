from pylab import *

# from http://matplotlib.org/examples/pylab_examples/boxplot_demo.html

# fake up some data
spread= rand(50) * 100
center = ones(25) * 50
flier_high = rand(10) * 100 + 100
flier_low = rand(10) * -100
data =concatenate((spread, center, flier_high, flier_low), 0)

# fake up some more data
spread= rand(50) * 100
center = ones(25) * 40
flier_high = rand(10) * 100 + 100
flier_low = rand(10) * -100
d2 = concatenate( (spread, center, flier_high, flier_low), 0 )
data.shape = (-1, 1)
d2.shape = (-1, 1)
#data = concatenate( (data, d2), 1 )
# Making a 2-D array only works if all the columns are the
# same length.  If they are not, then use a list instead.
# This is actually more efficient because boxplot converts
# a 2-D array into a list of vectors internally anyway.
data = [data, d2, d2[::2,0]]

# multiple box plots on one figure
figure()

# get dictionary returned from boxplot
bp_dict = boxplot(data, vert=False)

for line in bp_dict['medians']:
    # get position data for median line
    x, y = line.get_xydata()[1] # top of median line
    # overlay median value
    text(x, y, '%.1f' % x,
         horizontalalignment='center') # draw above, centered

for line in bp_dict['boxes']:
    x, y = line.get_xydata()[0] # bottom of left line
    text(x,y, '%.1f' % x,
         horizontalalignment='center', # centered
         verticalalignment='top')      # below
    x, y = line.get_xydata()[3] # bottom of right line
    text(x,y, '%.1f' % x,
         horizontalalignment='center', # centered
             verticalalignment='top')      # below

show()