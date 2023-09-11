# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 17:30:51 2015

@author: DIEGO
"""

import matplotlib.pyplot as plt
import math

class Circle(object):
    def __init__(self, cX, cY, radius):
        self.__cX = cX
        self.__cY = cY
        self.__radius = radius
        self.in_end_points()
        
    def in_end_points(self):
        self.__iX=self.__cX-radius
        self.__fX=self.__cX+radius
        
    def get_diameter(self):
        self.__diameter=2*self.__radius
        return self.__diameter
    
    def get_radius(self):
        return self.__radius
    
    def get_center_coordinates(self):
        return self.__cX, self.__cY
    
class Line(object):
    def __init__(self, iX, iY, fX_or_angle, fY_or_length, type_of_data):
        if type_of_data=='Point_and_Angle':
            self.__iX = iX
            self.__iY = iY
            self.__angle = fX_or_angle
            self.__length = fY_or_length
            self.in_end_points()  
            self.get_slope_value()
        elif type_of_data=='Two_Points':
            self.__iX = iX
            self.__iY = iY
            self.__fX = fX_or_angle
            self.__fY = fY_or_length
            self.get_slope_value()            
        else:
            print('Error while creating a line')
    
    def in_end_points(self):
        self.__fX=self.__iX+self.__length*math.cos(self.__angle*math.pi/float(180))
        self.__fY=self.__iY+self.__length*math.sin(self.__angle*math.pi/float(180))
        if self.__angle==90 or self.__angle==270:
            self.__fX=self.__iX          

    def get_slope_value(self):
        try:
            self.__slope=float(self.__fY-self.__iY)/float(self.__fX-self.__iX)
        except:
            self.__slope='undef'
    
    def get_inclination_angle(self):
        try:
            self.__inc_angle=math.atan(self.__slope)*180.0/math.pi
            if self.__iX > self.__fX:
                self.__inc_angle+=180
            elif self.__iX < self.__fX and self.__iY > self.__fY:
                self.__inc_angle+=360
        except:
            if self.__fY > self.__iY:
                self.__inc_angle=90
            else:
                self.__inc_angle=270
        return self.__inc_angle
    
    def get_middle_X(self):
        self.__mX=0.5*(self.__iX+self.__fX)
        return self.__mX
    
    def get_middle_Y(self):
        self.__mY=0.5*(self.__iY+self.__fY)
        return self.__mY

    def get_iX(self):
        return self.__iX
        
    def get_iY(self):
        return self.__iY
        
    def get_fX(self):
        return self.__fX
        
    def get_fY(self):
        return self.__fY
        
    def get_slope(self):
        return self.__slope
        
    def get_perpendicular_slope(self):
        if self.__slope!=0:
            if self.__slope=='undef':
                self.__perp_slope=0
            else:
                self.__perp_slope=-1.0/float(self.__slope)
        else:
            self.__perp_slope='undef'
        return self.__perp_slope
    
class My_Functions(Line):
    @staticmethod
    def x_y_intersection_points(midX1, midY1, midX2, midY2, slope1, slope2):
        try:
            if slope1!='undef' and slope2!='undef':
                x_inters=float(midY2-midY1-slope2*midX2+slope1*midX1)/float(slope1-slope2)         
                y_inters=midY1+slope1*(x_inters-midX1)
            elif slope1=='undef' and slope2!='undef':
                x_inters=midX1
                y_inters=midY2+slope2*(x_inters-midX2)
            else:
                x_inters=midX2
                y_inters=midY1+slope1*(x_inters-midX1)
            return x_inters, y_inters
        except:
            return 'inf', 'inf'  
            
    @staticmethod
    def rotate(from_ref_line, to_ref_line, rot_line, ppX, ppY):
        alfa=to_ref_line.get_inclination_angle()-from_ref_line.get_inclination_angle()
        alfa=math.fabs(alfa)
        alfa=(-1.0)*float(alfa*math.pi)/float(180)
        x_rotated=(rot_line.get_fX()-ppX)*math.cos(alfa)-(rot_line.get_fY()-ppY)*math.sin(alfa)+ppX
        y_rotated=(rot_line.get_fX()-ppX)*math.sin(alfa)+(rot_line.get_fY()-ppY)*math.cos(alfa)+ppY
        return x_rotated, y_rotated
        
    @staticmethod
    def dyadpoints(dyadline, length):
        alfa=float(dyadline.get_inclination_angle()*math.pi)/float(180)
        cCX = length*math.cos(alfa)+dyadline.get_iX()
        cCY = dyadline.get_iY()+dyadline.get_slope()*(cCX-dyadline.get_iX())
        return cCX, cCY
        
    @staticmethod
    def euclidean_distance(iX, iY, fX, fY):
        dist=math.sqrt((fX-iX)**2+(fY-iY)**2)
        return dist
        
    @staticmethod
    def dyad_adding(cplr_len, x_rot, y_rot, tnry_posX, tnry_posY):
        cplr = Line(x_rot, y_rot, tnry_posX, tnry_posY, 'Two_Points')
        cX, cY = My_Functions.dyadpoints(cplr, cplr_len)
        dyad_cplr = Line(x_rot, y_rot, cX, cY, 'Two_Points')
        rad = My_Functions.euclidean_distance(x_rot, y_rot, cplr.get_middle_X(), cplr.get_middle_Y())
        ldyad_cplr = Make_List(dyad_cplr.get_iX(), dyad_cplr.get_iY(), dyad_cplr.get_fX(), dyad_cplr.get_fY(), 'Line')
        crank=Make_List(cX, cY, rad, 'None', 'Circle')
        upper_crk=[crank.get_circle_list()[0][:], crank.get_circle_list()[1][:]]
        bottom_crk=[crank.get_circle_list()[0][:], crank.get_circle_list()[2][:]]
        return ldyad_cplr, upper_crk, bottom_crk  
        
    @staticmethod
    def on_draw(double_list,scolor,width,style,holdState=False):
        xVector=double_list[0][:]
        yVector=double_list[1][:]
        plt.plot(xVector,yVector,color=scolor,linewidth=width,linestyle=style)
        plt.grid()
        plt.axis('equal')
        plt.title('Graphical Linkage Synthesis', fontsize=20, color='red')
        plt.xlabel('X axis', fontsize=13, color='blue')
        plt.ylabel('Y axis', fontsize=13, color='blue')
        plt.figtext(0,0,"Please reference the colors as:" + " link2='blue'" + \
                        '\n' + "link3='green'" + ", link4='red'" + ", link5='cyan'" + ", link6='yellow'", fontsize=12, color='red')
        plt.show()
        #plt.hold(holdState)
        
    @staticmethod
    def get_base_linkage2PM(dpos_1, dpos_2):
        e1e2=Line(dpos_1.get_iX(), dpos_1.get_iY(), dpos_2.get_iX(), dpos_2.get_iY(), 'Two_Points')
        f1f2=Line(dpos_1.get_fX(), dpos_1.get_fY(), dpos_2.get_fX(), dpos_2.get_fY(), 'Two_Points')
        pivX, pivY = My_Functions.x_y_intersection_points(e1e2.get_middle_X(), e1e2.get_middle_Y(), + \
                                                            f1f2.get_middle_X(), f1f2.get_middle_Y(), + \
                                                            e1e2.get_perpendicular_slope(), f1f2.get_perpendicular_slope())
        lk4_pos1 = Line(pivX ,pivY, dpos_1.get_iX(), dpos_1.get_iY(), 'Two_Points')
        lk4_pos2 = Line(pivX ,pivY, dpos_2.get_iX(), dpos_2.get_iY(), 'Two_Points')
        ldpos_1=Make_List(dpos_1.get_iX(), dpos_1.get_iY(), dpos_1.get_fX(), dpos_1.get_fY(), 'Line')
        ldpos_2=Make_List(dpos_2.get_iX(), dpos_2.get_iY(), dpos_2.get_fX(), dpos_2.get_fY(), 'Line')
        le1e2=Make_List(e1e2.get_iX(), e1e2.get_iY(), e1e2.get_fX(), e1e2.get_fY(), 'Line')
        lf1f2=Make_List(f1f2.get_iX(), f1f2.get_iY(), f1f2.get_fX(), f1f2.get_fY(), 'Line')
        bis1 = Make_List(pivX, pivY, e1e2.get_middle_X(), e1e2.get_middle_Y(), 'Line')
        bis2 = Make_List(pivX, pivY, f1f2.get_middle_X(), f1f2.get_middle_Y(), 'Line')
        l_lk4_pos1 = Make_List(lk4_pos1.get_iX(), lk4_pos1.get_iY(), lk4_pos1.get_fX(), lk4_pos1.get_fY(), 'Line')
        l_lk4_pos2 = Make_List(lk4_pos2.get_iX(), lk4_pos2.get_iY(), lk4_pos2.get_fX(), lk4_pos2.get_fY(), 'Line')
        return pivX, pivY, lk4_pos1, lk4_pos2, ldpos_1, ldpos_2, le1e2, lf1f2, bis1, bis2, l_lk4_pos1, l_lk4_pos2 
        
    @staticmethod
    def get_ternary_link2PM(tnry_posX, tnry_posY, pivX, pivY, dpos_1, dpos_2, lk4_pos1, lk4_pos2):
        t_lk4_pos1 = Line(pivX, pivY, tnry_posX, tnry_posY, 'Two_Points')
        t_lk4_pos1_close = Line(tnry_posX, tnry_posY, dpos_1.get_iX(), dpos_1.get_iY(), 'Two_Points')
        x_rot, y_rot = My_Functions.rotate(lk4_pos1, lk4_pos2, t_lk4_pos1, pivX, pivY)
        t_lk4_pos2 = Line(pivX, pivY, x_rot, y_rot, 'Two_Points')
        t_lk4_pos2_close = Line(x_rot, y_rot, dpos_2.get_iX(), dpos_2.get_iY(), 'Two_Points')
        lt_lk4_pos1 = Make_List(t_lk4_pos1.get_iX(), t_lk4_pos1.get_iY(), t_lk4_pos1.get_fX(), + \
                                t_lk4_pos1.get_fY(), 'Line')
        lt_lk4_pos1_close = Make_List(t_lk4_pos1_close.get_iX(), t_lk4_pos1_close.get_iY(), + \
                                      t_lk4_pos1_close.get_fX(), t_lk4_pos1_close.get_fY(), 'Line')
        lt_lk4_pos2 = Make_List(t_lk4_pos2.get_iX(), t_lk4_pos2.get_iY(), t_lk4_pos2.get_fX(), + \
                                t_lk4_pos2.get_fY(), 'Line')
        lt_lk4_pos2_close = Make_List(t_lk4_pos2_close.get_iX(), t_lk4_pos2_close.get_iY(), + \
                                      t_lk4_pos2_close.get_fX(), t_lk4_pos2_close.get_fY(), 'Line')
        return x_rot, y_rot, t_lk4_pos1, t_lk4_pos1_close, lt_lk4_pos1, lt_lk4_pos1_close, lt_lk4_pos2, lt_lk4_pos2_close
    
    @staticmethod
    def draw_base_2PM(ldpos_1,ldpos_2,le1e2,lf1f2,bis1,bis2,l_lk4_pos1,l_lk4_pos2):
        My_Functions.on_draw(ldpos_1.get_line_list(),'red',3,'-',True)
        My_Functions.on_draw(ldpos_2.get_line_list(),'red',3,'-',True)
        My_Functions.on_draw(le1e2.get_line_list(),'gray',1,'-',True)
        My_Functions.on_draw(lf1f2.get_line_list(),'gray',1,'-',True)
        My_Functions.on_draw(bis1.get_line_list(),'black',1,'--',True)
        My_Functions.on_draw(bis2.get_line_list(),'black',1,'--',True)
        My_Functions.on_draw(l_lk4_pos1.get_line_list(),'red',3,'-',True)
        My_Functions.on_draw(l_lk4_pos2.get_line_list(),'red',3,'-',False)        
    
    @staticmethod
    def draw_2PM(ldpos_1,ldpos_2,le1e2,lf1f2,bis1,bis2,l_lk4_pos1,l_lk4_pos2,lt_lk4_pos1,lt_lk4_pos1_close,lt_lk4_pos2,lt_lk4_pos2_close,ldyad_cplr,upper_crk,bottom_crk):
        My_Functions.on_draw(ldpos_1.get_line_list(),'red',3,'-',True)
        My_Functions.on_draw(ldpos_2.get_line_list(),'red',3,'-',True)
        My_Functions.on_draw(le1e2.get_line_list(),'gray',1,'-',True)
        My_Functions.on_draw(lf1f2.get_line_list(),'gray',1,'-',True)
        My_Functions.on_draw(bis1.get_line_list(),'black',1,'--',True)
        My_Functions.on_draw(bis2.get_line_list(),'black',1,'--',True)
        My_Functions.on_draw(l_lk4_pos1.get_line_list(),'red',3,'-',True)
        My_Functions.on_draw(l_lk4_pos2.get_line_list(),'red',3,'-',True)
        My_Functions.on_draw(lt_lk4_pos1.get_line_list(),'red',3,'-',True)
        My_Functions.on_draw(lt_lk4_pos1_close.get_line_list(),'red',3,'-',True)
        My_Functions.on_draw(lt_lk4_pos2.get_line_list(),'red',3,'-',True)
        My_Functions.on_draw(lt_lk4_pos2_close.get_line_list(),'red',3,'-',True)
        My_Functions.on_draw(ldyad_cplr.get_line_list(),'green',3,'-',True)
        My_Functions.on_draw(upper_crk,'blue',3,'--',True)
        My_Functions.on_draw(bottom_crk,'blue',3,'--',False)    
    
    @staticmethod
    def get_base_linkage3PM(dpos_1, dpos_2, dpos_3):
        e1e2=Line(dpos_1.get_iX(), dpos_1.get_iY(), dpos_2.get_iX(), dpos_2.get_iY(), 'Two_Points')
        e2e3=Line(dpos_2.get_iX(), dpos_2.get_iY(), dpos_3.get_iX(), dpos_3.get_iY(), 'Two_Points')
        f1f2=Line(dpos_1.get_fX(), dpos_1.get_fY(), dpos_2.get_fX(), dpos_2.get_fY(), 'Two_Points')
        f2f3=Line(dpos_2.get_fX(), dpos_2.get_fY(), dpos_3.get_fX(), dpos_3.get_fY(), 'Two_Points')
        pivX1, pivY1 = My_Functions.x_y_intersection_points(e1e2.get_middle_X(), e1e2.get_middle_Y(), + \
                                                            e2e3.get_middle_X(), e2e3.get_middle_Y(), + \
                                                            e1e2.get_perpendicular_slope(), e2e3.get_perpendicular_slope())
        pivX2, pivY2 = My_Functions.x_y_intersection_points(f1f2.get_middle_X(), f1f2.get_middle_Y(), + \
                                                            f2f3.get_middle_X(), f2f3.get_middle_Y(), + \
                                                            f1f2.get_perpendicular_slope(), f2f3.get_perpendicular_slope())
        lk2_pos1 = Line(pivX1 ,pivY1, dpos_1.get_iX(), dpos_1.get_iY(), 'Two_Points')
        lk4_pos1 = Line(pivX2 ,pivY2, dpos_1.get_fX(), dpos_1.get_fY(), 'Two_Points')
        lk2_pos3 = Line(pivX1 ,pivY1, dpos_3.get_iX(), dpos_3.get_iY(), 'Two_Points')
        lk4_pos3 = Line(pivX2 ,pivY2, dpos_3.get_fX(), dpos_3.get_fY(), 'Two_Points')
        ldpos_1=Make_List(dpos_1.get_iX(), dpos_1.get_iY(), dpos_1.get_fX(), dpos_1.get_fY(), 'Line')
        ldpos_2=Make_List(dpos_2.get_iX(), dpos_2.get_iY(), dpos_2.get_fX(), dpos_2.get_fY(), 'Line')
        ldpos_3=Make_List(dpos_3.get_iX(), dpos_3.get_iY(), dpos_3.get_fX(), dpos_3.get_fY(), 'Line')
        le1e2=Make_List(e1e2.get_iX(), e1e2.get_iY(), e1e2.get_fX(), e1e2.get_fY(), 'Line')
        le2e3=Make_List(e2e3.get_iX(), e2e3.get_iY(), e2e3.get_fX(), e2e3.get_fY(), 'Line')
        lf1f2=Make_List(f1f2.get_iX(), f1f2.get_iY(), f1f2.get_fX(), f1f2.get_fY(), 'Line')
        lf2f3=Make_List(f2f3.get_iX(), f2f3.get_iY(), f2f3.get_fX(), f2f3.get_fY(), 'Line')
        bis1 = Make_List(pivX1, pivY1, e1e2.get_middle_X(), e1e2.get_middle_Y(), 'Line')
        bis2 = Make_List(pivX1, pivY1, e2e3.get_middle_X(), e2e3.get_middle_Y(), 'Line')
        bis3 = Make_List(pivX2, pivY2, f1f2.get_middle_X(), f1f2.get_middle_Y(), 'Line')
        bis4 = Make_List(pivX2, pivY2, f2f3.get_middle_X(), f2f3.get_middle_Y(), 'Line')
        l_lk2_pos1 = Make_List(lk2_pos1.get_iX(), lk2_pos1.get_iY(), lk2_pos1.get_fX(), lk2_pos1.get_fY(), 'Line')
        l_lk4_pos1 = Make_List(lk4_pos1.get_iX(), lk4_pos1.get_iY(), lk4_pos1.get_fX(), lk4_pos1.get_fY(), 'Line')
        l_lk2_pos3 = Make_List(lk2_pos3.get_iX(), lk2_pos3.get_iY(), lk2_pos3.get_fX(), lk2_pos3.get_fY(), 'Line')
        l_lk4_pos3 = Make_List(lk4_pos3.get_iX(), lk4_pos3.get_iY(), lk4_pos3.get_fX(), lk4_pos3.get_fY(), 'Line')
        return pivX1, pivY1, lk2_pos1, lk2_pos3, lk4_pos1, ldpos_1, ldpos_2, ldpos_3, le1e2, le2e3, lf1f2, lf2f3, bis1, bis2, bis3, bis4, l_lk2_pos1, l_lk4_pos1, l_lk2_pos3, l_lk4_pos3
    
    @staticmethod
    def get_ternary_link3PM(tnry_posX, tnry_posY, pivX1, pivY1, dpos_1, dpos_2, dpos_3, lk2_pos1, lk2_pos3, lk4_pos1):
        t_lk2_pos1 = Line(pivX1, pivY1, tnry_posX, tnry_posY, 'Two_Points')
        t_lk2_pos1_close = Line(tnry_posX, tnry_posY, dpos_1.get_iX(), dpos_1.get_iY(), 'Two_Points')
        x_rot, y_rot = My_Functions.rotate(lk2_pos1, lk2_pos3, t_lk2_pos1, pivX1, pivY1)
        t_lk2_pos3 = Line(pivX1, pivY1, x_rot, y_rot, 'Two_Points')
        t_lk2_pos3_close = Line(x_rot, y_rot, dpos_3.get_iX(), dpos_3.get_iY(), 'Two_Points')    
        lt_lk2_pos1 = Make_List(t_lk2_pos1.get_iX(), t_lk2_pos1.get_iY(), t_lk2_pos1.get_fX(), + \
                                t_lk2_pos1.get_fY(), 'Line')
        lt_lk2_pos1_close = Make_List(t_lk2_pos1_close.get_iX(), t_lk2_pos1_close.get_iY(), + \
                                      t_lk2_pos1_close.get_fX(), t_lk2_pos1_close.get_fY(), 'Line')
        lt_lk2_pos3 = Make_List(t_lk2_pos3.get_iX(), t_lk2_pos3.get_iY(), t_lk2_pos3.get_fX(), + \
                                t_lk2_pos3.get_fY(), 'Line')
        lt_lk2_pos3_close = Make_List(t_lk2_pos3_close.get_iX(), t_lk2_pos3_close.get_iY(), + \
                                      t_lk2_pos3_close.get_fX(), t_lk2_pos3_close.get_fY(), 'Line')
        return x_rot, y_rot, t_lk2_pos1, t_lk2_pos1_close, lt_lk2_pos1, lt_lk2_pos1_close, lt_lk2_pos3, lt_lk2_pos3_close           
    
    @staticmethod
    def draw_base_3PM(ldpos_1,ldpos_2,ldpos_3,le1e2,le2e3,lf1f2,lf2f3,bis1,bis2,bis3,bis4,l_lk2_pos1,l_lk4_pos1,l_lk2_pos3,l_lk4_pos3):
        My_Functions.on_draw(ldpos_1.get_line_list(),'green',3,'-',True)
        My_Functions.on_draw(ldpos_2.get_line_list(),'green',3,'-',True)
        My_Functions.on_draw(ldpos_3.get_line_list(),'green',3,'-',True)
        My_Functions.on_draw(le1e2.get_line_list(),'gray',1,'-',True)
        My_Functions.on_draw(le2e3.get_line_list(),'gray',1,'-',True)
        My_Functions.on_draw(lf1f2.get_line_list(),'gray',1,'-',True)
        My_Functions.on_draw(lf2f3.get_line_list(),'gray',1,'-',True)
        My_Functions.on_draw(bis1.get_line_list(),'black',1,'--',True)
        My_Functions.on_draw(bis2.get_line_list(),'black',1,'--',True)
        My_Functions.on_draw(bis3.get_line_list(),'black',1,'--',True)
        My_Functions.on_draw(bis4.get_line_list(),'black',1,'--',True)
        My_Functions.on_draw(l_lk2_pos1.get_line_list(),'blue',3,'-',True)
        My_Functions.on_draw(l_lk4_pos1.get_line_list(),'red',3,'-',True)
        My_Functions.on_draw(l_lk2_pos3.get_line_list(),'blue',3,'-',True)
        My_Functions.on_draw(l_lk4_pos3.get_line_list(),'red',3,'-',False)
        
    @staticmethod        
    def draw_3PM(ldpos_1,ldpos_2,ldpos_3,le1e2,le2e3,lf1f2,lf2f3,bis1,bis2,bis3,bis4,l_lk2_pos1,l_lk4_pos1,l_lk2_pos3,l_lk4_pos3,lt_lk2_pos1,lt_lk2_pos1_close,lt_lk2_pos3,lt_lk2_pos3_close,ldyad_cplr,upper_crk,bottom_crk):
        My_Functions.on_draw(ldpos_1.get_line_list(),'green',3,'-',True)
        My_Functions.on_draw(ldpos_2.get_line_list(),'green',3,'-',True)
        My_Functions.on_draw(ldpos_3.get_line_list(),'green',3,'-',True)
        My_Functions.on_draw(le1e2.get_line_list(),'gray',1,'-',True)
        My_Functions.on_draw(le2e3.get_line_list(),'gray',1,'-',True)
        My_Functions.on_draw(lf1f2.get_line_list(),'gray',1,'-',True)
        My_Functions.on_draw(lf2f3.get_line_list(),'gray',1,'-',True)
        My_Functions.on_draw(bis1.get_line_list(),'black',1,'--',True)
        My_Functions.on_draw(bis2.get_line_list(),'black',1,'--',True)
        My_Functions.on_draw(bis3.get_line_list(),'black',1,'--',True)
        My_Functions.on_draw(bis4.get_line_list(),'black',1,'--',True)
        My_Functions.on_draw(l_lk2_pos1.get_line_list(),'blue',3,'-',True)
        My_Functions.on_draw(l_lk4_pos1.get_line_list(),'red',3,'-',True)
        My_Functions.on_draw(l_lk2_pos3.get_line_list(),'blue',3,'-',True)
        My_Functions.on_draw(l_lk4_pos3.get_line_list(),'red',3,'-',True)
        My_Functions.on_draw(lt_lk2_pos1.get_line_list(),'blue',3,'-',True)
        My_Functions.on_draw(lt_lk2_pos1_close.get_line_list(),'blue',3,'-',True)
        My_Functions.on_draw(lt_lk2_pos3.get_line_list(),'blue',3,'-',True)
        My_Functions.on_draw(lt_lk2_pos3_close.get_line_list(),'blue',3,'-',True)
        My_Functions.on_draw(ldyad_cplr.get_line_list(),'cyan',3,'-',True)
        My_Functions.on_draw(upper_crk,'yellow',3,'--',True)
        My_Functions.on_draw(bottom_crk,'yellow',3,'--',False)
    
    @staticmethod
    def get_2P_linkage_results(iposX1, iposY1, incAng1, iposX2, iposY2, incAng2, link_len, tnry_posX, tnry_posY, coupler_len):
        dpos_1 = Line(iposX1, iposY1, incAng1, link_len, 'Point_and_Angle')
        dpos_2 = Line(iposX2, iposY2, incAng2, link_len, 'Point_and_Angle')
        pivX, pivY, lk4_pos1, lk4_pos2, ldpos_1, ldpos_2, le1e2, lf1f2, bis1, bis2, l_lk4_pos1, l_lk4_pos2  = My_Functions.get_base_linkage2PM(dpos_1, dpos_2)
        x_rot, y_rot, t_lk4_pos1, t_lk4_pos1_close, lt_lk4_pos1, lt_lk4_pos1_close, lt_lk4_pos2, lt_lk4_pos2_close = My_Functions.get_ternary_link2PM(tnry_posX, tnry_posY, pivX, pivY, dpos_1, dpos_2, lk4_pos1, lk4_pos2)
        cplr = Line(x_rot, y_rot, tnry_posX, tnry_posY, 'Two_Points')
        cX, cY = My_Functions.dyadpoints(cplr, coupler_len)
        rad = My_Functions.euclidean_distance(x_rot, y_rot, cplr.get_middle_X(), cplr.get_middle_Y())            
        link4x = pivX
        link4y = pivY
        link3x = dpos_1.get_iX()
        link3y = dpos_1.get_iY()
        ternary_pointx = tnry_posX
        ternary_pointy = tnry_posY
        gndpoint3x = cX
        gndpoint3y = cY        
        len_link2 = rad #This is the crank
        len_link3 = coupler_len #This is the coupler's length
        len_link4 = My_Functions.euclidean_distance(link4x, link4y, iposX1, iposY1) #This is the link 4's length        
        return link4x, link4y, link3x, link3y, ternary_pointx, ternary_pointy, gndpoint3x, gndpoint3y, len_link2, len_link3, len_link4
   
    @staticmethod
    def get_3P_linkage_results(iposX1, iposY1, incAng1, iposX2, iposY2, incAng2, iposX3, iposY3, incAng3, link_len, tnry_posX, tnry_posY, coupler_len):
        dpos_1=Line(iposX1, iposY1, incAng1, link_len,'Point_and_Angle')
        dpos_2=Line(iposX2, iposY2, incAng2, link_len,'Point_and_Angle')
        dpos_3=Line(iposX3, iposY3, incAng3, link_len,'Point_and_Angle')
        e1e2=Line(dpos_1.get_iX(), dpos_1.get_iY(), dpos_2.get_iX(), dpos_2.get_iY(), 'Two_Points')
        e2e3=Line(dpos_2.get_iX(), dpos_2.get_iY(), dpos_3.get_iX(), dpos_3.get_iY(), 'Two_Points')
        f1f2=Line(dpos_1.get_fX(), dpos_1.get_fY(), dpos_2.get_fX(), dpos_2.get_fY(), 'Two_Points')
        f2f3=Line(dpos_2.get_fX(), dpos_2.get_fY(), dpos_3.get_fX(), dpos_3.get_fY(), 'Two_Points')
        pivX1, pivY1 = My_Functions.x_y_intersection_points(e1e2.get_middle_X(), e1e2.get_middle_Y(), + \
                                                            e2e3.get_middle_X(), e2e3.get_middle_Y(), + \
                                                            e1e2.get_perpendicular_slope(), e2e3.get_perpendicular_slope())
        pivX2, pivY2 = My_Functions.x_y_intersection_points(f1f2.get_middle_X(), f1f2.get_middle_Y(), + \
                                                            f2f3.get_middle_X(), f2f3.get_middle_Y(), + \
                                                            f1f2.get_perpendicular_slope(), f2f3.get_perpendicular_slope())
        pivX1, pivY1, lk2_pos1, lk2_pos3, lk4_pos1, ldpos_1, ldpos_2, ldpos_3, le1e2, le2e3, lf1f2, lf2f3, bis1, bis2, bis3, bis4, l_lk2_pos1, l_lk4_pos1, l_lk2_pos3, l_lk4_pos3 = My_Functions.get_base_linkage3PM(dpos_1, dpos_2, dpos_3)
        x_rot, y_rot, t_lk2_pos1, t_lk2_pos1_close, lt_lk2_pos1, lt_lk2_pos1_close, lt_lk2_pos3, lt_lk2_pos3_close = My_Functions.get_ternary_link3PM(tnry_posX, tnry_posY, pivX1, pivY1, dpos_1, dpos_2, dpos_3, lk2_pos1, lk2_pos3, lk4_pos1)
        cplr = Line(x_rot, y_rot, tnry_posX, tnry_posY, 'Two_Points')
        cX, cY = My_Functions.dyadpoints(cplr, coupler_len)
        rad = My_Functions.euclidean_distance(x_rot, y_rot, cplr.get_middle_X(), cplr.get_middle_Y())            
        link2x = pivX1
        link2y = pivY1
        link3x = dpos_1.get_iX()
        link3y = dpos_1.get_iY()
        link4x = pivX2
        link4y = pivY2
        ternary_pointx = tnry_posX
        ternary_pointy = tnry_posY
        gndpoint3x = cX
        gndpoint3y = cY 
        len_link6 = rad #This is the crank
        len_link5 = coupler_len #This is the coupler's length
        len_link2 = My_Functions.euclidean_distance(link2x, link2y, iposX1, iposY1) #This is the link 2's length        
        len_link4 = My_Functions.euclidean_distance(link4x, link4y, dpos_1.get_fX(), dpos_1.get_fY())
        return link2x, link2y, link3x, link3y, link4x, link4y, ternary_pointx, ternary_pointy, gndpoint3x, gndpoint3y, len_link2, len_link4, len_link5, len_link6
        
    @staticmethod
    def get_3P_linkage_base_results(iposX1, iposY1, incAng1, iposX2, iposY2, incAng2, iposX3, iposY3, incAng3, link_len):
        dpos_1=Line(iposX1, iposY1, incAng1, link_len,'Point_and_Angle')
        dpos_2=Line(iposX2, iposY2, incAng2, link_len,'Point_and_Angle')
        dpos_3=Line(iposX3, iposY3, incAng3, link_len,'Point_and_Angle')
        e1e2=Line(dpos_1.get_iX(), dpos_1.get_iY(), dpos_2.get_iX(), dpos_2.get_iY(), 'Two_Points')
        e2e3=Line(dpos_2.get_iX(), dpos_2.get_iY(), dpos_3.get_iX(), dpos_3.get_iY(), 'Two_Points')
        f1f2=Line(dpos_1.get_fX(), dpos_1.get_fY(), dpos_2.get_fX(), dpos_2.get_fY(), 'Two_Points')
        f2f3=Line(dpos_2.get_fX(), dpos_2.get_fY(), dpos_3.get_fX(), dpos_3.get_fY(), 'Two_Points')
        pivX1, pivY1 = My_Functions.x_y_intersection_points(e1e2.get_middle_X(), e1e2.get_middle_Y(), + \
                                                            e2e3.get_middle_X(), e2e3.get_middle_Y(), + \
                                                            e1e2.get_perpendicular_slope(), e2e3.get_perpendicular_slope())
        pivX2, pivY2 = My_Functions.x_y_intersection_points(f1f2.get_middle_X(), f1f2.get_middle_Y(), + \
                                                            f2f3.get_middle_X(), f2f3.get_middle_Y(), + \
                                                            f1f2.get_perpendicular_slope(), f2f3.get_perpendicular_slope())
        link2x = pivX1
        link2y = pivY1
        link3x = dpos_1.get_iX()
        link3y = dpos_1.get_iY()
        link4x = pivX2
        link4y = pivY2
        len_link2 = My_Functions.euclidean_distance(link2x, link2y, iposX1, iposY1) #This is the link 2's length        
        len_link4 = My_Functions.euclidean_distance(link4x, link4y, dpos_1.get_fX(), dpos_1.get_fY())
        return link2x, link2y, link3x, link3y, link4x, link4y, len_link2, len_link4
        
    @staticmethod
    def design_2P__base_linkage(iposX1, iposY1, incAng1, iposX2, iposY2, incAng2, link_len):
        dpos_1 = Line(iposX1, iposY1, incAng1, link_len, 'Point_and_Angle')
        dpos_2 = Line(iposX2, iposY2, incAng2, link_len, 'Point_and_Angle')
        pivX, pivY, lk4_pos1, lk4_pos2, ldpos_1, ldpos_2, le1e2, lf1f2, bis1, bis2, l_lk4_pos1, l_lk4_pos2  = My_Functions.get_base_linkage2PM(dpos_1, dpos_2)
        My_Functions.draw_base_2PM(ldpos_1,ldpos_2,le1e2,lf1f2,bis1,bis2,l_lk4_pos1,l_lk4_pos2)
    @staticmethod
    def design_2P_complete_linkage(iposX1, iposY1, incAng1, iposX2, iposY2, incAng2, link_len, tnry_posX, tnry_posY, coupler_len):
        dpos_1 = Line(iposX1, iposY1, incAng1, link_len, 'Point_and_Angle')
        dpos_2 = Line(iposX2, iposY2, incAng2, link_len, 'Point_and_Angle')
        pivX, pivY, lk4_pos1, lk4_pos2, ldpos_1, ldpos_2, le1e2, lf1f2, bis1, bis2, l_lk4_pos1, l_lk4_pos2  = My_Functions.get_base_linkage2PM(dpos_1, dpos_2)
        x_rot, y_rot, t_lk4_pos1, t_lk4_pos1_close, lt_lk4_pos1, lt_lk4_pos1_close, lt_lk4_pos2, lt_lk4_pos2_close = My_Functions.get_ternary_link2PM(tnry_posX, tnry_posY, pivX, pivY, dpos_1, dpos_2, lk4_pos1, lk4_pos2)
        ldyad_cplr, upper_crk, bottom_crk = My_Functions.dyad_adding(coupler_len,x_rot, y_rot, tnry_posX, tnry_posY)
        My_Functions.draw_2PM(ldpos_1,ldpos_2,le1e2,lf1f2,bis1,bis2,l_lk4_pos1,l_lk4_pos2,lt_lk4_pos1,lt_lk4_pos1_close,lt_lk4_pos2,lt_lk4_pos2_close,ldyad_cplr,upper_crk,bottom_crk)
    
    @staticmethod
    def design_3P__base_linkage(iposX1, iposY1, incAng1, iposX2, iposY2, incAng2, iposX3, iposY3, incAng3, link_len):
        dpos_1=Line(iposX1, iposY1, incAng1, link_len,'Point_and_Angle')
        dpos_2=Line(iposX2, iposY2, incAng2, link_len,'Point_and_Angle')
        dpos_3=Line(iposX3, iposY3, incAng3, link_len,'Point_and_Angle')
        pivX1, pivY1, lk2_pos1, lk2_pos3, lk4_pos1, ldpos_1, ldpos_2, ldpos_3, le1e2, le2e3, lf1f2, lf2f3, bis1, bis2, bis3, bis4, l_lk2_pos1, l_lk4_pos1, l_lk2_pos3, l_lk4_pos3 = My_Functions.get_base_linkage3PM(dpos_1, dpos_2, dpos_3)
        My_Functions.draw_base_3PM(ldpos_1,ldpos_2,ldpos_3,le1e2,le2e3,lf1f2,lf2f3,bis1,bis2,bis3,bis4,l_lk2_pos1,l_lk4_pos1,l_lk2_pos3,l_lk4_pos3)
    @staticmethod
    def design_3P_complete_linkage(iposX1, iposY1, incAng1, iposX2, iposY2, incAng2, iposX3, iposY3, incAng3, link_len, tnry_posX, tnry_posY, coupler_len):
        dpos_1=Line(iposX1, iposY1, incAng1, link_len,'Point_and_Angle')
        dpos_2=Line(iposX2, iposY2, incAng2, link_len,'Point_and_Angle')
        dpos_3=Line(iposX3, iposY3, incAng3, link_len,'Point_and_Angle')
        pivX1, pivY1, lk2_pos1, lk2_pos3, lk4_pos1, ldpos_1, ldpos_2, ldpos_3, le1e2, le2e3, lf1f2, lf2f3, bis1, bis2, bis3, bis4, l_lk2_pos1, l_lk4_pos1, l_lk2_pos3, l_lk4_pos3 = My_Functions.get_base_linkage3PM(dpos_1, dpos_2, dpos_3)
        x_rot, y_rot, t_lk2_pos1, t_lk2_pos1_close, lt_lk2_pos1, lt_lk2_pos1_close, lt_lk2_pos3, lt_lk2_pos3_close = My_Functions.get_ternary_link3PM(tnry_posX, tnry_posY, pivX1, pivY1, dpos_1, dpos_2, dpos_3, lk2_pos1, lk2_pos3, lk4_pos1)
        ldyad_cplr, upper_crk, bottom_crk = My_Functions.dyad_adding(coupler_len, x_rot, y_rot, tnry_posX, tnry_posY)
        My_Functions.draw_3PM(ldpos_1,ldpos_2,ldpos_3,le1e2,le2e3,lf1f2,lf2f3,bis1,bis2,bis3,bis4,l_lk2_pos1,l_lk4_pos1,l_lk2_pos3,l_lk4_pos3,lt_lk2_pos1,lt_lk2_pos1_close,lt_lk2_pos3,lt_lk2_pos3_close,ldyad_cplr,upper_crk,bottom_crk)

        
        
        
    
class Make_List(object):
    def __init__(self, ix_or_cX, iy_or_cY, fx_or_radius, fy_or_none, shape):
        if shape=='Line':
            self.__ix = ix_or_cX
            self.__iy = iy_or_cY
            self.__fx = fx_or_radius
            self.__fy = fy_or_none
            
        if shape=='Circle':
            self.__cX=ix_or_cX
            self.__cY=iy_or_cY
            self.__radius=fx_or_radius
            self.__ix = self.__cX - self.__radius
            self.__fx = self.__cX + self.__radius
                           
    def get_line_list(self):
        self.__line_list=[[self.__ix,self.__fx],[self.__iy,self.__fy]]
        return self.__line_list
    
    def get_circle_list(self):
        self.__x_pos=[]
        self.__y_pos_up=[]
        self.__y_pos_down=[]
        self.__circle_list=[]
        step=0.01
        x=round(self.__ix,2)+0.01
        while x<=round(self.__fx,2)-0.01:
            self.__x_pos.append(x)
            self.__y_pos_up.append(round(self.__cY,3)+math.sqrt(round(self.__radius,3)**2-(round(x,3)-round(self.__cX,3))**2))
            self.__y_pos_down.append(round(self.__cY,3)-math.sqrt(round(self.__radius,3)**2-(round(x,3)-round(self.__cX,3))**2))
            x+=step
        self.__circle_list.append(self.__x_pos)
        self.__circle_list.append(self.__y_pos_up)
        self.__circle_list.append(self.__y_pos_down)
        return self.__circle_list


#from Tkinter import *
#import tkMessageBox
from tkinter import *
import tkinter.messagebox


class GUI:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title('Graphical Linkage Synthesis - Developed by Diego Hidalgo C.')
        self.main_window.resizable(width=False, height=True)
        self.welcome_label = Label(self.main_window, text = 'Welcome to the Linkage Designing Software', bg='white', fg='black', relief=SUNKEN, font='Rockwell 20 bold', height=2)
        self.welcome_label.pack(fill=X)
        self.instruction_label = Label(self.main_window, text = 'Please choose the type of mechanism you need to design: ', bg='white', fg='black', relief=SUNKEN, font='Arial 15', height=1)
        self.instruction_label.pack(fill=X)        
        self.two_positions_button = Button(self.main_window, text='Two Positions Design', command=self.two_position_window, bg='black', fg='white', relief=GROOVE, font='Rockwell 20 bold', height=1)
        self.two_positions_button.pack(side=LEFT, fill=BOTH)
        self.three_positions_button = Button(self.main_window, text='Three Position Design', command=self.three_position_window, bg='black', fg='white', relief=GROOVE, font='Rockwell 20 bold', height=1)
        self.three_positions_button.pack(side=RIGHT, fill=BOTH)     
        self.main_window.mainloop()
        
    def two_position_window(self):
        self.two_position_window = Tk()
        self.two_position_window.title('Two Position Graphical Linkage Synthesis')
        self.two_position_window.resizable(width=False, height=False)
        self.label_x_pos_1_req = Label(self.two_position_window, text = 'X coordinate for position 1:', fg='black', relief=FLAT, font='Rockwell 10', height=1)
        self.label_y_pos_1_req = Label(self.two_position_window, text = 'Y coordinate for position 1:', fg='black', relief=FLAT, font='Rockwell 10', height=1)
        self.label_x_pos_2_req = Label(self.two_position_window, text = 'X coordinate for position 2:', fg='black', relief=FLAT, font='Rockwell 10', height=1)
        self.label_y_pos_2_req = Label(self.two_position_window, text = 'Y coordinate for position 2:', fg='black', relief=FLAT, font='Rockwell 10', height=1)
        self.label_angle_pos_1_req = Label(self.two_position_window, text = 'Inclination angle for position 1:', fg='black', relief=FLAT, font='Rockwell 10', height=1)
        self.label_angle_pos_2_req = Label(self.two_position_window, text = 'Inclination angle for position 2:', fg='black', relief=FLAT, font='Rockwell 10', height=1)
        self.label_moving_link_len = Label(self.two_position_window, text = 'Length of the moving link:', fg='black', relief=FLAT, font='Rockwell 10', height=1)
        self.label_x_pos_1_req.grid(row=0, column=0, sticky=E)
        self.label_y_pos_1_req.grid(row=1, column=0, sticky=E)
        self.label_x_pos_2_req.grid(row=0, column=2, sticky=E)
        self.label_y_pos_2_req.grid(row=1, column=2, sticky=E)
        self.label_angle_pos_1_req.grid(row=2, column=0, sticky=E)
        self.label_angle_pos_2_req.grid(row=2, column=2, sticky=E)
        self.label_moving_link_len.grid(row=9, column=0, sticky=E)
        self.val_x_pos_1 = StringVar()
        self.val_y_pos_1 = StringVar()
        self.val_x_pos_2 = StringVar()
        self.val_y_pos_2 = StringVar()
        self.val_angle_pos_1 = StringVar()
        self.val_angle_pos_2 = StringVar()
        self.val_link_len = StringVar()        
        self.x_pos_1 = Entry(self.two_position_window, textvariable = self.val_x_pos_1, width=6)
        self.y_pos_1 = Entry(self.two_position_window, textvariable = self.val_y_pos_1, width=6)
        self.x_pos_2 = Entry(self.two_position_window, textvariable = self.val_x_pos_2, width=6)
        self.y_pos_2 = Entry(self.two_position_window, textvariable = self.val_y_pos_2, width=6)
        self.angle_pos_1 = Entry(self.two_position_window, textvariable = self.val_angle_pos_1, width=6)
        self.angle_pos_2 = Entry(self.two_position_window, textvariable = self.val_angle_pos_2, width=6)
        self.link_len = Entry(self.two_position_window, textvariable = self.val_link_len, width=6)
        self.x_pos_1.grid(row=0, column=1, padx=5, pady=3)
        self.y_pos_1.grid(row=1, column=1, padx=5, pady=3)
        self.x_pos_2.grid(row=0, column=3, padx=5, pady=3)
        self.y_pos_2.grid(row=1, column=3, padx=5, pady=3)
        self.angle_pos_1.grid(row=2, column=1, padx=5, pady=3)
        self.angle_pos_2.grid(row=2, column=3, padx=5, pady=3)
        self.link_len.grid(row=9, column=1, padx=5, pady=3)
        self.button_get_basic_mechanism = Button(self.two_position_window, text='Get the Basic Mechanism', command=lambda:My_Functions.design_2P__base_linkage(float(self.x_pos_1.get()), float(self.y_pos_1.get()), float(self.angle_pos_1.get()), float(self.x_pos_2.get()), float(self.y_pos_2.get()),  float(self.angle_pos_2.get()), float(self.link_len.get())), bg='black', fg='red', relief=RAISED, font='Rockwell 10 bold', height=2, width=45)
        self.button_get_basic_mechanism.grid(row=10, column=0, columnspan=4)        
        self.label_x_ternary_pos_1_req = Label(self.two_position_window, text = 'X coordinate for ternary link 2:', fg='black', relief=FLAT, font='Rockwell 10', height=1)
        self.label_y_ternary_pos_1_req = Label(self.two_position_window, text = 'Y coordinate for ternary link 2:', fg='black', relief=FLAT, font='Rockwell 10', height=1)
        self.label_length_coupler_req = Label(self.two_position_window, text = 'Length of the coupler in the dyad:', fg='black', relief=FLAT, font='Rockwell 10', height=1)
        self.val_x_ternary_pos_1 = StringVar()
        self.val_y_ternary_pos_1 = StringVar()
        self.val_length_coupler = StringVar()
        self.x_ternary_pos_1 = Entry(self.two_position_window, textvariable = self.val_x_ternary_pos_1, width=6)
        self.y_ternary_pos_1 = Entry(self.two_position_window, textvariable = self.val_y_ternary_pos_1, width=6)
        self.length_coupler = Entry(self.two_position_window, textvariable = self.val_length_coupler, width=6)
        self.x_ternary_pos_1.grid(row=11, column=1, padx=5, pady=3)
        self.y_ternary_pos_1.grid(row=12, column=1, padx=5, pady=3)
        self.length_coupler.grid(row=13, column=1, padx=5, pady=3)  
        self.label_x_ternary_pos_1_req.grid(row=11, column=0, sticky=E)
        self.label_y_ternary_pos_1_req.grid(row=12, column=0, sticky=E)
        self.label_length_coupler_req.grid(row=13, column=0, sticky=E)
        self.button_get_resulting_mechanism = Button(self.two_position_window, text='Get the Resulting Mechanism', command=lambda:My_Functions.design_2P_complete_linkage(float(self.x_pos_1.get()), float(self.y_pos_1.get()), float(self.angle_pos_1.get()), float(self.x_pos_2.get()), float(self.y_pos_2.get()),  float(self.angle_pos_2.get()), float(self.link_len.get()), float(self.x_ternary_pos_1.get()), float(self.y_ternary_pos_1.get()), float(self.length_coupler.get())), bg='black', fg='red', relief=RAISED, font='Rockwell 10 bold', height=2, width=25)
        self.button_get_resulting_mechanism.grid(row=11, column=2, rowspan=3, columnspan=2)
        self.button_get_results = Button(self.two_position_window, text='Get the results of dimensional synthesis', command=self.show_2P_results, bg='black', fg='white', relief=GROOVE, font='Rockwell 12 bold', height=1, width=35)        
        self.button_get_results.grid(row=14, column=0, columnspan=4)        
        self.two_position_window.mainloop()
        
    def three_position_window(self):
        self.three_position_window = Tk()
        self.three_position_window.title('Three Position Graphical Linkage Synthesis')
        self.three_position_window.resizable(width=False, height=False)
        self.label_x_pos_1_req = Label(self.three_position_window, text = 'X coordinate for position 1:', fg='black', relief=FLAT, font='Rockwell 10', height=1)
        self.label_y_pos_1_req = Label(self.three_position_window, text = 'Y coordinate for position 1:', fg='black', relief=FLAT, font='Rockwell 10', height=1)
        self.label_x_pos_2_req = Label(self.three_position_window, text = 'X coordinate for position 2:', fg='black', relief=FLAT, font='Rockwell 10', height=1)
        self.label_y_pos_2_req = Label(self.three_position_window, text = 'Y coordinate for position 2:', fg='black', relief=FLAT, font='Rockwell 10', height=1)
        self.label_x_pos_3_req = Label(self.three_position_window, text = 'X coordinate for position 3:', fg='black', relief=FLAT, font='Rockwell 10', height=1)
        self.label_y_pos_3_req = Label(self.three_position_window, text = 'Y coordinate for position 3:', fg='black', relief=FLAT, font='Rockwell 10', height=1)
        self.label_angle_pos_1_req = Label(self.three_position_window, text = 'Inclination angle for position 1:', fg='black', relief=FLAT, font='Rockwell 10', height=1)
        self.label_angle_pos_2_req = Label(self.three_position_window, text = 'Inclination angle for position 2:', fg='black', relief=FLAT, font='Rockwell 10', height=1)
        self.label_angle_pos_3_req = Label(self.three_position_window, text = 'Inclination angle for position 3:', fg='black', relief=FLAT, font='Rockwell 10', height=1)
        self.label_moving_link_len = Label(self.three_position_window, text = 'Length of the moving link:', fg='black', relief=FLAT, font='Rockwell 10', height=1)
        self.label_x_pos_1_req.grid(row=0, column=0, sticky=E)
        self.label_y_pos_1_req.grid(row=1, column=0, sticky=E)
        self.label_x_pos_2_req.grid(row=0, column=2, sticky=E)
        self.label_y_pos_2_req.grid(row=1, column=2, sticky=E)
        self.label_x_pos_3_req.grid(row=0, column=4, sticky=E)
        self.label_y_pos_3_req.grid(row=1, column=4, sticky=E)
        self.label_angle_pos_1_req.grid(row=2, column=0, sticky=E)
        self.label_angle_pos_2_req.grid(row=2, column=2, sticky=E)
        self.label_angle_pos_3_req.grid(row=2, column=4, sticky=E)        
        self.label_moving_link_len.grid(row=9, column=0, sticky=E)
        self.val_x_pos_1 = StringVar()
        self.val_y_pos_1 = StringVar()
        self.val_x_pos_2 = StringVar()
        self.val_y_pos_2 = StringVar()
        self.val_x_pos_3 = StringVar()
        self.val_y_pos_3 = StringVar()        
        self.val_angle_pos_1 = StringVar()
        self.val_angle_pos_2 = StringVar()
        self.val_angle_pos_3 = StringVar()
        self.val_link_len = StringVar()        
        self.x_pos_1 = Entry(self.three_position_window, textvariable = self.val_x_pos_1, width=6)
        self.y_pos_1 = Entry(self.three_position_window, textvariable = self.val_y_pos_1, width=6)
        self.x_pos_2 = Entry(self.three_position_window, textvariable = self.val_x_pos_2, width=6)
        self.y_pos_2 = Entry(self.three_position_window, textvariable = self.val_y_pos_2, width=6)
        self.x_pos_3 = Entry(self.three_position_window, textvariable = self.val_x_pos_3, width=6)
        self.y_pos_3 = Entry(self.three_position_window, textvariable = self.val_y_pos_3, width=6)
        self.angle_pos_1 = Entry(self.three_position_window, textvariable = self.val_angle_pos_1, width=6)
        self.angle_pos_2 = Entry(self.three_position_window, textvariable = self.val_angle_pos_2, width=6)
        self.angle_pos_3 = Entry(self.three_position_window, textvariable = self.val_angle_pos_3, width=6)
        self.link_len = Entry(self.three_position_window, textvariable = self.val_link_len, width=6)
        self.x_pos_1.grid(row=0, column=1, padx=5, pady=3)
        self.y_pos_1.grid(row=1, column=1, padx=5, pady=3)
        self.x_pos_2.grid(row=0, column=3, padx=5, pady=3)
        self.y_pos_2.grid(row=1, column=3, padx=5, pady=3)
        self.x_pos_3.grid(row=0, column=5, padx=5, pady=3)
        self.y_pos_3.grid(row=1, column=5, padx=5, pady=3)
        self.angle_pos_1.grid(row=2, column=1, padx=5, pady=3)
        self.angle_pos_2.grid(row=2, column=3, padx=5, pady=3)
        self.angle_pos_3.grid(row=2, column=5, padx=5, pady=3)
        self.link_len.grid(row=9, column=1, padx=5, pady=3)
        self.button_get_basic_mechanism = Button(self.three_position_window, text='Get the Basic Mechanism', command=lambda:My_Functions.design_3P__base_linkage(float(self.x_pos_1.get()), float(self.y_pos_1.get()), float(self.angle_pos_1.get()), float(self.x_pos_2.get()), float(self.y_pos_2.get()), float(self.angle_pos_2.get()), float(self.x_pos_3.get()), float(self.y_pos_3.get()), float(self.angle_pos_3.get()), float(self.link_len.get())), bg='black', fg='red', relief=RAISED, font='Rockwell 15 bold', height=1, width=20)
        self.button_get_basic_mechanism.grid(row=10, column=0, columnspan=3)    
        self.button_get_preliminar_results = Button(self.three_position_window, text='Get the Preliminar Results', command=self.show_3P__base_results, bg='black', fg='white', relief=GROOVE, font='Rockwell 15 bold', height=1, width=20)
        self.button_get_preliminar_results.grid(row=10, column=3, columnspan=2)        
        self.label_x_ternary_pos_1_req = Label(self.three_position_window, text = 'X coordinate for ternary link 2:', fg='black', relief=FLAT, font='Rockwell 10', height=1)
        self.label_y_ternary_pos_1_req = Label(self.three_position_window, text = 'Y coordinate for ternary link 2:', fg='black', relief=FLAT, font='Rockwell 10', height=1)
        self.label_length_coupler_req = Label(self.three_position_window, text = 'Length of the coupler in the dyad:', fg='black', relief=FLAT, font='Rockwell 10', height=1)
        self.val_x_ternary_pos_1 = StringVar()
        self.val_y_ternary_pos_1 = StringVar()
        self.val_length_coupler = StringVar()
        self.x_ternary_pos_1 = Entry(self.three_position_window, textvariable = self.val_x_ternary_pos_1, width=6)
        self.y_ternary_pos_1 = Entry(self.three_position_window, textvariable = self.val_y_ternary_pos_1, width=6)
        self.length_coupler = Entry(self.three_position_window, textvariable = self.val_length_coupler, width=6)
        self.x_ternary_pos_1.grid(row=11, column=1, padx=5, pady=3)
        self.y_ternary_pos_1.grid(row=12, column=1, padx=5, pady=3)
        self.length_coupler.grid(row=13, column=1, padx=5, pady=3)  
        self.label_x_ternary_pos_1_req.grid(row=11, column=0, sticky=E)
        self.label_y_ternary_pos_1_req.grid(row=12, column=0, sticky=E)
        self.label_length_coupler_req.grid(row=13, column=0, sticky=E)
        self.button_get_resulting_mechanism = Button(self.three_position_window, text='Get the Resulting Mechanism', command=lambda:My_Functions.design_3P_complete_linkage(float(self.x_pos_1.get()), float(self.y_pos_1.get()), float(self.angle_pos_1.get()), float(self.x_pos_2.get()), float(self.y_pos_2.get()), float(self.angle_pos_2.get()), float(self.x_pos_3.get()), float(self.y_pos_3.get()), float(self.angle_pos_3.get()), float(self.link_len.get()), float(self.x_ternary_pos_1.get()), float(self.y_ternary_pos_1.get()), float(self.length_coupler.get())), bg='black', fg='red', relief=RAISED, font='Rockwell 15 bold', height=1, width=25)
        self.button_get_resulting_mechanism.grid(row=11, column=2, rowspan=3, columnspan=4)
        self.button_get_results = Button(self.three_position_window, text='Get the results of dimensional synthesis', command=self.show_3P_results, bg='black', fg='white', relief=GROOVE, font='Rockwell 15 bold', height=1, width=35)        
        self.button_get_results.grid(row=14, column=0, columnspan=6)        
        self.three_position_window.mainloop()

    def show_2P_results(self):
        self.lk4x, self.lk4y, self.lk3x, self.lk3y, self.tnry_px, self.tnry_py, self.gndp3x, self.gndp3y, self.len_lk2, self.len_lk3, self.len_lk4 = My_Functions.get_2P_linkage_results(float(self.x_pos_1.get()), float(self.y_pos_1.get()), float(self.angle_pos_1.get()), float(self.x_pos_2.get()), float(self.y_pos_2.get()), float(self.angle_pos_2.get()), float(self.link_len.get()), float(self.x_ternary_pos_1.get()), float(self.y_ternary_pos_1.get()), float(self.length_coupler.get()))
        tkinter.messagebox.showinfo('Results', 'Ground link starts at x and y: ' + format(self.lk4x, '.2f') + ', ' + format(self.lk4y, '.2f') + ' and ends at: ' + format(self.gndp3x, '.2f') + ', ' + format(self.gndp3y, '.2f') + '\n' + \
                                            'The length of link 2 is: ' + format(self.len_lk2, '.2f') + ' with initial coordinates at: ' + format(self.gndp3x, '.2f') + ', ' + format(self.gndp3y, '.2f') + '\n' + \
                                            "The coordinates of the ternary link's vertex are at: " + format(self.tnry_px, '.2f') + ', ' + format(self.tnry_py, '.2f') + '\n' + \
                                            'The length of coupler link is: ' + format(self.len_lk3, '.2f') + '\n' + \
                                            'The length of link 4 is: ' + format(self.len_lk4, '.2f')) 
    
    def show_3P__base_results(self):
        self.lk2x, self.lk2y, self.lk3x, self.lk3y, self.lk4x, self.lk4y, self.len_lk2, self.len_lk4 = My_Functions.get_3P_linkage_base_results(float(self.x_pos_1.get()), float(self.y_pos_1.get()), float(self.angle_pos_1.get()), float(self.x_pos_2.get()), float(self.y_pos_2.get()), float(self.angle_pos_2.get()), float(self.x_pos_3.get()), float(self.y_pos_3.get()), float(self.angle_pos_3.get()), float(self.link_len.get()))                                  
        tkinter.messagebox.showinfo('Results', "Ground link's first pivot is at x and y: " + format(self.lk2x, '.2f') + ', ' + format(self.lk2y, '.2f') + ' its secont pivod is at: ' + format(self.lk4x, '.2f') + ', ' + format(self.lk4y, '.2f') + '\n' + \
                                          'The length of link 2 is: ' + format(self.len_lk2, '.2f') + ' with ending coordinates at: ' + format(self.lk3x, '.2f') + ', ' + format(self.lk3y, '.2f') + '\n' + \
                                          'The length of link 4 is: ' + format(self.len_lk4, '.2f'))                                              
                                          
    def show_3P_results(self):
        self.lk2x, self.lk2y, self.lk3x, self.lk3y, self.lk4x, self.lk4y, self.tnry_px, self.tnry_py, self.gndp3x, self.gndp3y, self.len_lk2, self.len_lk4, self.len_lk5, self.len_lk6 = My_Functions.get_3P_linkage_results(float(self.x_pos_1.get()), float(self.y_pos_1.get()), float(self.angle_pos_1.get()), float(self.x_pos_2.get()), float(self.y_pos_2.get()), float(self.angle_pos_2.get()), float(self.x_pos_3.get()), float(self.y_pos_3.get()), float(self.angle_pos_3.get()), float(self.link_len.get()), float(self.x_ternary_pos_1.get()), float(self.y_ternary_pos_1.get()), float(self.length_coupler.get()))                                  
        tkinter.messagebox.showinfo('Results', "Ground link's first pivot is at x and y: " + format(self.lk2x, '.2f') + ', ' + format(self.lk2y, '.2f') + ' its secont pivod is at: ' + format(self.lk4x, '.2f') + ', ' + format(self.lk4y, '.2f') + 'and its third pivot is at: ' + format(self.gndp3x, '.2f') + ', ' + format(self.gndp3y, '.2f') + '\n' + \
                                          'The length of link 2 is: ' + format(self.len_lk2, '.2f') + ' with ending coordinates at: ' + format(self.lk3x, '.2f') + ', ' + format(self.lk3y, '.2f') + '\n' + \
                                          "The coordinates of the ternary link's vertex are at: " + format(self.tnry_px, '.2f') + ', ' + format(self.tnry_py, '.2f') + '\n' + \
                                          'The length of link 4 is: ' + format(self.len_lk4, '.2f') + '\n'                                              
                                          'The length of link 5 is: ' + format(self.len_lk5, '.2f') + '\n'
                                          'The length of link 6 is: ' + format(self.len_lk6, '.2f'))                                        

Run_Application = GUI()
