﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LightCoral
		self._label1.Font = System.Drawing.Font("Ebrima", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(4, 36)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(168, 42)
		self._label1.TabIndex = 0
		self._label1.Text = "First name:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LightCoral
		self._label2.Font = System.Drawing.Font("Ebrima", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(4, 101)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(168, 42)
		self._label2.TabIndex = 1
		self._label2.Text = "Last name:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.LightCoral
		self._label3.Font = System.Drawing.Font("Ebrima", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(4, 216)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(163, 42)
		self._label3.TabIndex = 2
		self._label3.Text = "Full name:"
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(178, 40)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(240, 38)
		self._textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(178, 101)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(240, 38)
		self._textBox2.TabIndex = 4
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.LightCoral
		self._label4.Font = System.Drawing.Font("Ebrima", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(159, 216)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(259, 42)
		self._label4.TabIndex = 5
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(4, 149)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(414, 64)
		self._button1.TabIndex = 6
		self._button1.Text = "Show name"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(4, 261)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(414, 64)
		self._button2.TabIndex = 7
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(4, 331)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(414, 64)
		self._button3.TabIndex = 8
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(430, 400)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "pg119FullName"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		fn = self._textBox1.Text
		ln = self._textBox2.Text
		fullname = fn + " " + ln
		self._label4.Text = fullname
		

	def Button2Click(self, sender, e):
		self._textBox1.Clear()
		self._textBox2.Clear()
		self._label4.Text = " "

	def Button3Click(self, sender, e):
		Application.Exit()