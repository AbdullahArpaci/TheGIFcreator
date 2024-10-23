import imageio.v3 as iio

the_picture = "images.jpg"
the_gif =iio.imread(the_picture)
iio.imwrite('team.gif',the_gif, duration = 500, loop = 0)