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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._textBox5 = System.Windows.Forms.TextBox()
		self._textBox6 = System.Windows.Forms.TextBox()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.MediumPurple
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 34)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(121, 35)
		self._label1.TabIndex = 0
		self._label1.Text = "Racer 1:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.MediumPurple
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 86)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(121, 35)
		self._label2.TabIndex = 1
		self._label2.Text = "Racer 2:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.MediumPurple
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 135)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(121, 35)
		self._label3.TabIndex = 2
		self._label3.Text = "Racer 3:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.MediumPurple
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(134, 9)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(63, 26)
		self._label4.TabIndex = 3
		self._label4.Text = "Name"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.MediumPurple
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(223, 9)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(135, 23)
		self._label5.TabIndex = 4
		self._label5.Text = "Finishing Time"
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(134, 38)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(86, 29)
		self._textBox1.TabIndex = 5
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(226, 40)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(132, 29)
		self._textBox2.TabIndex = 6
		# 
		# textBox3
		# 
		self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(134, 90)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(86, 29)
		self._textBox3.TabIndex = 7
		# 
		# textBox4
		# 
		self._textBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox4.Location = System.Drawing.Point(226, 90)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(132, 29)
		self._textBox4.TabIndex = 8
		# 
		# textBox5
		# 
		self._textBox5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox5.Location = System.Drawing.Point(134, 135)
		self._textBox5.Name = "textBox5"
		self._textBox5.Size = System.Drawing.Size(86, 29)
		self._textBox5.TabIndex = 9
		# 
		# textBox6
		# 
		self._textBox6.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox6.Location = System.Drawing.Point(226, 135)
		self._textBox6.Name = "textBox6"
		self._textBox6.Size = System.Drawing.Size(132, 29)
		self._textBox6.TabIndex = 10
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.Color.MediumPurple
		self._groupBox1.Controls.Add(self._label11)
		self._groupBox1.Controls.Add(self._label10)
		self._groupBox1.Controls.Add(self._label9)
		self._groupBox1.Controls.Add(self._label8)
		self._groupBox1.Controls.Add(self._label7)
		self._groupBox1.Controls.Add(self._label6)
		self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox1.Location = System.Drawing.Point(12, 196)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(346, 167)
		self._groupBox1.TabIndex = 11
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Reace Results"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Thistle
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.Black
		self._label6.Location = System.Drawing.Point(51, 44)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(107, 24)
		self._label6.TabIndex = 0
		self._label6.Text = "1st Place:"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Thistle
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.Color.Black
		self._label7.Location = System.Drawing.Point(51, 82)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(107, 24)
		self._label7.TabIndex = 1
		self._label7.Text = "2nd Place:"
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Thistle
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.ForeColor = System.Drawing.Color.Black
		self._label8.Location = System.Drawing.Point(51, 120)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(107, 24)
		self._label8.TabIndex = 2
		self._label8.Text = "3rd Place:"
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.Thistle
		self._label9.ForeColor = System.Drawing.Color.Black
		self._label9.Location = System.Drawing.Point(169, 44)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(136, 24)
		self._label9.TabIndex = 3
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.Thistle
		self._label10.ForeColor = System.Drawing.Color.Black
		self._label10.Location = System.Drawing.Point(169, 82)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(136, 24)
		self._label10.TabIndex = 4
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.Thistle
		self._label11.ForeColor = System.Drawing.Color.Black
		self._label11.Location = System.Drawing.Point(169, 120)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(136, 24)
		self._label11.TabIndex = 5
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 369)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(107, 32)
		self._button1.TabIndex = 12
		self._button1.Text = "Results"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(125, 369)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(121, 32)
		self._button2.TabIndex = 13
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(252, 369)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(106, 32)
		self._button3.TabIndex = 14
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkOrchid
		self.ClientSize = System.Drawing.Size(370, 408)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._textBox6)
		self.Controls.Add(self._textBox5)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Pg269Race"
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button2Click(self, sender, e):
		self._label9.Text = " "
		self._label10.Text = " "
		self._label11.Text = " "
		self._textBox1.Clear()
		self._textBox2.Clear()
		self._textBox3.Clear()
		self._textBox4.Clear()
		self._textBox5.Clear()
		self._textBox6.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()

	def Button1Click(self, sender, e):
		r = int(self._textBox2.Text)
		s = int(self._textBox4.Text)
		g = int(self._textBox6.Text)
		if r<s<g:
			self._label9.Text = self._textBox1.Text
			self._label10.Text = self._textBox3.Text
			self._label11.Text = self._textBox5.Text
		elif r<g<s:
			self._label9.Text = self._textBox1.Text
			self._label10.Text = self._textBox5.Text
			self._label11.Text = self._textBox3.Text
		elif g<s<r:
			self._label9.Text = self._textBox5.Text
			self._label10.Text = self._textBox3.Text
			self._label11.Text = self._textBox1.Text
		elif g<r<s:
			self._label9.Text = self._textBox5.Text
			self._label10.Text = self._textBox1.Text
			self._label11.Text = self._textBox3.Text
		elif s<g<r:
			self._label9.Text = self._textBox3.Text
			self._label10.Text = self._textBox5.Text
			self._label11.Text = self._textBox1.Text
		elif s<r<g:
			self._label9.Text = self._textBox3.Text
			self._label10.Text = self._textBox1.Text
			self._label11.Text = self._textBox5.Text