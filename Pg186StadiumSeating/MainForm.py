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
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.IndianRed
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 27)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(86, 39)
		self._label1.TabIndex = 0
		self._label1.Text = "Class A:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.IndianRed
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 92)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(86, 39)
		self._label2.TabIndex = 1
		self._label2.Text = "Class B:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.IndianRed
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 160)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(86, 39)
		self._label3.TabIndex = 2
		self._label3.Text = "Class C:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.IndianRed
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(268, 27)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 39)
		self._label4.TabIndex = 3
		self._label4.Text = "Class A:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.IndianRed
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(268, 92)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 39)
		self._label5.TabIndex = 4
		self._label5.Text = "Class B:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.IndianRed
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(268, 160)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 39)
		self._label6.TabIndex = 5
		self._label6.Text = "Class C:"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.IndianRed
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(268, 215)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(113, 39)
		self._label7.TabIndex = 6
		self._label7.Text = "Total Revenue "
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.IndianRed
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(374, 27)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(203, 39)
		self._label8.TabIndex = 7
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.IndianRed
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(374, 92)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(203, 39)
		self._label9.TabIndex = 8
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.IndianRed
		self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(374, 160)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(203, 39)
		self._label10.TabIndex = 9
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.IndianRed
		self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(387, 215)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(190, 39)
		self._label11.TabIndex = 10
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(104, 24)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(158, 38)
		self._textBox1.TabIndex = 11
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(104, 92)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(158, 38)
		self._textBox2.TabIndex = 12
		# 
		# textBox3
		# 
		self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(104, 157)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(158, 38)
		self._textBox3.TabIndex = 13
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 202)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(250, 23)
		self._button1.TabIndex = 14
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(12, 225)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(250, 23)
		self._button2.TabIndex = 15
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(12, 246)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(250, 23)
		self._button3.TabIndex = 16
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Maroon
		self.ClientSize = System.Drawing.Size(600, 275)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Pg186StadiumSeating"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		A = float(self._textBox1.Text)
		B = float(self._textBox2.Text)
		C = float(self._textBox3.Text)
		ca = A * 15
		cb = B * 12
		cc = C * 9
		tr = ca + cb + cc
		self._label11.Text = str(round(tr, 2))
		self._label10.Text = str(round(cc, 2))
		self._label9.Text = str(round(cb, 2))
		self._label8.Text = str(round(ca, 2))

	def Button2Click(self, sender, e):
		self._textBox1.Clear()
		self._textBox2.Clear()
		self._textBox3.Clear()
		self._label11.Text = " "
		self._label10.Text = " "
		self._label9.Text = " "
		self._label8.Text = " "

	def Button3Click(self, sender, e):
		Application.Exit()