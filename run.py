# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    run.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: scollet <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/11/18 15:52:39 by scollet           #+#    #+#              #
#    Updated: 2017/11/18 15:52:41 by scollet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import classes
import os

EPOCHS = 1

def run(args, network):
    if args[1] == '--train' and len(args) == 2:
        print "Training ..."
        for i in range(EPOCHS):
            data = np.loadtxt("data/train", delimiter=',')
            verify = np.loadtxt("data/test", delimiter=',')
            X = data[:,0:9]
            Y = data[:,9:]
            X_ = verify[:,0:9]
            Y_ = verify[:,9:]
            network.fit(X_train, Y_train, X_, Y_)
        network.save('trained.h5')
    elif args[1] == '--predict' and len(args) == 3:
		# if args[2] == '1' or args[2] == '0':
		M = [args[2]]
		P = network.predict(M)
		print P
		# else:
			# print "Error"
			# return
    else:
		print "Error"
		return
    print "Arguments Processed!"

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        network = classes.Network(9, 1)
        if os.path.exists('trained.h5'):
            network.load('trained.h5')
        run(sys.argv, network)
    else:
        print "Options: python run.py --train\n\
         python run.py --predict <values>"
