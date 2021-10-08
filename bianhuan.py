import math
import stddraw
import stdio
import numpy

class Point2DMatrix:
    def _update_poss_byXY(self):
        tempX = self._X
        tempY = self._Y
        temp1 = numpy.empty([self._m*self._n,1],dtype=int)
        for i in range(self._m*self._n):
            temp1[i,:] = 1
        tempX = tempX.reshape(self._m*self._n,1)
        tempY = tempY.reshape(self._m*self._n,1)
        self._poss = numpy.c_[tempX,tempY,temp1]
    def _update_XY_byposs(self):
        temp_left = self._poss[:,0]
        temp_right = self._poss[:,1]
        self._X = temp_left.reshape(self._m,self._n)
        self._Y = temp_right.reshape(self._m,self._n)

    def __init__(self,cx = 0.0,cy = 0.0,w=0.0,h=0.0,m=10,n=10):
        self._cx = cx
        self._cy = cy
        self._w = w
        self._h = h
        self._m = m
        self._n = n
        self._X = numpy.empty([m,n],dtype = float)
        self._Y = numpy.empty([m,n],dtype = float)
        self._poss = numpy.empty([n*m,3],dtype = float)
        self._A = numpy.zeros([m,n],dtype = float)
        lbx = self._cx - w/2
        lby = self._cy - h/2
        delta_x = w/n
        delta_y = h/n
        lbx = lbx + delta_x/2
        lby = lby + delta_y/2
        for i in range(n):
            self._X[:,[i]] = lbx + delta_x*i
        for j in range(m):
            self._Y[[j],:] = lby + delta_y*j
        self._update_poss_byXY()

    def set_value(self,r,c,a):
        self._A[r,c] = a

    def set_values(self,A):
        self._A = A

    def get_value(self,r,c):
        return self._A[r,c]

    def get_values(self):
        return self._A

    def m(self):
        return self._m

    def n(self):
        return self._n
    def cordi_mx(self):
        return self._poss
    def ix_pos(self,ix):
        return self._poss[ix,:]
    def row_pos(self,r):
        r_ps = []
        for j in range(self._n):
            r_ps.append((self._X[r,j],self._Y[r,j]))
        return r_ps
    def col_pos(self,c):
        c_ps = []
        for i in range(self._m):
            c_ps.append((self._X[i,c],self._Y[i,c]))
        return c_ps

    def pos(self,r,c):
        return (self._X[r,c], self._Y[r,c])

    def cs(self):
        return (self._cx,self._cy)

    def transform(self,T):
        self._poss = numpy.matmul(self._poss,T)
        return self._poss

def main():
    stddraw.setCanvasSize(600,600)
    stddraw.setXscale(-10,10)
    stddraw.setYscale(-10,10)
    m = 60
    n = 60
    pm = Point2DMatrix(0,0,3,3,m,n)

    cs = pm.cs()
    stddraw.setPenColor(stddraw.BLACK)
    for i in range(pm.m()):
        for j in range(pm.n()):
            p = pm.pos(i,j)
            stddraw.filledCircle(p[0],p[1],0.08)
    stddraw.setPenColor(stddraw.GREEN)
    stddraw.filledCircle(cs[0],cs[1],0.1)
    tx = 1
    ty = 3
    sx = 2
    sy = 2
    theta = -math.pi/6
    sT = numpy.array([[sx,0,0],[0,sy,0],[0,0,1]])
    tT = numpy.array([[1,0,0],[0,1,0],[tx,ty,1]])
    rT = numpy.array([[math.cos(theta),math.sin(theta),0],[-math.sin(theta),math.cos(theta),0],[0,0,1]])
    mT = numpy.matmul(numpy.matmul(tT,rT),sT)
    new_ps = pm.transform(mT)
    for i in range(m*n):
        stddraw.setPenColor(stddraw.RED)
        stddraw.filledCircle(new_ps[i][0],new_ps[i][1],0.1)
    stddraw.show()
if __name__ == '__main__':
    main()
