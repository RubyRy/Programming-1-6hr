import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(16, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(404, 342)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Aqua
		self._button1.Location = System.Drawing.Point(16, 360)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(112, 66)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Aqua
		self._button2.Location = System.Drawing.Point(167, 360)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(112, 66)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Aqua
		self._button3.Location = System.Drawing.Point(308, 360)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(112, 66)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self.ClientSize = System.Drawing.Size(432, 438)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Prog122a"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		header = "Number\t\tSquare\t\tSquare root"
		self._listBox1.Items.Add(header)
		for num in range(1, 50+10):
			numsqrd = num**2
			numsqrt = math.sqrt(num)
			msg = str(num) + "t\t" + str(numsqrd) + "\t\t" + str(round(numsqrt, 4))
			self._listBox1.Items.Add(msg)

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit