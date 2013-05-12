#!/usr/bin/python
import wx
import time
#read from obstacle input file , and sign up obstacles. with input format x1,y1 , means that specific position
#read from movement input file , with coordinates only that means the current position.
#and show off the movement tracks.

app = wx.App(False)

frame = wx.Frame(None, title="Draw on Panel")
panel = wx.Panel(frame)

def on_paint(event):
	dc = wx.PaintDC(event.GetEventObject())
	dc.Clear()
	dc.SetPen(wx.Pen("BLACK", 1))
	dc.SetBrush(wx.Brush("RED")) # set color
	obstacle_f = open('obstacle.in','r+')
	for line in obstacle_f:
		arr = line.split('\n')
		arr = arr[0].split(' ')
		arr[0] = int(arr[0])
		arr[1] = int(arr[1])
		arr[2] = int(arr[2])
		arr[3] = int(arr[3])
		x = arr[0] * 10
		y = arr[1] * 10
		xlen = arr[2] * 10
		ylen = arr[3] * 10
		dc.DrawRectangle(x,y,xlen,ylen)
	movement_f = open('movement.in','r+')
	dc.SetPen(wx.Pen("BLACK", 1))
	dc.SetBrush(wx.Brush("BLUE")) # set color
	for line in movement_f:
		arr = line.split('\n')
		arr = arr[0].split(' ')
		arr[0] = int(arr[0])
		arr[1] = int(arr[1])
		x = arr[0] * 10
		y = arr[1] * 10
		dc.DrawRectangle(x,y,10,10)

panel.Bind(wx.EVT_PAINT, on_paint)

frame.Show(True)
app.MainLoop()

