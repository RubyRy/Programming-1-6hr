import System.Drawing
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
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label7 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LightSteelBlue
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(190, 37)
		self._label1.TabIndex = 0
		self._label1.Text = "Sales:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LightSteelBlue
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 62)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(190, 37)
		self._label2.TabIndex = 1
		self._label2.Text = "Advance pay:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.LightSteelBlue
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 123)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(190, 37)
		self._label3.TabIndex = 2
		self._label3.Text = "Commision rate:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.LightSteelBlue
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 191)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(190, 37)
		self._label4.TabIndex = 3
		self._label4.Text = "Commission:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.LightSteelBlue
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(12, 259)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(190, 37)
		self._label5.TabIndex = 4
		self._label5.Text = "Net Pay:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.LightSteelBlue
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(227, 123)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(190, 37)
		self._label6.TabIndex = 5
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.LightSteelBlue
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(227, 259)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(190, 37)
		self._label8.TabIndex = 7
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(227, 9)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(190, 39)
		self._textBox1.TabIndex = 8
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 21, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(227, 62)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(190, 39)
		self._textBox2.TabIndex = 9
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(436, 17)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(125, 82)
		self._button1.TabIndex = 10
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(436, 105)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(125, 82)
		self._button2.TabIndex = 11
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(436, 193)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(125, 82)
		self._button3.TabIndex = 12
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.LightSteelBlue
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(227, 191)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(190, 37)
		self._label7.TabIndex = 6
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(573, 304)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Pg240Comm"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		l = float(self._textBox1.Text)
		n = float(self._textBox2.Text)
		
		if l < 10000:
			r = 0.05
		elif l >= 10000 and l < 15000:
			r = 0.1
		elif l >= 15000 and l < 18000:
			r = 0.12
		elif l >= 18000 and l < 22000:
			r = 0.14
		elif l >= 22000:
			r = 0.16
		self._label6.Text = str(r * 100) + "%"
		
		c = r * l
		self._label7.Text = str(c)
		
		o = c - n
		self._label8.Text = str(o)
		
		

	def Button2Click(self, sender, e):
		self._textBox1.Clear()
		self._textBox2.Clear()
		self._label6.Text = " "
		self._label7.Text = " "
		self._label8.Text = " "

	def Button3Click(self, sender, e):
		Application.Exit()