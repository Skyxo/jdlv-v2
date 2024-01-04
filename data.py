# coding: utf-8
#Création et stockage des figures qu'on récupère dans jeu_de_la_vie.pyde et qu'on exploite

import jdlv

figure_2 = [
[-1, -6],
[0, -6],
[1, -6],
[-4, -5],
[4, -5],
[-6, -4],
[-2, -4],
[2, -4],
[6, -4],
[-1, -3],
[1, -3],
[-6, -2],
[-1, -2],
[1, -2],
[6, -2],
[-8, -1],
[-5, -1],
[-4, -1],
[-3, -1],
[-2, -1],
[-1, -1],
[1, -1],
[2, -1],
[3, -1],
[4, -1],
[5, -1],
[8, -1],
[-8, 0],
[8, 0],
[-8, 1],
[-5, 1],
[-4, 1],
[-3, 1],
[-2, 1],
[-1, 1],
[1, 1],
[2, 1],
[3, 1],
[4, 1],
[5, 1],
[8, 1],
[-6, 2],
[-1, 2],
[1, 2],
[6, 2],
[-1, 3],
[1, 3],
[-6, 4],
[-2, 4],
[2, 4],
[6, 4],
[-4, 5],
[4, 5],
[-1, 6],
[0, 6],
[1, 6]]

figure_1 = [
[57, -40],
[58, -40],
[57, -39],
[55, -38],
[57, -38],
[55, -37],
[56, -37],
[51, -35],
[52, -35],
[52, -34],
[53, -34],
[51, -33],
[44, -28],
[44, -27],
[45, -27],
[43, -26],
[45, -26],
[36, -20],
[37, -20],
[37, -19],
[38, -19],
[36, -18],
[29, -13],
[29, -12],
[30, -12],
[28, -11],
[30, -11],
[21, -5],
[22, -5],
[9, -4],
[11, -4],
[22, -4],
[23, -4],
[4, -3],
[9, -3],
[12, -3],
[21, -3],
[5, -2],
[6, -2],
[12, -2],
[13, -2],
[25, -2],
[26, -2],
[0, -1],
[1, -1],
[10, -1],
[14, -1],
[15, -1],
[24, -1],
[26, -1],
[0, 0],
[1, 0],
[12, 0],
[13, 0],
[23, 0],
[30, 0],
[31, 0],
[9, 1],
[12, 1],
[23, 1],
[26, 1],
[29, 1],
[32, 1],
[34, 1],
[35, 1],
[9, 2],
[11, 2],
[23, 2],
[30, 2],
[31, 2],
[34, 2],
[35, 2],
[24, 3],
[26, 3],
[25, 4],
[26, 4]]

ruche = [[0, 0],
         [1, -1],
         [1, -2],
         [0, -3],
         [-1, -1],
         [-1, -2]]

ten = [[i, 0] for i in range(10)]

glider = [[0, 0],
          [0, -2],
          [1, -2],
          [1, -1],
          [2, -1]]

gliderc = [[0, 0], 
           [1, 0], 
           [0, -1], 
           [1, -1], 
           [10, 0], 
           [10, -1], 
           [10, -2], 
           [11, 1], 
           [11, -3], 
           [12, -4], 
           [13, -4], 
           [12, 2], 
           [13, 2], 
           [15, 1], 
           [15, -3], 
           [14, -1], 
           [16, 0], 
           [16, -1], 
           [16, -2], 
           [17, -1], 
           [20, 0], 
           [20, 1], 
           [20, 2], 
           [21, 0], 
           [21, 1], 
           [21, 2], 
           [22, 3], 
           [22, -1], 
           [24, 3], 
           [24, 4], 
           [24, -1], 
           [24, -2], 
           [34, 2], 
           [35, 2],
           [34, 1],
           [35, 1]] 

