import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random



fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

xs =[]
ys =[]

for i in range(1,300):
	xs.append(i)
	ys.append(random.random())

def animate(i):

	del ys[0]
	ys.append(random.random())
	ax1.clear()
	ax1.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, interval=200)
plt.show()



