﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
		self.R = System.Random()
		self.ballup = 0
		self.balld = 0
		self.flagleft = False
		self.flagright = False

	
	def InitializeComponent(self):
		self._components = System.ComponentModel.Container()
		self._lblball = System.Windows.Forms.Label()
		self._lblleft = System.Windows.Forms.Label()
		self._lblright = System.Windows.Forms.Label()
		self._timerright = System.Windows.Forms.Timer(self._components)
		self._timerleft = System.Windows.Forms.Timer(self._components)
		self._timerball = System.Windows.Forms.Timer(self._components)
		self._timermulti = System.Windows.Forms.Timer(self._components)
		self._timerdummy = System.Windows.Forms.Timer(self._components)
		self._timerboolean = System.Windows.Forms.Timer(self._components)
		self._leftscore = System.Windows.Forms.Label()
		self._rightscore = System.Windows.Forms.Label()
		self._lbltitle = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# lblball
		# 
		self._lblball.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._lblball.Location = System.Drawing.Point(479, 304)
		self._lblball.Name = "lblball"
		self._lblball.Size = System.Drawing.Size(20, 20)
		self._lblball.TabIndex = 0
		self._lblball.Click += self.LblballClick
		# 
		# lblleft
		# 
		self._lblleft.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._lblleft.Location = System.Drawing.Point(12, 246)
		self._lblleft.Name = "lblleft"
		self._lblleft.Size = System.Drawing.Size(20, 100)
		self._lblleft.TabIndex = 1
		# 
		# lblright
		# 
		self._lblright.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._lblright.Location = System.Drawing.Point(950, 246)
		self._lblright.Name = "lblright"
		self._lblright.Size = System.Drawing.Size(20, 100)
		self._lblright.TabIndex = 2
		self._lblright.Click += self.LblrightClick
		# 
		# timerright
		# 
		self._timerright.Interval = 20
		self._timerright.Tick += self.TimerrightTick
		# 
		# timerleft
		# 
		self._timerleft.Interval = 20
		self._timerleft.Tick += self.TimerleftTick
		# 
		# timerball
		# 
		self._timerball.Interval = 20
		self._timerball.Tick += self.TimerballTick
		# 
		# timermulti
		# 
		self._timermulti.Interval = 20
		# 
		# leftscore
		# 
		self._leftscore.BackColor = System.Drawing.Color.Transparent
		self._leftscore.Font = System.Drawing.Font("Microsoft Sans Serif", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._leftscore.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._leftscore.Location = System.Drawing.Point(78, 96)
		self._leftscore.Name = "leftscore"
		self._leftscore.Size = System.Drawing.Size(74, 78)
		self._leftscore.TabIndex = 3
		self._leftscore.Text = "0"
		self._leftscore.Click += self.LeftscoreClick
		# 
		# rightscore
		# 
		self._rightscore.BackColor = System.Drawing.Color.Transparent
		self._rightscore.Font = System.Drawing.Font("Microsoft Sans Serif", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._rightscore.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._rightscore.Location = System.Drawing.Point(734, 96)
		self._rightscore.Name = "rightscore"
		self._rightscore.Size = System.Drawing.Size(74, 78)
		self._rightscore.TabIndex = 4
		self._rightscore.Text = "0"
		self._rightscore.Click += self.RightscoreClick
		# 
		# lbltitle
		# 
		self._lbltitle.BackColor = System.Drawing.Color.Transparent
		self._lbltitle.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._lbltitle.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._lbltitle.Location = System.Drawing.Point(12, 25)
		self._lbltitle.Name = "lbltitle"
		self._lbltitle.Size = System.Drawing.Size(958, 52)
		self._lbltitle.TabIndex = 5
		self._lbltitle.Text = "Press Enter to start or M to start multiplayer"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self.ClientSize = System.Drawing.Size(988, 607)
		self.Controls.Add(self._lbltitle)
		self.Controls.Add(self._rightscore)
		self.Controls.Add(self._leftscore)
		self.Controls.Add(self._lblright)
		self.Controls.Add(self._lblleft)
		self.Controls.Add(self._lblball)
		self.Name = "MainForm"
		self.Text = "Pong"
		self.Load += self.MainFormLoad
		self.SizeChanged += self.MainFormSizeChanged
		self.KeyDown += self.MainFormKeyDown
		self.ResumeLayout(False)


	def TimerballTick(self, sender, e):
		ball = self._lblball
		lpdl = self._lblleft
		rpdl = self._lblright
		rscore = int(self._rightscore.Text)
		lscore = int(self._leftscore.Text)
		ball.Top += self.ballup
		ball.Left += 8 * self.balld
		
		if ball.Right >= rpdl.Left and ball.Bottom >= rpdl.Top and ball.Top <= rpdl.Bottom:
			self.balld = -1
			self.ballup = self.R.Next(-4, 5)
		elif ball.Left <= lpdl.Right and ball.Bottom >= lpdl.Top and ball.Top <= lpdl.Bottom:
			self.balld = 1
			self.ballup = self.R.Next(-4, 5)
		
		if ball.Top <= 0:
			self.balld = -1
			ball.Top += 5 * self.balld
		
		if ball.Bottom >= self.Height:
			self.balld = 1
			ball.Top += 5 * self.balld
		
		if ball.Location.X <= 0 or \
		   (ball.Location.X < lpdl.Left + 20 and ball.Location.Y < lpdl.Top):
		   	rscore += 1
		   	ball.Left = self.Width // 2
		   	ball.Top = self.Height // 2
		   	self._rightscore.Text = str(rscore)
		
		if ball.Location.X >= self.Width or \
		   (ball.Location.X > rpdl.Right + 20 and ball.Location.Y > rpdl.Top):
		   	lscore += 1
		   	ball.Left = self.Width // 2
		   	ball.Top = self.Height // 2
		   	self._leftscore.Text = str(lscore)
		
		if lscore == 10:  
			self._timerball.Enabled = False
			ball.Left = self.Width // 2
			ball.Top = self.Height // 2
			self.ballup = 0
			self._lbltitle.Visible = True
			self._lbltitle.Text = "Left Player Wins! Press R to restart"
			
		if rscore == 10: 
			self._timerball.Enabled = False
			ball.Left = self.Width // 2
			ball.Top = self.Height // 2
			self.ballup = 0
			self._lbltitle.Visible = True
			self._lbltitle.Text = "Right Player Wins! Press R to restart"
	
		if ball.Top <= 0:
			self.ballup *= -1
		elif ball.Bottom >= self.Height:
			self.ballup *= -1
		
		if ball.Top <= self.Top:
			self.ballup = 1
		elif ball.Top >= self.Height:
			self.ballup = -1

		if self._timerboolean.Enabled == True:
			lpdl.Top = ball.Top - 0
		
	
	def MainFormLoad(self, sender, e):
		self.balld = 1
		self.ballup = self.R.Next(-4, 5)
		self._timerball.Enabled = False
		self._timerdummy.Enabled = False
		self._timermulti.Enabled = False
	
	def pdlTick(self, pdl, flagd, tmr):
		if flagd == True:
			pdl.Top += 5
		if flagd == False:
			pdl.Top -= 5
		if pdl.Top <= 10:
			tmr.Enabled = False
		if pdl.Bottom <= self.Height - 50:
			tmr.Enabled = False
			


	def TimerleftTick(self, sender, e):
		self.pdlTick(self._lblleft, self.flagleft, self._timerleft)

	def TimerrightTick(self, sender, e):
		self.pdlTick(self._lblright, self.flagright, self._timerright)

	def LblballClick(self, sender, e):
		self._lblball.BackColor = Color.Red
		self.BackColor = Color.Green

	def MainFormSizeChanged(self, sender, e):
		self._lblright.Left = self.Width - 25 - self._lblright.Width
		self._lblball.Left = self.Width // 2
		self._ball.Top = self.Height // 2
		self.lbltitle.Width = self.Width - 25
		self._rightscore.Left = self.Width - 75 - self._rightscore.Width

	def MainFormKeyDown(self, sender, e):
		tball = self._timerball
		tdum = self._timerdummy
		tbool = self._timerboolean
		tmult = self._timermulti
		tleft = self._timerleft
		tright = self._timerright
		bl = self._lblball
		lblf = self._lblleft
		lblrt = self._lblright
		
		def reset():
			self._lbltitle.Visible = True
			self._lbltitle.Text = "Press Enter to Start or M to start Multiplayer"
			self._leftscore.Text = "0"
			self._rightscore.Text = "0"
			tball.Enabled = False
			tdum.Enabled = False
			tbool.Enabled = False
			tmult.Enabled = False
			tleft.Enabled = False
			tright.Enabled = False
			bl.Left = self.Width // 2
			bl.Top = self.Height // 2
			lblf.Top = (self.Height // 2) - 100 + self._lblleft.Height
			lblrt.Top = (self.Height // 2) - 100 + self._lblright.Height
			self._lblball.BackColor = Color.White
			self._rightscore.ForeColor = Color.White
			self._leftscore.ForeColor = Color.White
			self.BackColor = Color.Black
			self._lblright.BackColor = Color.White
			self._lblleft.BackColor = Color.White
			self._lbltitle.ForeColor = Color.White
		
		if e.KeyCode == Keys.R:
			reset()
		
		if e.KeyCode == Keys.Enter:
			tball.Enabled = True
			tdum.Enabled = True
			tbool.Enabled = True
			self._lbltitle.Visible = False
		
		if e.KeyCode == Keys.M:
			reset()
			self._lbltitle.Visible = True
			self._lbltitle.Text = "Use W and S to move the left paddle; " \
								  "hit Enter to begin"
			tmult.Enabled = True
			if e.KeyCode == Keys.Enter:
				self._lbltitle.Visible = False
				tbool.Enabled = False
				tmult.Enabled = True
				tdum.Enabled = True
				tball.Enabled = True
		
		if tdum.Enabled:
			if e.KeyCode == Keys.Up:
				self.flagright = False
				tright.Enabled = True
			elif e.KeyCode == Keys.Down:
				self.flagright = True
				tright.Enabled = True
			elif tright.Enabled and self.flagright == False:
				tright.Enabled = False
		
		if tmult.Enabled and tball.Enabled:
			tleft.Enabled = False
			if e.KeyCode == Keys.W:
				self.flagleft = False
				tleft.Enabled = True
				tbool.Enabled = False
			if e.KeyCode == Keys.S:
				self.flagleft = True
				tleft.Enabled = True
				tbool.Enabled = False

	def RightscoreClick(self, sender, e):
		self._rightscore.ForeColor = Color.Black
		self._leftscore.ForeColor = Color.Black
		self.BackColor = Color.White
		self._lblright.BackColor = Color.Black
		self._lblleft.BackColor = Color.Black
		self._lblball.BackColor = Color.Black
		self._lbltitle.ForeColor = Color.Black

	def LblrightClick(self, sender, e):
		pass

	def LeftscoreClick(self, sender, e):
		self._rightscore.ForeColor = Color.Purple
		self._leftscore.ForeColor = Color.Purple
		self.BackColor = Color.DarkGray
		self._lblright.BackColor = Color.Purple
		self._lblleft.BackColor = Color.Purple
		self._lblball.BackColor = Color.Purple
		self._lbltitle.ForeColor = Color.Purple