line1 = [
[37, -40],
[38, -40],
[36, -39],
[38, -39],
[38, -38],
[29, -32],
[30, -32],
[31, -32],
[31, -31],
[30, -30],
[22, -25],
[23, -25],
[21, -24],
[23, -24],
[23, -23],
[14, -17],
[15, -17],
[16, -17],
[16, -16],
[15, -15],
[7, -10],
[8, -10],
[6, -9],
[8, -9],
[8, -8],
[-1, -2],
[0, -2],
[1, -2],
[1, -1],
[0, 0]]

line2 = [
[38, -39],
[39, -39],
[39, -38],
[40, -38],
[38, -37],
[31, -32],
[31, -31],
[32, -31],
[30, -30],
[32, -30],
[23, -24],
[24, -24],
[24, -23],
[25, -23],
[23, -22],
[16, -17],
[16, -16],
[17, -16],
[15, -15],
[17, -15],
[8, -9],
[9, -9],
[9, -8],
[10, -8],
[8, -7],
[1, -2],
[1, -1],
[2, -1],
[0, 0],
[2, 0]]

line3 = [
[38, -38],
[39, -38],
[40, -38],
[40, -37],
[39, -36],
[31, -31],
[32, -31],
[30, -30],
[32, -30],
[32, -29],
[23, -23],
[24, -23],
[25, -23],
[25, -22],
[24, -21],
[16, -16],
[17, -16],
[15, -15],
[17, -15],
[17, -14],
[8, -8],
[9, -8],
[10, -8],
[10, -7],
[9, -6],
[1, -1],
[2, -1],
[0, 0],
[2, 0],
[2, 1]]


line4 = [
[38, -40],
[38, -39],
[39, -39],
[37, -38],
[39, -38],
[30, -32],
[31, -32],
[31, -31],
[32, -31],
[30, -30],
[23, -25],
[23, -24],
[24, -24],
[22, -23],
[24, -23],
[15, -17],
[16, -17],
[16, -16],
[17, -16],
[15, -15],
[8, -10],
[8, -9],
[9, -9],
[7, -8],
[9, -8],
[0, -2],
[1, -2],
[1, -1],
[2, -1],
[0, 0]]

c1 = [
[24, -8],
[25, -8],
[26, -8],
[26, -7],
[25, -6],
[11, -4],
[12, -4],
[11, -3],
[12, -3],
[17, -3],
[8, -2],
[9, -2],
[16, -2],
[17, -2],
[18, -2],
[19, -2],
[20, -2],
[22, -2],
[23, -2],
[0, -1],
[1, -1],
[7, -1],
[8, -1],
[9, -1],
[15, -1],
[18, -1],
[19, -1],
[24, -1],
[0, 0],
[1, 0],
[8, 0],
[9, 0],
[15, 0],
[16, 0],
[25, 0],
[11, 1],
[12, 1],
[17, 1],
[25, 1],
[34, 1],
[35, 1],
[11, 2],
[12, 2],
[25, 2],
[34, 2],
[35, 2],
[24, 3],
[22, 4],
[23, 4]]

c2 = [
[25, -9],
[25, -8],
[26, -8],
[24, -7],
[26, -7],
[11, -4],
[12, -4],
[10, -3],
[11, -3],
[12, -3],
[16, -3],
[17, -3],
[19, -3],
[7, -2],
[9, -2],
[10, -2],
[16, -2],
[20, -2],
[23, -2],
[0, -1],
[1, -1],
[7, -1],
[10, -1],
[15, -1],
[20, -1],
[23, -1],
[24, -1],
[0, 0],
[1, 0],
[7, 0],
[9, 0],
[10, 0],
[15, 0],
[16, 0],
[17, 0],
[18, 0],
[24, 0],
[25, 0],
[10, 1],
[11, 1],
[12, 1],
[16, 1],
[24, 1],
[25, 1],
[26, 1],
[34, 1],
[35, 1],
[11, 2],
[12, 2],
[24, 2],
[25, 2],
[34, 2],
[35, 2],
[23, 3],
[24, 3],
[23, 4]]

c3 = [
[25, -9],
[26, -9],
[24, -8],
[26, -8],
[26, -7],
[10, -4],
[12, -4],
[9, -3],
[12, -3],
[16, -3],
[17, -3],
[8, -2],
[9, -2],
[15, -2],
[16, -2],
[17, -2],
[19, -2],
[20, -2],
[23, -2],
[24, -2],
[0, -1],
[1, -1],
[6, -1],
[7, -1],
[11, -1],
[15, -1],
[19, -1],
[23, -1],
[25, -1],
[0, 0],
[1, 0],
[8, 0],
[9, 0],
[15, 0],
[17, 0],
[26, 0],
[9, 1],
[12, 1],
[15, 1],
[16, 1],
[23, 1],
[26, 1],
[34, 1],
[35, 1],
[10, 2],
[12, 2],
[26, 2],
[34, 2],
[35, 2],
[23, 3],
[25, 3],
[23, 4],
[24, 4]]


c4 = [
[25, -9],
[26, -9],
[26, -8],
[27, -8],
[25, -7],
[11, -4],
[8, -3],
[9, -3],
[10, -3],
[11, -3],
[15, -3],
[17, -3],
[18, -3],
[7, -2],
[8, -2],
[9, -2],
[10, -2],
[15, -2],
[17, -2],
[19, -2],
[20, -2],
[23, -2],
[24, -2],
[0, -1],
[1, -1],
[7, -1],
[10, -1],
[14, -1],
[15, -1],
[17, -1],
[19, -1],
[20, -1],
[23, -1],
[25, -1],
[0, 0],
[1, 0],
[7, 0],
[8, 0],
[9, 0],
[10, 0],
[14, 0],
[15, 0],
[24, 0],
[25, 0],
[26, 0],
[8, 1],
[9, 1],
[10, 1],
[11, 1],
[15, 1],
[16, 1],
[25, 1],
[26, 1],
[27, 1],
[34, 1],
[35, 1],
[11, 2],
[24, 2],
[25, 2],
[26, 2],
[34, 2],
[35, 2],
[23, 3],
[25, 3],
[23, 4],
[24, 4]]

lwss = [[0, 0],
        [3, 0],
        [4, -1],
        [4, -2],
        [4, -3],
        [3, -3],
        [2, -3],
        [1, -3],
        [0, -2]]

mwss = [[0, 0],
        [2, 1],
        [4, 0],
        [5, -1],
        [5, -2],
        [5, -3],
        [4, -3],
        [3, -3],
        [2, -3],
        [1, -3],
        [0, -2]]

breaker = [[0, 0],
           [-1, 0],
           [0, 1],
           [-2, 1],
           [-2, 2],
           [-2, 3],
           [-3, 3]]

cube1x1 = [[0, 0]]

cube2x2 = [[0, 0],
           [1, 0],
           [1, 1],
           [0, 1]]

cube4x4 = [[0, 0],
           [1, 0],
           [2, 0],
           [3, 0],
           [0, 1],
           [0, 2],
           [0, 3],
           [1, 1],
           [1, 2],
           [1, 3],
           [2, 1],
           [2, 2],
           [2, 3],
           [3, 1],
           [3, 2],
           [3, 3]]
           
#placing = [ruche, ten, glider, gliderc, c1, c2, c3, c4, line1, line2, line3, line4, lwss, mwss, breaker, cube1x1, cube2x2, cube4x4]
#placing_names = ["Ruche", "10", "Glider", "GliderC", "C1", "C2", "C3", "C4", "line1", "line2", "line3", "line4", "LWSS", "MWSS", "Breaker", "1x1", "2x2", "4x4"]

placing = [ruche, ten, glider, gliderc, lwss, mwss, breaker, cube1x1, cube2x2, cube4x4, figure_1, figure_2]
placing_names = ["Ruche", "10", "Glider", "GliderC", "LWSS", "MWSS", "Breaker", "1x1", "2x2", "4x4", "figure_1", "figure_2"]
